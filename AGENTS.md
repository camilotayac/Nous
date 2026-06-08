# Nous — Cuaderno de Apuntes

Book project en Quarto con dos materias: Química General y Conjuntos (Teoría de Conjuntos).

## Estructura

```
/
├── index.qmd                    # Homepage
├── _quarto.yml                  # Config principal
├── _brand.yml                   # Colores del tema
├── AGENTS.md                    # Este archivo
├── references.qmd               # Página de referencias
├── references.bib               # Bibliografía
├── .github/workflows/publish.yml  # Deploy a gh-pages
├── _extensions/juba/bookup/     # Tema bookup (HTML)
├── assets/
│   ├── css/custom.css           # Breadcrumb styling
│   ├── js/sidebar-autocollapse.html  # Auto-colapso sidebar
│   └── images/cover.png         # Portada
├── Química_General/
│   ├── index.qmd
│   ├── 01-estructura-atomica.qmd
│   ├── 02-enlaces-quimicos.qmd
│   └── 03-reacciones.qmd
└── Conjuntos/
    ├── index.qmd
    ├── 01-teoria-de-conjuntos.qmd
    ├── 02-operaciones.qmd
    └── 03-producto-cartesiano.qmd
```

## Formatos

- **HTML**: `bookup-html` (tema bookup, sidebar unificado, breadcrumb, auto-colapso)
- **PDF**: `typst` (orange-book, colors from _brand.yml)

## Comandos

```bash
quarto render               # Renderiza todo
quarto preview              # Preview local
quarto render --to typst    # Solo PDF
```

## Convenciones

- Nombres de archivos en kebab-case o descriptivos
- Assets estáticos en `assets/{css,js,images}/`
- Cada materia en su propia carpeta con `index.qmd` + capítulos numerados
