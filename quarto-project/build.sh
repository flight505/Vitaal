#!/bin/bash
# Vitaal Business Plan Build Script

set -e  # Exit on error

echo "🚀 Building Vitaal Business Plan..."

# Ensure we're in the right directory
cd "$(dirname "$0")"

# Check dependencies
echo "📋 Checking dependencies..."
command -v quarto >/dev/null 2>&1 || { echo "❌ Quarto is required but not installed."; exit 1; }
command -v d2 >/dev/null 2>&1 || { echo "❌ D2 is required but not installed."; exit 1; }

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf _output

# Render the book
echo "📚 Rendering book..."
quarto render

# Generate different formats
echo "📄 Generating PDF..."
quarto render --to pdf

echo "🌐 Generating HTML..."
quarto render --to html

echo "✅ Build complete! Output in _output/"
echo ""
echo "📂 Generated files:"
ls -la _output/

# Open the HTML version
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "🌐 Opening HTML preview..."
    open _output/index.html
fi
