"""
Visual Canvas Generator - Creates HTML/CSS representation of the AI ROI & Roadmap Canvas
matching the professional layout format.
"""

from typing import Dict, Any


def generate_visual_canvas_html(canvas: Dict[str, Any]) -> str:
    """
    Generate a beautiful HTML/CSS visual representation of the canvas
    that matches the professional layout in the reference image.
    """
    
    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{canvas['Header']['CanvasTitle']}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: #f5f5f5;
            padding: 20px;
        }}
        
        .canvas-container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border: 3px solid #333;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}
        
        .canvas-header {{
            background: white;
            padding: 20px 30px;
            border-bottom: 2px solid #333;
            display: grid;
            grid-template-columns: 2fr 1fr 1fr 1fr 1fr;
            gap: 15px;
            align-items: center;
        }}
        
        .canvas-title {{
            font-size: 28px;
            font-weight: bold;
            color: #333;
        }}
        
        .header-field {{
            display: flex;
            flex-direction: column;
        }}
        
        .header-label {{
            font-size: 11px;
            color: #666;
            font-weight: 600;
            margin-bottom: 3px;
        }}
        
        .header-value {{
            font-size: 13px;
            color: #333;
            padding: 5px;
            border-bottom: 1px solid #ddd;
        }}
        
        .objectives-section {{
            background: #f9f9f9;
            padding: 20px 30px;
            border-bottom: 2px solid #333;
            position: relative;
        }}
        
        .objectives-icon {{
            position: absolute;
            top: 20px;
            right: 30px;
            width: 40px;
            height: 40px;
            background: #fff;
            border: 2px solid #333;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
        }}
        
        .section-title {{
            font-size: 18px;
            font-weight: bold;
            color: #333;
            margin-bottom: 10px;
        }}
        
        .section-subtitle {{
            font-size: 12px;
            font-style: italic;
            color: #666;
            line-height: 1.6;
            margin-bottom: 15px;
        }}
        
        .objectives-content {{
            font-size: 14px;
            color: #333;
            line-height: 1.8;
        }}
        
        .main-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr 2fr;
            border-bottom: 2px solid #333;
        }}
        
        .grid-cell {{
            padding: 20px;
            border-right: 2px solid #333;
            position: relative;
        }}
        
        .grid-cell:last-child {{
            border-right: none;
        }}
        
        .cell-icon {{
            position: absolute;
            top: 20px;
            right: 20px;
            width: 35px;
            height: 35px;
            background: #fff;
            border: 2px solid #333;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
        }}
        
        .cell-content {{
            font-size: 13px;
            color: #333;
            line-height: 1.6;
        }}
        
        .cell-content ul {{
            list-style: none;
            padding-left: 0;
        }}
        
        .cell-content li {{
            padding: 4px 0;
            padding-left: 15px;
            position: relative;
        }}
        
        .cell-content li:before {{
            content: "▸";
            position: absolute;
            left: 0;
            color: #666;
        }}
        
        .bottom-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            border-bottom: 2px solid #333;
        }}
        
        .risks-caps-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
        }}
        
        .full-width-section {{
            padding: 20px 30px;
            border-bottom: 2px solid #333;
        }}
        
        .costs-benefits-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
        }}
        
        .roi-section {{
            padding: 20px 30px;
            background: #f9f9f9;
            border-bottom: 2px solid #333;
        }}
        
        .roi-content {{
            display: grid;
            grid-template-columns: 1fr 1fr 2fr;
            gap: 20px;
            margin-top: 10px;
        }}
        
        .roi-metric {{
            background: white;
            padding: 15px;
            border: 2px solid #333;
            border-radius: 8px;
            text-align: center;
        }}
        
        .roi-label {{
            font-size: 11px;
            color: #666;
            font-weight: 600;
            margin-bottom: 5px;
        }}
        
        .roi-value {{
            font-size: 24px;
            font-weight: bold;
            color: #2563eb;
        }}
        
        .roi-note {{
            background: white;
            padding: 15px;
            border: 2px solid #333;
            border-radius: 8px;
            font-size: 12px;
            color: #666;
            display: flex;
            align-items: center;
        }}
        
        .footer {{
            padding: 15px 30px;
            text-align: center;
            font-size: 11px;
            color: #666;
            font-style: italic;
        }}
        
        .timeline-table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }}
        
        .timeline-table th {{
            background: #f9f9f9;
            padding: 10px;
            text-align: left;
            font-size: 11px;
            font-weight: 600;
            border: 1px solid #ddd;
        }}
        
        .timeline-table td {{
            padding: 10px;
            font-size: 12px;
            border: 1px solid #ddd;
        }}
        
        .timeline-table tr:nth-child(even) {{
            background: #fafafa;
        }}
        
        @media print {{
            body {{
                padding: 0;
            }}
            .canvas-container {{
                box-shadow: none;
            }}
        }}
    </style>
</head>
<body>
    <div class="canvas-container">
        <!-- Header -->
        <div class="canvas-header">
            <div class="canvas-title">{canvas['Header']['CanvasTitle']}</div>
            <div class="header-field">
                <div class="header-label">Organization:</div>
                <div class="header-value">{canvas['Header'].get('Organization', 'N/A')}</div>
            </div>
            <div class="header-field">
                <div class="header-label">Team/Department:</div>
                <div class="header-value">{canvas['Header'].get('Team', 'N/A')}</div>
            </div>
            <div class="header-field">
                <div class="header-label">Designed by:</div>
                <div class="header-value">{canvas['Header']['DesignedBy']}</div>
            </div>
            <div class="header-field">
                <div class="header-label">Designed For:</div>
                <div class="header-value">{canvas['Header']['DesignedFor']}</div>
            </div>
            <div class="header-field">
                <div class="header-label">Date:</div>
                <div class="header-value">{canvas['Header']['Date']}</div>
            </div>
        </div>
        
        <!-- Objectives -->
        <div class="objectives-section">
            <div class="objectives-icon">🎯</div>
            <div class="section-title">Objectives</div>
            <div class="section-subtitle">
                Clearly define the strategic goals of the AI initiative, aligning with broader business objectives. 
                Specify the purpose of the portfolio, distinguishing between initiatives aimed at staying in business, 
                generating ROI, and creating future options
            </div>
            <div class="objectives-content">
                <strong>Primary Goal:</strong> {canvas['Objectives']['PrimaryGoal']}<br>
                <strong>Strategic Focus:</strong> {canvas['Objectives']['StrategicFocus']}
            </div>
        </div>
        
        <!-- Main Grid: Inputs, Impacts, Timeline -->
        <div class="main-grid">
            <!-- Inputs -->
            <div class="grid-cell">
                <div class="cell-icon">👥</div>
                <div class="section-title">Inputs</div>
                <div class="section-subtitle">
                    List the necessary resources, categorized into hard costs (e.g., hardware, software, data) 
                    and soft costs (e.g., training, change management), ensuring that all financial, human, 
                    and technological inputs are accounted for
                </div>
                <div class="cell-content">
                    <strong>Resources:</strong>
                    <ul>
                        {''.join(f'<li>{r}</li>' for r in canvas['Inputs']['Resources'])}
                    </ul>
                    <strong>Personnel:</strong>
                    <ul>
                        {''.join(f'<li>{p}</li>' for p in canvas['Inputs']['Personnel'])}
                    </ul>
                    <strong>External Support:</strong>
                    <ul>
                        {''.join(f'<li>{e}</li>' for e in canvas['Inputs']['ExternalSupport'])}
                    </ul>
                </div>
            </div>
            
            <!-- Impacts -->
            <div class="grid-cell">
                <div class="cell-icon">✓</div>
                <div class="section-title">Impacts</div>
                <div class="section-subtitle">
                    Detail the anticipated impacts of the AI initiative from individual, organizational, 
                    and societal perspectives. Include metrics for both hard benefits (e.g., time savings) 
                    and soft benefits (e.g., improved decision-making)
                </div>
                <div class="cell-content">
                    <strong>Hard Benefits:</strong>
                    <ul>
                        {''.join(f'<li>{b}</li>' for b in canvas['Impacts']['HardBenefits'])}
                    </ul>
                    <strong>Soft Benefits:</strong>
                    <ul>
                        {'' if not canvas['Impacts'].get('SoftBenefitsWithContext') else ''.join(f'<li><strong>{sb.get("benefit", sb.get("name", ""))}</strong><br/><small style="color: #666; font-size: 12px; font-style: italic;">{sb.get("context", "")}</small></li>' for sb in canvas['Impacts'].get('SoftBenefitsWithContext', []))}
                        {''.join(f'<li>{b}</li>' for b in canvas['Impacts']['SoftBenefits'] if not any(c.get("benefit") == b or c.get("name") == b for c in canvas['Impacts'].get('SoftBenefitsWithContext', [])))}
                    </ul>
                </div>
            </div>
            
            <!-- Timeline & Milestones -->
            <div class="grid-cell">
                <div class="cell-icon">💬</div>
                <div class="section-title">Timeline & Milestones</div>
                <div class="section-subtitle">
                    Outline the project phases, key deliverables, and deadlines, incorporating checkpoints 
                    for evaluating the realization of hard and soft benefits. Ensure alignment with prioritized 
                    initiatives and strategic objectives
                </div>
                <div class="cell-content">
                    <table class="timeline-table">
                        <thead>
                            <tr>
                                <th>AI Initiative</th>
                                <th>Duration</th>
                                <th>Start Date</th>
                                <th>End Date</th>
                                <th>ROI</th>
                                <th>Expected Benefit</th>
                                <th>Effort</th>
                            </tr>
                        </thead>
                        <tbody>
                            {''.join(f'''
                            <tr>
                                <td><strong>{t['AIInitiative']}</strong></td>
                                <td>{t.get('DurationMonths', 'N/A')} months</td>
                                <td>{t['StartDate']}</td>
                                <td>{t['EndDate']}</td>
                                <td>{t.get('ROI', 'N/A')}</td>
                                <td>{t.get('ExpectedBenefit', 'N/A')}</td>
                                <td>{t.get('Effort', 'N/A')}/10</td>
                            </tr>
                            ''' for t in canvas['Timeline'])}
                        </tbody>
                    </table>
                    
                    <!-- Detailed Phase Breakdown for Each Initiative -->
                    <div style="margin-top: 30px; border-top: 2px solid #333; padding-top: 20px;">
                        <h4 style="font-size: 14px; font-weight: bold; margin-bottom: 20px;">📋 Detailed Phase Breakdown by Initiative</h4>
                        {''.join(f'''
                        <div style="margin-bottom: 25px; border: 1px solid #ddd; padding: 15px; border-radius: 5px;">
                            <h5 style="font-size: 13px; font-weight: bold; margin-bottom: 12px; color: #333;">{initiative}</h5>
                            <p style="font-size: 11px; color: #666; margin-bottom: 10px;"><strong>Timeline:</strong> {info['overall_start']} to {info['overall_end']} ({info['total_duration_months']} months)</p>
                            <table style="width: 100%; font-size: 11px; border-collapse: collapse;">
                                <thead>
                                    <tr style="background-color: #f5f5f5;">
                                        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Phase</th>
                                        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Duration</th>
                                        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Start - End</th>
                                        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Key Deliverables</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {''.join(f'''
                                    <tr>
                                        <td style="border: 1px solid #ddd; padding: 8px;"><strong>{phase['phase_name']}</strong></td>
                                        <td style="border: 1px solid #ddd; padding: 8px;">{phase['duration_months']} months</td>
                                        <td style="border: 1px solid #ddd; padding: 8px;">{phase['start_date']}<br/>{phase['end_date']}</td>
                                        <td style="border: 1px solid #ddd; padding: 8px;">
                                            <ul style="margin: 0; padding-left: 20px; font-size: 10px;">
                                                {''.join(f'<li>{deliverable}</li>' for deliverable in phase['deliverables'])}
                                            </ul>
                                        </td>
                                    </tr>
                                    ''' for phase in info['phases'])}
                                </tbody>
                            </table>
                        </div>
                        ''' for initiative, info in canvas.get('DetailedTimeline', {}).items())}
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Risks & Capabilities Grid -->
        <div class="risks-caps-grid">
            <!-- Risks -->
            <div class="grid-cell">
                <div class="cell-icon">⚠️</div>
                <div class="section-title">Risks</div>
                <div class="section-subtitle">
                    Identify potential risks associated with the AI project, categorizing them into consumer, 
                    company, societal, and environmental risks. Include strategies for mitigating these risks 
                    and account for both the direct and indirect costs of risk management
                </div>
                <div class="cell-content">
                    <ul>
                        {''.join(f'<li>{r}</li>' for r in canvas['Risks'])}
                    </ul>
                </div>
            </div>
            
            <!-- Capabilities -->
            <div class="grid-cell">
                <div class="cell-icon">👤</div>
                <div class="section-title">Capabilities</div>
                <div class="section-subtitle">
                    Specify the skills, expertise, and technological capabilities required to successfully 
                    develop, deploy, and manage the AI solution. Ensure that the capabilities align with 
                    the strategic objectives and are sufficient to deliver both hard and soft benefits
                </div>
                <div class="cell-content">
                    <strong>Skills Needed:</strong>
                    <ul>
                        {''.join(f'<li>{s}</li>' for s in canvas['Capabilities']['SkillsNeeded'])}
                    </ul>
                    <strong>Technology:</strong>
                    <ul>
                        {''.join(f'<li>{t}</li>' for t in canvas['Capabilities']['Technology'])}
                    </ul>
                </div>
            </div>
        </div>
        
        <!-- Costs & Benefits Grid -->
        <div class="costs-benefits-grid">
            <!-- Costs -->
            <div class="grid-cell">
                <div class="cell-icon">💳</div>
                <div class="section-title">Costs</div>
                <div class="section-subtitle">
                    Provide a detailed breakdown of the financial expenditure required for the AI project, 
                    including both hard costs (e.g., infrastructure, licensing) and soft costs (e.g., employee training, 
                    compliance). Allocate these costs across different phases of the project and categorize them 
                    according to their relevance to stay-in-business, ROI-generating, or option-creating initiatives
                </div>
                <div class="cell-content">
                    <ul>
                        <li><strong>Near Term:</strong> {canvas['Costs']['NearTerm']}</li>
                        <li><strong>Long Term:</strong> {canvas['Costs']['LongTerm']}</li>
                        <li><strong>Annual Maintenance:</strong> {canvas['Costs']['AnnualMaintenance']}</li>
                    </ul>
                    <div style="margin-top: 12px; padding-top: 12px; border-top: 1px solid #ddd; font-size: 12px;">
                        <strong>Cost Breakdown by Initiative:</strong>
                        <ul style="margin-top: 8px;">
                            {chr(10).join(f'''
                            <li style="margin-bottom: 10px;">
                                <strong>{detail['category']}</strong><br/>
                                Initial: {detail['initial']} {chr(10)}
                                Annual: {detail['annual']} {chr(10)}
                                <em style="color: #666; font-size: 11px;">Details: {detail['breakdown']}</em>
                            </li>
                            ''' for detail in canvas['Costs'].get('CostDetails', []))}
                        </ul>
                    </div>
                </div>
            </div>
            
            <!-- Benefits -->
            <div class="grid-cell">
                <div class="cell-icon">📊</div>
                <div class="section-title">Benefits</div>
                <div class="section-subtitle">
                    Quantify the expected returns from the AI project, detailing both hard benefits (e.g., cost savings, 
                    revenue growth). These align with the organization's strategic objectives and provide a clear value proposition
                </div>
                <div class="cell-content">
                    <ul>
                        <li><strong>Near Term:</strong> {canvas['Benefits']['NearTerm']}</li>
                        <li><strong>Long Term:</strong> {canvas['Benefits']['LongTerm']}</li>
                    </ul>
                    <div style="margin-top: 12px; padding-top: 12px; border-top: 1px solid #ddd; font-size: 12px;">
                        <strong>Benefits Breakdown by Initiative:</strong>
                        <ul style="margin-top: 8px;">
                            {chr(10).join(f'''
                            <li style="margin-bottom: 10px;">
                                <strong>{detail['initiative']}</strong><br/>
                                Year 1: {detail['year1_benefit']} {chr(10)}
                                Ongoing: {detail['ongoing_benefit']}/year {chr(10)}
                                <em style="color: #666; font-size: 11px;">Breakdown: {detail['year1_breakdown']}</em>
                            </li>
                            ''' for detail in canvas['Benefits'].get('BenefitDetails', []))}
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Portfolio ROI -->
        <div class="roi-section">
            <div class="section-title">Portfolio Return on Investment</div>
            <div class="section-subtitle">
                Evaluate the overall ROI for the AI portfolio, identifying the proportion of initiatives aimed at 
                staying in business, generating ROI, and creating future options. Use a value-effort matrix to prioritize 
                initiatives with the highest impact and feasibility, ensuring a balanced portfolio approach
            </div>
            <div class="roi-content">
                <div class="roi-metric">
                    <div class="roi-label">Near-Term ROI</div>
                    <div class="roi-value">{canvas['PortfolioROI']['NearTermROIPercent']}</div>
                </div>
                <div class="roi-metric">
                    <div class="roi-label">Long-Term ROI</div>
                    <div class="roi-value">{canvas['PortfolioROI']['LongTermROIPercent']}</div>
                </div>
                <div class="roi-note">
                    {canvas['PortfolioROI']['PortfolioNote']}
                </div>
            </div>
        </div>
        
        <!-- Footer -->
        <div class="footer">
            {canvas['Footer']['CreditLine']}
        </div>
    </div>
</body>
</html>
"""
    
    return html
