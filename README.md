# Vitaal Klinic Business Plan

Denmark's Premier Metabolic Health & Longevity Center

## Overview

This repository contains the comprehensive business plan for Vitaal Klinic, an innovative healthcare venture combining:
- GLP-1 metabolic optimization therapy
- Hyperbaric oxygen therapy (HBOT)
- Precision genetic testing
- Advanced biomarker monitoring
- Digital health platform (Vitaal Digital)

**Location**: Jagtvej 113, 1. sal, 2200 Copenhagen N  
**Founders**: Dr. Peyman Pedrampour (GP) & Dr. Jesper Vang (PhD Bioinformatics)

## Current Status ✅

**Business Plan Complete** - All sections created with 50+ diagrams and comprehensive financial projections.

**Professional Document System** - Quarto-based compilation with D2 diagrams and Vega-Lite charts for publication-ready output.

**Latest Update (v2.0.0)** - Migration to professional document system with consistent branding and enhanced visualizations.

## Repository Structure

```
.
├── quarto-project/        # Professional document compilation (NEW)
│   ├── _quarto.yml       # Quarto configuration
│   ├── *.qmd             # Chapter files
│   ├── diagrams/         # D2 diagram sources
│   ├── charts/           # Vega-Lite specifications
│   └── _output/          # Generated PDF/HTML
├── docs/
│   ├── sections/          # Original business plan chapters
│   │   ├── 00_vitaal_executive_summary.md
│   │   ├── 01_vitaal_market_analysis.md
│   │   ├── 02_vitaal_clinical_services.md
│   │   ├── 03_vitaal_technology_platform.md
│   │   ├── 04_vitaal_financial_projections.md
│   │   ├── 05_vitaal_implementation_roadmap.md
│   │   └── 06_vitaal_next_steps.md
│   ├── compiled/          # Complete compiled documents
│   │   └── Vitaal_Business_Plan_v1.0.md
│   └── CREATION_SUMMARY.md # Overview of all content
├── assets/                # Images, diagrams, and supporting data
├── scripts/              # Automation scripts
├── references/           # Bibliography and citations
└── pdfs/                # PDF versions
```

## Quick Start

### Building Professional Documents (NEW)

1. Navigate to the Quarto project:
   ```bash
   cd quarto-project
   ```

2. Build all formats:
   ```bash
   ./build.sh
   ```

3. View outputs in `_output/` directory:
   - `Vitaal-Business-Plan.pdf` - Professional PDF
   - `index.html` - Interactive HTML version

### Original Markdown Files

1. Clone the repository:
   ```bash
   git clone https://github.com/flight505/Vitaal.git
   cd Vitaal
   ```

2. View original business plan sections in `docs/sections/`

## Key Highlights

- **Investment Needed**: €1.5-2.0 million
- **Target Market**: 25,000 HNW households in Denmark
- **Revenue Projection**: €28.5M by Year 3
- **Break-even**: Month 14-16
- **First-Mover Advantage**: No HBOT longevity centers in Denmark

## Diagrams and Visualizations

The business plan includes 50+ professional diagrams and charts:

### Original Format (Mermaid)
- Market analysis and segmentation
- Clinical protocols and workflows
- Technology architecture
- Financial projections
- Implementation timelines

### Enhanced Format (D2 + Vega-Lite)
- **D2 Diagrams**: Superior layouts with consistent branding
- **Vega-Lite Charts**: Interactive, data-driven visualizations
- **Professional Styling**: Vitaal brand colors and typography

To view enhanced diagrams:
- Open HTML output in `quarto-project/_output/`
- Or generate from source in `quarto-project/diagrams/`

## Working with Sections

Each section is a standalone markdown file in `docs/sections/`. To edit:

1. Open the relevant section file
2. Make your changes
3. Run citation check: `./scripts/check_citations.sh`
4. Commit changes with descriptive message

## Citation Management

Harvard (Author, Year) style with 22 references including:
- Clinical studies (SELECT trial, HBOT research)
- Danish regulatory documents
- Market analysis reports
- Technology frameworks

## Next Steps

1. **Board Review**: Share compiled business plan
2. **Investor Deck**: Extract key slides from sections
3. **Regulatory Filing**: Use Section 05 for STPS applications
4. **Team Building**: Follow Section 06 action plan

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- Writing style and formatting
- Citation requirements
- Commit messages
- Pull request process

## Confidentiality

This repository contains confidential business information. Do not share without authorization from the founders.

## Contact

- **CEO/Technology**: Dr. Jesper Vang - jesper@vitaalklinic.dk
- **Medical Director**: Dr. Peyman Pedrampour - peyman@vitaalklinic.dk
- **Location**: Jagtvej 113, 1. sal, 2200 Copenhagen N

---

© 2025 Vitaal Klinic. All rights reserved.