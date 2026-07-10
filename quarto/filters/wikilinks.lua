-- wikilinks.lua
--
-- Traduce wikilinks de Obsidian (doble corchete) a sintaxis nativa de
-- Quarto durante el render, para poder escribir en Obsidian (con graph
-- view y backlinks reales) y publicar con Quarto sin tocar el fuente.
--
-- Reglas:
--
-- 1. Wikilink a un id tipo "exm-algo"  ->  @exm-algo  (crossref Quarto)
--    Prefijos reconocidos: exm tbl fig eq sec thm lem def cor prp
--
-- 2. Wikilink con alias a un id de crossref -> link manual al ancla
--    (Quarto crossref con @ no soporta texto custom directo)
--
-- 3. Wikilink a "Nombre de otra nota" -> link al archivo .html
--    El nombre se "slugifica" (minúsculas, espacios -> guiones, sin
--    tildes) asumiendo que así se llaman tus archivos .html.
--
-- 4. Wikilink con alias a una nota -> link al archivo con el alias
--    como texto visible.
--
-- Activación: registrado en _quarto.yml bajo:
--   filters:
--     - filters/wikilinks.lua
--
-- Pandoc no reconoce el doble corchete como sintaxis nativa, así que
-- llega como texto plano (Str). Este filtro reconstruye ese texto
-- crudo a nivel de Para/Plain y lo reemplaza por Inlines de Quarto.

local CROSSREF_PREFIXES = {
  ["exm"] = true, ["tbl"] = true, ["fig"] = true, ["eq"]  = true,
  ["sec"] = true, ["thm"] = true, ["lem"] = true, ["def"] = true,
  ["cor"] = true, ["prp"] = true,
}

local function strip_accents(s)
  local map = {
    ["á"]="a", ["é"]="e", ["í"]="i", ["ó"]="o", ["ú"]="u",
    ["Á"]="A", ["É"]="E", ["Í"]="I", ["Ó"]="O", ["Ú"]="U",
    ["ñ"]="n", ["Ñ"]="N", ["ü"]="u", ["Ü"]="U",
  }
  local out = {}
  for _, cp in utf8.codes(s) do
    local ch = utf8.char(cp)
    table.insert(out, map[ch] or ch)
  end
  return table.concat(out)
end

local function slugify(s)
  s = strip_accents(s)
  s = s:lower()
  s = s:gsub("[^%w%s%-_]", "")  -- %w no incluye _ en Lua, se agrega explícitamente
  s = s:gsub("%s+", "-")
  s = s:gsub("%-+", "-")
  s = s:gsub("^%-+", ""):gsub("%-+$", "")
  return s
end

-- Slugify para anchors (#heading) — preserva acentos para coincidir con
-- Pandoc/Quarto auto_identifiers (que trata letras acentuadas como letras,
-- no como puntuación).
local function slugify_anchor(s)
  s = s:gsub("^%^", "")  -- remueve prefijo ^ para block IDs
  s = s:lower()
  s = s:gsub("%s+", "-")
  s = s:gsub("%-+", "-")
  s = s:gsub("^%-+", ""):gsub("%-+$", "")
  return s
end

local function is_crossref_id(target)
  local prefix = target:match("^(%a+)%-")
  return prefix ~= nil and CROSSREF_PREFIXES[prefix] == true
end

local function build_replacement(target, alias)
  target = target:gsub("^%s+", ""):gsub("%s+$", "")
  if alias then alias = alias:gsub("^%s+", ""):gsub("%s+$", "") end

  if is_crossref_id(target) then
    if alias then
      return pandoc.Link(pandoc.Str(alias), "#" .. target)
    else
      local citation = pandoc.Citation(target, "AuthorInText")
      return pandoc.Cite({ pandoc.Str("@" .. target) }, { citation })
    end
  else
    local file_part, anchor_part = target:match("^(.-)#(.-)$")
    local href, label
    if file_part then
      local slug_anchor = slugify_anchor(anchor_part)
      if file_part == "" then
        href = "#" .. slug_anchor
        label = alias or anchor_part
      else
        href = slugify(file_part) .. ".html#" .. slug_anchor
        label = alias or anchor_part
      end
    else
      href = slugify(target) .. ".html"
      label = alias or target
    end
    return pandoc.Link(pandoc.Str(label), href)
  end
end

local function process_inlines(inlines)
  local result = pandoc.List()
  local i = 1
  while i <= #inlines do
    local el = inlines[i]
    if el.t == "Str" and el.text:find("%[%[") then
      local buffer = {}
      local j = i
      local closed = false
      while j <= #inlines do
        local e2 = inlines[j]
        if e2.t == "Str" then
          table.insert(buffer, e2.text)
        elseif e2.t == "Space" then
          table.insert(buffer, " ")
        elseif e2.t == "SoftBreak" then
          table.insert(buffer, " ")
        else
          break
        end
        if e2.t == "Str" and e2.text:find("%]%]") then
          closed = true
          j = j + 1
          break
        end
        j = j + 1
      end

      local merged = table.concat(buffer)
      if closed and merged:find("%[%[.-%]%]") then
        local remaining = merged
        while remaining do
          local s, e, link_body = remaining:find("%[%[(.-)%]%]")
          if not s then
            if #remaining > 0 then
              result:insert(pandoc.Str(remaining))
            end
            break
          end
          local before = remaining:sub(1, s - 1)
          if #before > 0 then
            result:insert(pandoc.Str(before))
          end
          local target, alias = link_body:match("^(.-)|(.*)$")
          if not target then target = link_body end
          result:insert(build_replacement(target, alias))
          remaining = remaining:sub(e + 1)
        end
        i = j
      else
        result:insert(el)
        i = i + 1
      end
    else
      result:insert(el)
      i = i + 1
    end
  end
  return result
end

function Pandoc(doc)
  doc.blocks = doc.blocks:walk {
    Para = function(p)
      p.content = process_inlines(p.content)
      return p
    end,
    Plain = function(p)
      p.content = process_inlines(p.content)
      return p
    end,
  }
  return doc
end
