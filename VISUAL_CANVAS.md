# Visual Canvas Feature

## Overview

The Visual Canvas Generator creates a professional, print-ready HTML representation of your AI ROI & Roadmap Canvas that matches the standard industry format.

## Features

### Professional Layout
- **Header Section**: Organization name, designer info, date, version
- **Objectives**: Strategic goals and focus areas
- **Grid Layout**: Inputs, Impacts, Timeline organized in columns
- **Risk & Capabilities**: Comprehensive risk assessment and capability requirements
- **Financial Overview**: Costs and benefits breakdown
- **Portfolio ROI**: High-level ROI metrics with visual emphasis

### Design Elements
- Clean, professional typography
- Print-optimized layout
- Responsive grid system
- Icon indicators for each section
- Color-coded ROI metrics
- Bordered sections for clarity

## How to Use

### In the Streamlit App

1. Complete all 4 phases of the agent interview
2. Navigate to the "🗺️ Canvas" tab
3. Select **"📊 Visual Canvas"** from the view mode options
4. The visual canvas will render in the browser
5. Click **"⬇️ Download Visual Canvas (HTML)"** to save

### From Command Line

Convert any canvas JSON to visual HTML:

```bash
python generate_visual_canvas.py input_canvas.json output_visual.html
```

Or simply:

```bash
python generate_visual_canvas.py my_canvas.json
```

This creates `my_canvas_visual.html` automatically.

## Viewing and Sharing

### Open in Browser
Double-click the HTML file to open it in your default browser.

### Print to PDF
1. Open the HTML file in your browser
2. Press Ctrl+P (Cmd+P on Mac) to print
3. Select "Save as PDF" as the destination
4. Adjust settings if needed
5. Save your PDF

### Present in Meetings
- Open the HTML file in a browser
- Present in full-screen mode (F11)
- Professional layout ready for executive presentations

### Email or Share
The HTML file is self-contained - all styles are embedded. You can:
- Attach it to emails
- Share via cloud storage
- Host on a web server
- Include in documentation

## Customization

The visual layout is defined in `src/visual_canvas.py`. You can customize:

### Colors
Edit the CSS color values:
```css
.roi-value {
    color: #2563eb;  /* Change this hex code */
}
```

### Fonts
Modify the font-family in the CSS:
```css
font-family: 'Your Font', sans-serif;
```

### Layout
Adjust grid columns in the CSS:
```css
grid-template-columns: 1fr 1fr 2fr;  /* Adjust ratios */
```

### Icons
Change the emoji icons in the HTML:
```python
"<div class='cell-icon'>🎯</div>"  # Change emoji
```

## Comparison with Other Formats

| Format | Use Case | Strengths |
|--------|----------|-----------|
| **Visual HTML** | Presentations, executive review | Beautiful layout, professional appearance, print-ready |
| **JSON** | Integration with other tools | Structured data, machine-readable, programmable |
| **Markdown** | Documentation, version control | Plain text, easy to edit, git-friendly |

## Technical Details

### Browser Compatibility
- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+

### File Size
Typical canvas HTML: 50-100 KB (very lightweight)

### Dependencies
None! The HTML is completely self-contained with embedded CSS.

### Accessibility
- Semantic HTML structure
- Proper heading hierarchy
- Readable color contrast
- Print-optimized styles

## Examples

See the generated HTML files for examples of:
- Small portfolio (3-5 use cases)
- Medium portfolio (6-10 use cases)
- Large portfolio (10+ use cases)

All layouts scale gracefully based on content size.
