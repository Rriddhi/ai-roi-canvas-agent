"""
Export utilities for canvas in multiple formats (PNG, HTML, JSON, Markdown)
"""

import json
import io
from typing import Dict, Any


def export_to_json(canvas: Dict[str, Any]) -> str:
    """Export canvas as JSON string"""
    return json.dumps(canvas, indent=2, default=str)


def export_to_markdown(canvas: Dict[str, Any]) -> str:
    """Export canvas as Markdown for easy sharing and documentation"""
    
    md = f"""# {canvas['Header']['CanvasTitle']}

**Organization:** {canvas['Header']['Name']}  
**Designed By:** {canvas['Header']['DesignedBy']}  
**Designed For:** {canvas['Header']['DesignedFor']}  
**Date:** {canvas['Header']['Date']}  

---

## 🎯 Objectives

**Primary Goal:** {canvas['Objectives']['PrimaryGoal']}

**Strategic Focus:** {canvas['Objectives']['StrategicFocus']}

{canvas['Objectives'].get('Description', '')}

---

## 📊 Inputs (Resources & Costs)

### Total Investment
**Initial Cost:** ${canvas['Inputs']['InitialCost']:,.0f}

### Resources
**Personnel:**
"""
    
    for person in canvas['Inputs'].get('Personnel', []):
        md += f"- {person}\n"
    
    md += "\n**External Support:**\n"
    for support in canvas['Inputs'].get('ExternalSupport', []):
        md += f"- {support}\n"
    
    md += "\n---\n\n## 💡 Impacts (Benefits)\n\n### Hard Benefits\n"
    for benefit in canvas['Impacts']['HardBenefits']:
        md += f"- {benefit}\n"
    
    md += "\n### Soft Benefits\n"
    for benefit in canvas['Impacts'].get('SoftBenefits', []):
        md += f"- {benefit}\n"
    
    md += "\n---\n\n## 📅 Timeline & Milestones\n\n| AI Initiative | Start Date | End Date | Milestone |\n"
    md += "|---|---|---|---|\n"
    
    for item in canvas['TimelineAndMilestones']:
        md += f"| {item['AIInitiative']} | {item['StartDate']} | {item['EndDate']} | {item['Milestone']} |\n"
    
    md += "\n---\n\n## 📈 Financial Summary\n\n"
    if 'FinancialSummary' in canvas:
        md += f"**Total Near-term ROI:** {canvas['FinancialSummary'].get('TotalNearTermROI', 'N/A')}\n\n"
        md += f"**Total Long-term ROI:** {canvas['FinancialSummary'].get('TotalLongTermROI', 'N/A')}\n\n"
        md += f"**Portfolio NPV:** ${canvas['FinancialSummary'].get('PortfolioNPV', 0):,.0f}\n\n"
    
    md += "\n---\n\n## ⚠️ Risk Analysis\n\n"
    if 'RiskAnalysis' in canvas:
        md += f"**Overall Risk Level:** {canvas['RiskAnalysis'].get('OverallRiskLevel', 'N/A')}\n\n"
        md += f"**Key Risks:**\n"
        for risk in canvas['RiskAnalysis'].get('KeyRisks', []):
            md += f"- {risk}\n"
    
    return md


def export_html_to_png(html_content: str, output_path: str) -> bool:
    """
    Convert HTML to PNG using html2image
    Requires: pip install html2image
    """
    try:
        from html2image import hti
        
        # Create instance
        hti_instance = hti.HTML(html_string=html_content)
        
        # Convert to PNG
        hti_instance.write_png(output_path)
        return True
    except ImportError:
        print("html2image not installed. Install with: pip install html2image")
        return False
    except Exception as e:
        print(f"Error converting HTML to PNG: {e}")
        return False


def export_canvas_formats(canvas: Dict[str, Any], html_content: str, base_filename: str = "ai_roi_canvas") -> Dict[str, Any]:
    """
    Export canvas in multiple formats
    Returns dictionary with file contents for download
    """
    
    results = {}
    
    # JSON
    results['json'] = {
        'content': export_to_json(canvas),
        'filename': f"{base_filename}.json",
        'mime': 'application/json'
    }
    
    # Markdown
    results['markdown'] = {
        'content': export_to_markdown(canvas),
        'filename': f"{base_filename}.md",
        'mime': 'text/markdown'
    }
    
    # HTML
    results['html'] = {
        'content': html_content,
        'filename': f"{base_filename}.html",
        'mime': 'text/html'
    }
    
    return results
