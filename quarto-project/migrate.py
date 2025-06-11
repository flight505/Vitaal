#!/usr/bin/env python3
"""
Vitaal Business Plan Migration Utilities
Helps convert Mermaid diagrams to D2 and provides other migration tools
"""

import re
import sys
from pathlib import Path

# Vitaal brand colors
BRAND_COLORS = {
    'primary': '#0B4F71',      # Trust Blue
    'secondary': '#4FB06D',    # Vitality Green
    'accent': '#F39C12',       # Energy Orange
    'dark': '#2C3E50',         # Dark Grey
    'light': '#ECF0F1',        # Light Grey
}

def convert_mermaid_to_d2_basic(mermaid_code):
    """
    Basic converter from Mermaid to D2 syntax
    This handles simple conversions - complex diagrams need manual adjustment
    """
    d2_code = mermaid_code
    
    # Convert graph direction
    d2_code = re.sub(r'graph\s+(TD|TB)', 'direction: down', d2_code)
    d2_code = re.sub(r'graph\s+LR', 'direction: right', d2_code)
    d2_code = re.sub(r'graph\s+RL', 'direction: left', d2_code)
    d2_code = re.sub(r'graph\s+BT', 'direction: up', d2_code)
    
    # Convert simple arrows
    d2_code = re.sub(r'-->', '->', d2_code)
    d2_code = re.sub(r'---', '->', d2_code)
    
    # Convert node definitions with text
    d2_code = re.sub(r'\[([^\]]+)\]', r': "\1"', d2_code)
    d2_code = re.sub(r'\(([^\)]+)\)', r': "\1" {\n  shape: circle\n}', d2_code)
    d2_code = re.sub(r'\{([^\}]+)\}', r': "\1" {\n  shape: diamond\n}', d2_code)
    
    # Add D2 styling
    styled_d2 = f"""# Converted from Mermaid - requires manual refinement

{d2_code}

# Apply Vitaal brand styling
style: {{
  fill: "{BRAND_COLORS['light']}"
  stroke: "{BRAND_COLORS['dark']}"
  font-color: "{BRAND_COLORS['dark']}"
}}
"""
    
    return styled_d2

def extract_mermaid_from_markdown(md_file):
    """Extract all Mermaid diagrams from a markdown file"""
    with open(md_file, 'r') as f:
        content = f.read()
    
    # Find all mermaid blocks
    pattern = r'```mermaid\n(.*?)\n```'
    diagrams = re.findall(pattern, content, re.DOTALL)
    
    return diagrams

def create_vega_chart_template(chart_type='line'):
    """Create a Vega-Lite chart template with Vitaal branding"""
    
    templates = {
        'line': {
            "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
            "title": {
                "text": "Chart Title",
                "font": "SF Pro Display",
                "fontSize": 18,
                "color": BRAND_COLORS['primary']
            },
            "data": {"values": []},
            "mark": {
                "type": "line",
                "strokeWidth": 3,
                "color": BRAND_COLORS['primary']
            },
            "encoding": {
                "x": {"field": "x", "type": "quantitative"},
                "y": {"field": "y", "type": "quantitative"}
            }
        },
        'bar': {
            "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
            "title": {
                "text": "Chart Title",
                "font": "SF Pro Display", 
                "fontSize": 18,
                "color": BRAND_COLORS['primary']
            },
            "data": {"values": []},
            "mark": {
                "type": "bar",
                "cornerRadius": 4,
                "color": BRAND_COLORS['primary']
            },
            "encoding": {
                "x": {"field": "category", "type": "nominal"},
                "y": {"field": "value", "type": "quantitative"}
            }
        }
    }
    
    return templates.get(chart_type, templates['line'])

def update_citations(content):
    """Convert inline citations to Quarto format"""
    # Convert (Author, Year) to [@authorYear]
    pattern = r'\(([A-Za-z\s&]+),\s*(\d{4})\)'
    
    def replace_citation(match):
        authors = match.group(1)
        year = match.group(2)
        # Simplify author names for citation keys
        key = authors.lower().replace(' ', '').replace('&', '').replace(',', '')
        key = re.sub(r'etal\.?', '', key)
        return f'[@{key}{year}]'
    
    return re.sub(pattern, replace_citation, content)

def main():
    """Main migration helper"""
    if len(sys.argv) < 2:
        print("Usage: python migrate.py [command] [args]")
        print("Commands:")
        print("  mermaid2d2 <file>  - Extract and convert Mermaid diagrams")
        print("  citations <file>   - Update citations to Quarto format")
        print("  vega <type>        - Create Vega-Lite template")
        return
    
    command = sys.argv[1]
    
    if command == 'mermaid2d2' and len(sys.argv) > 2:
        file_path = sys.argv[2]
        diagrams = extract_mermaid_from_markdown(file_path)
        for i, diagram in enumerate(diagrams):
            d2_code = convert_mermaid_to_d2_basic(diagram)
            output_file = f"diagram_{i+1}.d2"
            with open(output_file, 'w') as f:
                f.write(d2_code)
            print(f"Created {output_file}")
    
    elif command == 'citations' and len(sys.argv) > 2:
        file_path = sys.argv[2]
        with open(file_path, 'r') as f:
            content = f.read()
        updated = update_citations(content)
        print(updated)
    
    elif command == 'vega' and len(sys.argv) > 2:
        chart_type = sys.argv[2]
        template = create_vega_chart_template(chart_type)
        print(json.dumps(template, indent=2))

if __name__ == "__main__":
    main()
