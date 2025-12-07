"""
Canvas and roadmap generation following the exact specification format.
"""

from typing import Dict, Any, List
from datetime import datetime, timedelta


def generate_detailed_timeline(use_cases: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Generate detailed timeline with phases for each initiative
    Includes: Discovery (3mo), Design (3mo), Development (3-12mo), Deployment (1-3mo), Operations (ongoing)
    """
    detailed_timeline = {}
    current_date = datetime.now()
    start_offset = 0
    
    for uc in use_cases:
        effort = uc.get("effort_score_1_to_10", 5)
        title = uc["title"]
        
        # Determine total duration based on effort
        if effort <= 3:
            total_months = 6  # Quick win: 3mo discovery + 3mo deploy
            dev_months = 1
        elif effort <= 6:
            total_months = 12  # 1-year: 3mo discovery + 6mo dev + 3mo deploy
            dev_months = 6
        else:
            total_months = 36  # 3-year: 3mo discovery + 12-24mo dev + 3mo deploy
            dev_months = 24
        
        phases = {
            "Discovery & Planning": {
                "duration": 3,
                "description": "Requirements gathering, stakeholder alignment, resource planning",
                "deliverables": ["Business requirements", "Technical architecture", "Team structure"]
            },
            "Design & Preparation": {
                "duration": 3,
                "description": "Solution design, vendor selection, infrastructure setup",
                "deliverables": ["System design", "Implementation plan", "Infrastructure provisioned"]
            },
            "Development & Integration": {
                "duration": dev_months,
                "description": "Model development, system integration, quality assurance",
                "deliverables": ["Trained models", "API integrations", "Test reports"]
            },
            "Deployment & Rollout": {
                "duration": 3,
                "description": "Pilot testing, user training, production deployment",
                "deliverables": ["Production deployment", "User documentation", "Training completion"]
            },
            "Operations & Optimization": {
                "duration": 3,
                "description": "Monitoring, performance tuning, continuous improvement",
                "deliverables": ["Monitoring dashboards", "Performance metrics", "Optimization roadmap"]
            }
        }
        
        timeline_phases = []
        phase_start_offset = start_offset
        
        for phase_name, phase_info in phases.items():
            phase_duration = phase_info["duration"]
            phase_start = current_date + timedelta(days=phase_start_offset * 30)
            phase_end = phase_start + timedelta(days=phase_duration * 30)
            
            timeline_phases.append({
                "phase_name": phase_name,
                "start_date": phase_start.strftime("%Y-%m-%d"),
                "end_date": phase_end.strftime("%Y-%m-%d"),
                "duration_months": phase_duration,
                "description": phase_info["description"],
                "deliverables": phase_info["deliverables"]
            })
            
            phase_start_offset += phase_duration
        
        detailed_timeline[title] = {
            "effort": effort,
            "total_duration_months": total_months,
            "overall_start": (current_date + timedelta(days=start_offset * 30)).strftime("%Y-%m-%d"),
            "overall_end": (current_date + timedelta(days=phase_start_offset * 30)).strftime("%Y-%m-%d"),
            "phases": timeline_phases,
            "expected_benefit": f"${uc['expected_benefits'].get('near_term_annual_benefit', 0):,.0f}/year",
            "roi": f"{uc.get('near_term_roi_percent', 'N/A')}%"
        }
        
        start_offset = phase_start_offset + 1  # Add buffer between initiatives
    
    return detailed_timeline


def assign_roadmap_timeline(use_cases: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """
    Assign use cases to timeline buckets:
    - Q1: Quick Wins
    - 1-Year: Effort <= 6
    - 3-Year: Effort > 6
    
    Respect dependencies: If B depends on A, A must be in same or earlier bucket.
    """
    q1_cases = []
    one_year_cases = []
    three_year_cases = []
    
    for uc in use_cases:
        category = uc.get("category", "")
        effort = uc["effort_score_1_to_10"]
        
        if category == "Quick Win":
            q1_cases.append(uc)
        elif effort <= 6:
            one_year_cases.append(uc)
        else:
            three_year_cases.append(uc)
    
    return {
        "Q1": q1_cases,
        "1-Year": one_year_cases,
        "3-Year": three_year_cases
    }


def build_canvas(
    use_cases: List[Dict[str, Any]],
    portfolio: Dict[str, Any],
    org_name: str = "",
    org_team: str = "",
    designed_by: str = "",
    designed_for: str = "",
    primary_goal: str = "",
    strategic_focus: str = ""
) -> Dict[str, Any]:
    """
    Build the complete AI ROI & Roadmap Canvas in exact specification format.
    """
    if not portfolio:
        return None
    
    selected = portfolio.get("selected_use_cases", [])
    
    # Generate detailed timeline with phases for each initiative
    detailed_timeline = generate_detailed_timeline(selected)
    
    # Also create simple timeline items for the main canvas view
    timeline_items = []
    for initiative, timeline_info in detailed_timeline.items():
        timeline_items.append({
            "AIInitiative": initiative,
            "StartDate": timeline_info["overall_start"],
            "EndDate": timeline_info["overall_end"],
            "DurationMonths": timeline_info["total_duration_months"],
            "Milestone": f"{timeline_info['total_duration_months']}-month delivery",
            "ROI": timeline_info["roi"],
            "ExpectedBenefit": timeline_info["expected_benefit"],
            "Effort": timeline_info["effort"],
            "Phases": timeline_info["phases"]
            })
    
    # Aggregate benefits
    total_near_term_benefit = sum(
        uc["expected_benefits"]["near_term_annual_benefit"] for uc in selected
    )
    total_long_term_benefit = sum(
        uc["expected_benefits"]["long_term_annual_benefit"] for uc in selected
    )
    
    all_soft_benefits = []
    all_soft_benefits_with_context = []
    for uc in selected:
        soft_benefits_data = uc["expected_benefits"].get("soft_benefits", [])
        # Handle both old format (list of strings) and new format (list of dicts with context)
        for item in soft_benefits_data:
            if isinstance(item, dict):
                all_soft_benefits_with_context.append(item)
                all_soft_benefits.append(item.get("benefit", item.get("name", "")))
            else:
                all_soft_benefits.append(item)
    
    # Aggregate costs and benefits
    total_initial_cost = sum(uc["costs"]["initial_cost"] for uc in selected)
    total_near_term_cost = sum(uc["costs"]["near_term_annual_cost"] for uc in selected)
    total_long_term_cost = sum(uc["costs"]["long_term_annual_cost"] for uc in selected)
    total_near_term_benefit = sum(uc["expected_benefits"].get("near_term_annual_benefit", 0) for uc in selected)
    total_long_term_benefit = sum(uc["expected_benefits"].get("long_term_annual_benefit", 0) for uc in selected)
    
    # Calculate aggregated ROI properly
    total_near_term_cost_with_initial = total_initial_cost + total_near_term_cost
    if total_near_term_cost_with_initial > 0:
        portfolio_near_term_roi = ((total_near_term_benefit - total_near_term_cost_with_initial) / total_near_term_cost_with_initial) * 100
    else:
        portfolio_near_term_roi = 0
    
    # Long-term ROI (3 year)
    total_long_term_cost_3y = total_initial_cost + total_near_term_cost + 2 * total_long_term_cost
    total_long_term_benefit_3y = total_near_term_benefit + 2 * total_long_term_benefit
    if total_long_term_cost_3y > 0:
        portfolio_long_term_roi = ((total_long_term_benefit_3y - total_long_term_cost_3y) / total_long_term_cost_3y) * 100
    else:
        portfolio_long_term_roi = 0
    
    # Collect risks
    all_risks = []
    for uc in selected:
        all_risks.extend(uc["risk"]["risks_list"])
    
    # Collect KPIs as hard benefits
    all_kpis = []
    for uc in selected:
        all_kpis.extend(uc.get("kpis", []))
    
    # Build canvas
    canvas = {
        "Header": {
            "CanvasTitle": "AI ROI & Roadmap Canvas",
            "Organization": org_name,
            "Team": org_team,
            "Name": org_name,
            "DesignedBy": designed_by,
            "DesignedFor": designed_for,
            "Date": datetime.now().strftime("%Y-%m-%d"),
            "Version": "v1.0"
        },
        "Objectives": {
            "PrimaryGoal": primary_goal,
            "StrategicFocus": strategic_focus
        },
        "Inputs": {
            "Resources": [f"${total_initial_cost:,.0f} initial investment"],
            "Personnel": ["AI/ML engineers", "Data scientists", "Project managers"],
            "ExternalSupport": ["Technology vendors", "Consulting partners"]
        },
        "Impacts": {
            "HardBenefits": list(set(all_kpis))[:10],
            "SoftBenefits": list(set(all_soft_benefits))[:10],
            "SoftBenefitsWithContext": all_soft_benefits_with_context[:10]
        },
        "Timeline": timeline_items,
        "DetailedTimeline": detailed_timeline,
        "Risks": list(set(all_risks))[:15],
        "Capabilities": {
            "SkillsNeeded": ["Machine Learning", "Data Engineering", "MLOps", "Change Management"],
            "Technology": ["Cloud infrastructure", "ML frameworks", "Data platforms"]
        },
        "Costs": {
            "NearTerm": f"${total_initial_cost + total_near_term_cost:,.0f}",
            "NearTermBreakdown": [f"Initial: ${total_initial_cost:,.0f}", f"Annual: ${total_near_term_cost:,.0f}"],
            "CostDetails": [
                {
                    "category": uc["title"],
                    "initial": f"${uc['costs'].get('initial_cost', 0):,.0f}",
                    "annual": f"${uc['costs'].get('near_term_annual_cost', 0):,.0f}",
                    "breakdown": uc['costs'].get('initial_cost_breakdown', 'See use case details'),
                    "annual_breakdown": uc['costs'].get('near_term_annual_cost_breakdown', 'See use case details')
                }
                for uc in selected
            ],
            "LongTerm": f"${total_long_term_cost:,.0f} annually",
            "AnnualMaintenance": f"${total_long_term_cost:,.0f}"
        },
        "Benefits": {
            "NearTerm": f"${total_near_term_benefit:,.0f} annually",
            "NearTermBreakdown": [f"Year 1: ${total_near_term_benefit:,.0f}", f"Years 2-3: ${total_long_term_benefit:,.0f}/year"],
            "BenefitDetails": [
                {
                    "initiative": uc["title"],
                    "year1_benefit": f"${uc['expected_benefits'].get('near_term_annual_benefit', 0):,.0f}",
                    "year1_breakdown": uc['expected_benefits'].get('near_term_benefit_breakdown', 'See use case details'),
                    "ongoing_benefit": f"${uc['expected_benefits'].get('long_term_annual_benefit', 0):,.0f}",
                    "soft_benefits": [sb.get('benefit', sb) if isinstance(sb, dict) else sb for sb in uc['expected_benefits'].get('soft_benefits', [])]
                }
                for uc in selected
            ],
            "LongTerm": f"${total_long_term_benefit:,.0f} annually",
            "SoftBenefits": list(set(all_soft_benefits))[:10]
        },
        "PortfolioROI": {
            "NearTermROIPercent": f"{portfolio_near_term_roi:.1f}%",
            "LongTermROIPercent": f"{portfolio_long_term_roi:.1f}%",
            "PortfolioNote": f"Portfolio of {len(selected)} AI initiatives selected from {len(use_cases)} candidates"
        },
        "Footer": {
            "CreditLine": "AI ROI & Roadmap Canvas generated by Smridhi's GPT Agent."
        }
    }
    
    return canvas


def canvas_to_markdown(canvas: Dict[str, Any]) -> str:
    """Convert canvas JSON to readable Markdown format."""
    md = f"""# {canvas['Header']['CanvasTitle']}

**Organization:** {canvas['Header']['Name']}  
**Designed By:** {canvas['Header']['DesignedBy']}  
**Designed For:** {canvas['Header']['DesignedFor']}  
**Date:** {canvas['Header']['Date']}  
**Version:** {canvas['Header']['Version']}

---

## Objectives

**Primary Goal:** {canvas['Objectives']['PrimaryGoal']}  
**Strategic Focus:** {canvas['Objectives']['StrategicFocus']}

---

## Inputs

### Resources
{chr(10).join(f"- {r}" for r in canvas['Inputs']['Resources'])}

### Personnel
{chr(10).join(f"- {p}" for p in canvas['Inputs']['Personnel'])}

### External Support
{chr(10).join(f"- {e}" for e in canvas['Inputs']['ExternalSupport'])}

---

## Impacts

### Hard Benefits
{chr(10).join(f"- {b}" for b in canvas['Impacts']['HardBenefits'])}

### Soft Benefits
{chr(10).join(f"- {b}" for b in canvas['Impacts']['SoftBenefits'])}

---

## Timeline

| AI Initiative | Start Date | End Date | Milestone |
|--------------|------------|----------|-----------|
{chr(10).join(f"| {t['AIInitiative']} | {t['StartDate']} | {t['EndDate']} | {t['Milestone']} |" for t in canvas['Timeline'])}

---

## Risks

{chr(10).join(f"- {r}" for r in canvas['Risks'])}

---

## Capabilities

### Skills Needed
{chr(10).join(f"- {s}" for s in canvas['Capabilities']['SkillsNeeded'])}

### Technology
{chr(10).join(f"- {t}" for t in canvas['Capabilities']['Technology'])}

---

## Costs

- **Near Term:** {canvas['Costs']['NearTerm']}
- **Long Term:** {canvas['Costs']['LongTerm']}
- **Annual Maintenance:** {canvas['Costs']['AnnualMaintenance']}

---

## Benefits

- **Near Term:** {canvas['Benefits']['NearTerm']}
- **Long Term:** {canvas['Benefits']['LongTerm']}

### Soft Benefits
{chr(10).join(f"- {b}" for b in canvas['Benefits']['SoftBenefits'])}

---

## Portfolio ROI

- **Near-Term ROI:** {canvas['PortfolioROI']['NearTermROIPercent']}
- **Long-Term ROI:** {canvas['PortfolioROI']['LongTermROIPercent']}
- **Note:** {canvas['PortfolioROI']['PortfolioNote']}

---

{canvas['Footer']['CreditLine']}
"""
    return md
