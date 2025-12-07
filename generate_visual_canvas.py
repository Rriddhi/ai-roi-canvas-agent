#!/usr/bin/env python3
"""
Standalone Visual Canvas Generator

Usage:
    python generate_visual_canvas.py canvas.json output.html

Reads a canvas JSON file and generates a beautiful visual HTML representation.
"""

import json
import sys
from pathlib import Path
from src.visual_canvas import generate_visual_canvas_html


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_visual_canvas.py <canvas.json> [output.html]")
        print("\nExample:")
        print("  python generate_visual_canvas.py my_canvas.json")
        print("  python generate_visual_canvas.py my_canvas.json visual_canvas.html")
        sys.exit(1)
    
    input_file = Path(sys.argv[1])
    
    # Determine output file
    if len(sys.argv) >= 3:
        output_file = Path(sys.argv[2])
    else:
        output_file = input_file.with_stem(f"{input_file.stem}_visual").with_suffix(".html")
    
    # Read JSON
    try:
        with open(input_file, 'r') as f:
            canvas_data = json.load(f)
        print(f"✓ Loaded canvas from: {input_file}")
    except FileNotFoundError:
        print(f"✗ Error: File not found: {input_file}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"✗ Error: Invalid JSON in {input_file}")
        print(f"  {e}")
        sys.exit(1)
    
    # Generate HTML
    try:
        html_content = generate_visual_canvas_html(canvas_data)
        print(f"✓ Generated visual canvas HTML")
    except Exception as e:
        print(f"✗ Error generating HTML: {e}")
        sys.exit(1)
    
    # Write output
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"✓ Saved visual canvas to: {output_file}")
        print(f"\n✨ Success! Open {output_file} in your browser to view the canvas.")
    except Exception as e:
        print(f"✗ Error writing file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
