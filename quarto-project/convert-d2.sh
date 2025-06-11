#!/bin/bash
# Convert D2 diagrams to PNG files

set -e

echo "🎨 Converting D2 diagrams to PNG..."

# Ensure output directory exists
mkdir -p diagrams/output

# Convert each D2 file
for d2_file in diagrams/*.d2; do
    if [ -f "$d2_file" ]; then
        filename=$(basename "$d2_file" .d2)
        echo "Converting $filename..."
        d2 --theme 0 --layout elk "$d2_file" "diagrams/output/${filename}.png"
    fi
done

echo "✅ D2 conversion complete!"
