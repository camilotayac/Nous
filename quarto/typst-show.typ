// =============================================================================
// NOUS - Custom Typst Book Template
// Faithfully reproducing LaTeX preamble.tex design
// =============================================================================

#let nouscolor = rgb("#2980B9")
#let nousbg = rgb(212, 230, 241) // Exactly nouscolor!20 in LaTeX
#let font-serif = "$if(mainfont)$$mainfont$$else$Libertinus Serif$endif$"
#let font-sans = ("Helvetica Neue", "Arial")
#let font-mono = "DejaVu Sans Mono"

#let part-state = state("part-state", "Inicio")
#let part-counter = counter("part-counter")
#let appendix-state = state("appendix-state", none)

// -----------------------------------------------------------------------------
// Part Page Definition (matching LaTeX \nouspagebackground + \partheadendvskip)
// -----------------------------------------------------------------------------
#let part(title) = {
  [#metadata("end") <ch-end>]
  pagebreak(to: "odd")
  [#metadata("start") <ch-start>]
  part-state.update(title)
  part-counter.step()
  counter(heading).update(0)
  [
    #metadata("part") <part-marker>
    // Full-bleed tinted background (matching \nouspagebackground in LaTeX)
    #place(top + left, dx: -2.5cm, dy: -2.8cm,
      rect(width: 8.5in, height: 11in, fill: nousbg)
    )
    #v(22%)
    #align(left)[
      #text(font: font-sans, size: 32pt, weight: "bold", fill: black, title)
      #v(0.6cm)
      #line(length: 100%, stroke: 2.5pt + nouscolor)

      // Local list of chapters in this part (matching \localtableofcontents)
      #context {
        let here-loc = here()
        let next-part = query(selector(<part-marker>).after(here-loc))
        let part-chapters = if next-part.len() > 0 {
          query(selector(heading.where(level: 1)).after(here-loc).before(next-part.first().location()))
        } else {
          query(selector(heading.where(level: 1)).after(here-loc))
        }

        if part-chapters.len() > 0 {
          v(0.8cm)
          let cols = if part-chapters.len() > 8 { 2 } else { 1 }
          grid(
            columns: (1fr,) * cols,
            row-gutter: 0.65em,
            column-gutter: 1.5cm,
            ..part-chapters.map(ch => {
              text(font: font-serif, size: 8.5pt, fill: luma(60))[#ch.body]
            })
          )
        }
      }
    ]
  ]
}

// -----------------------------------------------------------------------------
// Appendix Support
// -----------------------------------------------------------------------------
#let appendices(title, hide-parent: false, body) = {
  counter(heading).update(0)
  appendix-state.update(title)
  set heading(numbering: (..nums) => {
    let vals = nums.pos()
    if vals.len() == 1 {
      numbering("A.", ..vals)
    } else {
      numbering("A.1", ..vals)
    }
  })
  body
}

// Dummy chapter function in case of imports
#let chapter(title) = {
  heading(level: 1)[#title]
}

// -----------------------------------------------------------------------------
// Main Book Function
// -----------------------------------------------------------------------------
#let book(
  title: "$title$",
  subtitle: "$subtitle$",
  author: "$for(by-author)$$it.name.literal$$sep$, $endfor$",
  date: "$date$",
  lang: "$lang$",
  main-color: nouscolor,
  logo: none,
  outline-depth: $if(toc-depth)$$toc-depth$$else$2$endif$,
  body,
) = {
  set document(title: title, author: author)
  set text(font: font-serif, size: 10.5pt, lang: lang)
  set par(justify: true, leading: 0.65em)

  // Heading numbering for cross-references
  set heading(
    numbering: (..nums) => {
      let vals = nums.pos()
      let pattern = if vals.len() == 1 { "1." }
                    else if vals.len() <= 4 { "1.1" }
      if pattern != none { numbering(pattern, ..nums) }
    }
  )

  // Hyperlinks & citations in nouscolor (matching \hypersetup in LaTeX)
  show link: set text(fill: nouscolor)
  show ref: set text(fill: nouscolor)
  show cite: set text(fill: nouscolor)

  // Table booktabs styling
  set table(
    stroke: (x, y) => if y == 0 {
      (top: 1.5pt + black, bottom: 1pt + nouscolor)
    } else {
      none
    },
    fill: (col, row) => if row == 0 {
      nousbg.lighten(65%)
    } else if calc.odd(row) {
      rgb("#fafbfc")
    } else {
      none
    },
    inset: (x: 8pt, y: 6pt),
  )
  show table.cell.where(y: 0): set text(font: font-sans, weight: "bold", size: 9.5pt)
  set table.hline(stroke: 0.6pt + luma(160))

  // Figure captions: top for tables, bottom for images
  show figure.where(kind: "quarto-float-tbl"): set figure.caption(position: top)
  show figure.where(kind: "quarto-float-fig"): set figure.caption(position: bottom)
  show figure.caption: set text(font: font-sans, size: 9pt)

  // Running headers and footers (matching scrheadings in LaTeX)
  set page(
    paper: "us-letter",
    margin: (x: 2.5cm, top: 2.8cm, bottom: 2.5cm),
    header: context {
      let pg = here().page()

      // Suppress on cover, TOC pages, part pages, and chapter first pages
      let h1s = query(heading.where(level: 1))
      let first-h1 = h1s.at(0, default: none)
      if first-h1 != none and pg < first-h1.location().page() {
        return none
      }

      let on-cover = query(selector(<cover-marker>)).any(it => it.location().page() == pg)
      let on-part = query(selector(<part-marker>)).any(it => it.location().page() == pg)
      let on-h1 = h1s.any(it => it.location().page() == pg)

      // Suppress on blank transition pages
      let ends = query(selector(<ch-end>))
      let starts = query(selector(<ch-start>))
      let is-blank = range(ends.len()).any(i => {
        let ep = ends.at(i).location().page()
        if i + 1 < starts.len() {
          let sp = starts.at(i + 1).location().page()
          pg > ep and pg < sp
        } else {
          false
        }
      })

      if on-cover or on-part or on-h1 or is-blank {
        return none
      }

      let before-h1 = query(selector(heading.where(level: 1)).before(here()))
      let before-h2 = query(selector(heading.where(level: 2)).before(here()))
      let ch-title = if before-h1.len() > 0 { before-h1.last().body } else { title }
      let sec-title = if before-h2.len() > 0 { before-h2.last().body } else { ch-title }

      if calc.even(pg) {
        grid(
          columns: (auto, 1fr),
          align: (left, right),
          text(font: font-sans, size: 9pt, weight: "bold", fill: nouscolor)[#pg],
          text(font: font-sans, size: 8.5pt, fill: luma(100))[#ch-title],
        )
        v(2pt)
        line(length: 100%, stroke: 0.4pt + luma(200))
      } else {
        grid(
          columns: (1fr, auto),
          align: (left, right),
          text(font: font-sans, size: 8.5pt, fill: luma(100))[#sec-title],
          text(font: font-sans, size: 9pt, weight: "bold", fill: nouscolor)[#pg],
        )
        v(2pt)
        line(length: 100%, stroke: 0.4pt + luma(200))
      }
    },
    footer: none,
  )

  // Chapter Headings (Level 1)
  show heading.where(level: 1): it => {
    // Reset figure, table, and equation counters
    counter(figure.where(kind: "quarto-float-fig")).update(0)
    counter(figure.where(kind: "quarto-float-tbl")).update(0)
    counter(figure.where(kind: "quarto-float-lst")).update(0)
    counter(figure.where(kind: "quarto-callout-Note")).update(0)
    counter(figure.where(kind: "quarto-callout-Warning")).update(0)
    counter(figure.where(kind: "quarto-callout-Caution")).update(0)
    counter(figure.where(kind: "quarto-callout-Tip")).update(0)
    counter(figure.where(kind: "quarto-callout-Important")).update(0)
    counter(math.equation).update(0)

    [#metadata("end") <ch-end>]
    pagebreak(to: "odd")
    [#metadata("start") <ch-start>]
    v(1.5cm)
    block(width: 100%)[
      #set text(font: font-sans, fill: black)
      #text(size: 22pt, weight: "bold")[#it.body]
      #v(0.4cm)
      #line(length: 100%, stroke: 1.5pt + nouscolor)
    ]
    v(0.8cm)
  }

  // Section Headings (Level 2)
  show heading.where(level: 2): it => {
    v(1.8em, weak: true)
    set text(font: font-sans, size: 13.5pt, weight: "bold", fill: black)
    it
    v(0.8em, weak: true)
  }

  // Subsection Headings (Level 3)
  show heading.where(level: 3): it => {
    v(1.3em, weak: true)
    set text(font: font-sans, size: 11pt, weight: "bold", fill: black)
    it
    v(0.5em, weak: true)
  }

  // ===========================================================================
  // 1. Cover Page
  // ===========================================================================
  [
    #metadata("cover") <cover-marker>
    #metadata("start") <ch-start>
    #set page(margin: 0cm, header: none, footer: none)
    #place(top + left, rect(width: 100%, height: 100%, fill: rgb("#fafcff")))
    #align(center + horizon)[
      #v(2cm)
      #text(font: font-sans, size: 44pt, weight: "bold", fill: nouscolor)[#title]
      #v(0.4cm)
      #text(font: font-sans, size: 16pt, fill: luma(80))[#author]
      #v(1.5cm)
      #image("cover.png", width: 55%)
      #v(1.5cm)
      #text(font: font-sans, size: 12pt, fill: luma(120))[#date]
      #v(2cm)
    ]
    #metadata("end") <ch-end>
  ]
  pagebreak(to: "odd")

  // ===========================================================================
  // 2. TOC Title Page (matching LaTeX \nouspagebackground)
  // ===========================================================================
  [
    #metadata("toc") <toc-marker>
    #metadata("start") <ch-start>
    #place(top + left, dx: -2.5cm, dy: -2.8cm,
      rect(width: 8.5in, height: 11in, fill: nousbg)
    )
    #v(35%)
    #align(left)[
      #text(font: font-sans, size: 32pt, weight: "bold", fill: black)[Índice]
      #v(0.6cm)
      #line(length: 100%, stroke: 2.5pt + nouscolor)
    ]
    #metadata("end") <ch-end>
  ]
  pagebreak(to: "odd")

  // ===========================================================================
  // 3. TOC Entries Page (matching LaTeX \DeclareTOCStyleEntry)
  // ===========================================================================
  [
    #metadata("start") <ch-start>
    #show outline.entry: it => {
      context {
        let loc = it.element.location()
        if it.level == 1 {
          let current-part = part-state.at(loc)
          let prev-h1 = query(selector(heading.where(level: 1)).before(loc))
          let is-first = if prev-h1.len() <= 1 {
            current-part != "Inicio"
          } else {
            let prev-loc = prev-h1.at(-2).location()
            part-state.at(prev-loc) != current-part
          }

          if is-first and current-part != "Inicio" and current-part != none {
            v(1.6em, weak: true)
            text(font: font-sans, size: 1.2em, weight: "bold", fill: nouscolor)[#current-part]
            v(0.6em, weak: true)
          }

          v(0.45em, weak: true)
          grid(
            columns: (1fr, auto),
            align: (left, right),
            link(loc, text(font: font-sans, weight: "bold", size: 10.5pt, fill: black)[#it.element.body]),
            link(loc, text(font: font-sans, weight: "bold", size: 10.5pt, fill: black)[#it.page()]),
          )
        } else if it.level == 2 {
          v(0.2em, weak: true)
          h(1.2em)
          grid(
            columns: (1fr, auto),
            align: (left, right),
            [
              #link(loc, text(font: font-serif, size: 9.5pt, fill: luma(60))[#it.element.body])
              #box(width: 1fr, repeat(text(fill: luma(180))[. #h(3pt)]))
            ],
            [
              #h(4pt)
              #link(loc, text(font: font-serif, size: 9.5pt, fill: luma(60))[#it.page()])
            ],
          )
        }
      }
    }
    #outline(title: none, depth: outline-depth, indent: 0pt)
  ]

  body
  [#metadata("end") <ch-end>]
}

#show: book.with()
