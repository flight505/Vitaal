# Vitaal Business Plan - Quarto Project

This is the professional document compilation for the Vitaal Klinic business plan using Quarto, D2 diagrams, and Vega-Lite charts.

## 📁 Project Structure

```
quarto-project/
├── _quarto.yml           # Main configuration
├── index.qmd             # Cover/landing page
├── 00-executive-summary.qmd  # Executive summary chapter
├── references.bib        # Bibliography (BibTeX format)
├── harvard-cite-them-right.csl  # Citation style
├── custom.scss           # HTML styling
├── latex/preamble.tex    # PDF styling
├── vitaal-theme.d2       # D2 diagram theme
├── vitaal-vega-theme.json # Vega-Lite theme
├── diagrams/             # D2 diagram sources
├── charts/               # Vega-Lite specifications
├── build.sh              # Build script
└── migrate.py            # Migration utilities
```

## 🚀 Quick Start

### Building the Document

```bash
# Make build script executable (first time only)
chmod +x build.sh

# Build all formats
./build.sh

# Or build specific format
quarto render --to pdf
quarto render --to html
```

### Output

Generated files will be in the `_output/` directory:
- `Vitaal-Business-Plan.pdf` - Professional PDF
- `index.html` - Interactive HTML version
- Supporting files and assets

## 🎨 Brand Theme

The Vitaal brand is consistently applied across all elements:

**Colors:**
- Primary: `#0B4F71` (Trust Blue)
- Secondary: `#4FB06D` (Vitality Green)
- Accent: `#F39C12` (Energy Orange)
- Dark: `#2C3E50`
- Light: `#ECF0F1`

**Typography:**
- Headings: SF Pro Display
- Body: SF Pro Text
- Monospace: SF Mono

## 📊 Creating Diagrams and Charts

### D2 Diagrams

```d2
# Example D2 diagram with Vitaal styling
title: My Diagram {
  near: top-center
}

Box1: {
  class: primary-box
  Label Text
}

Box2: {
  class: secondary-box
  Another Label
}

Box1 -> Box2
```

### Vega-Lite Charts

Charts are created as JSON specifications and rendered via Kroki or embedded Python blocks.

## ✍️ Writing Content

### Citations

Use Quarto citation format:
```markdown
This is supported by research [@hachmo2020].
Multiple citations [@mulvaney2024; @select2024].
```

### Cross-references

```markdown
See @fig-revenue-projection for details.
As shown in @tbl-financial-summary.
Discussed in @sec-market-analysis.
```

### Callout Boxes

```markdown
::: {.callout-note}
This is a note callout
:::

::: {.callout-important}
This is important
:::
```

## 🔧 Migration Tools

Use the `migrate.py` script for:
- Converting Mermaid diagrams to D2
- Updating citation formats
- Creating chart templates

```bash
python migrate.py mermaid2d2 input.md
python migrate.py citations input.md
python migrate.py vega line
```

## 📚 Key Quarto Features Used

1. **Book Project**: Multi-chapter structure with navigation
2. **Bibliography**: BibTeX + CSL for Harvard citations
3. **Cross-references**: Figures, tables, sections
4. **Multiple Formats**: PDF and HTML from same source
5. **Custom Styling**: SCSS for HTML, LaTeX for PDF
6. **Extensions**: D2 filter for diagrams

## 🆘 Troubleshooting

**D2 diagrams not rendering:**
- Ensure D2 is installed: `brew install d2`
- Check filter in _quarto.yml

**PDF errors:**
- Install TinyTeX: `quarto install tinytex`
- Check LaTeX preamble syntax

**Citation issues:**
- Verify BibTeX entries in references.bib
- Check CSL file is present

---

For questions: jesper@vitaalklinic.dk
