-- responsive-tables.lua
--
-- Añade la clase .responsive a todas las tablas del documento para que
-- Quarto genere tablas con scroll horizontal en pantallas pequeñas.
--
-- Activación: registrado en _quarto.yml bajo:
--   filters:
--     - filters/responsive-tables.lua

function Table(tbl)
  tbl.classes = tbl.classes or {}
  for _, cls in ipairs(tbl.classes) do
    if cls == "responsive" then
      return tbl
    end
  end
  table.insert(tbl.classes, "responsive")
  return tbl
end
