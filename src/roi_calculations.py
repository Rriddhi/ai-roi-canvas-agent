"""
ROI calculation functions following the exact specification formulas.
"""

from typing import Dict, Any


def calculate_roi_metrics(use_case: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calculate all ROI metrics for a use case following exact specification formulas.
    
    Returns updated use case with additional fields:
    - near_term_roi_percent
    - long_term_roi_percent
    - npv_10_percent
    - payback_period_years
    - risk_adjusted_value
    """
    # Extract values
    initial_cost = use_case["costs"]["initial_cost"]
    near_term_annual_cost = use_case["costs"]["near_term_annual_cost"]
    long_term_annual_cost = use_case["costs"]["long_term_annual_cost"]
    
    near_term_annual_benefit = use_case["expected_benefits"]["near_term_annual_benefit"]
    long_term_annual_benefit = use_case["expected_benefits"]["long_term_annual_benefit"]
    
    probability = use_case["risk"]["probability_0_to_1"]
    impact = use_case["risk"]["impact_0_to_1"]
    
    # CASH FLOWS
    cf0 = -initial_cost
    cf1 = near_term_annual_benefit - near_term_annual_cost
    cf2 = long_term_annual_benefit - long_term_annual_cost
    cf3 = long_term_annual_benefit - long_term_annual_cost
    
    # 1. NEAR-TERM ROI %
    near_term_cost = initial_cost + near_term_annual_cost
    near_term_benefit = near_term_annual_benefit
    
    if near_term_cost > 0:
        near_term_roi_percent = ((near_term_benefit - near_term_cost) / near_term_cost) * 100
    else:
        near_term_roi_percent = 0.0
    
    # 2. LONG-TERM ROI % (3-year)
    total_cost_3y = initial_cost + near_term_annual_cost + 2 * long_term_annual_cost
    total_benefit_3y = near_term_annual_benefit + 2 * long_term_annual_benefit
    
    if total_cost_3y > 0:
        long_term_roi_percent = ((total_benefit_3y - total_cost_3y) / total_cost_3y) * 100
    else:
        long_term_roi_percent = 0.0
    
    # 3. NPV (10% discount rate)
    npv = cf0 + cf1 / 1.1 + cf2 / (1.1 ** 2) + cf3 / (1.1 ** 3)
    
    # 4. PAYBACK PERIOD
    c0 = cf0
    c1 = c0 + cf1
    c2 = c1 + cf2
    c3 = c2 + cf3
    
    if c0 >= 0:
        payback_period = "0 years"
    elif c1 >= 0:
        payback_period = "1 year"
    elif c2 >= 0:
        payback_period = "2 years"
    elif c3 >= 0:
        payback_period = "3 years"
    else:
        payback_period = "> 3 years"
    
    # 5. RISK-ADJUSTED VALUE
    risk_score = probability * impact
    risk_adjusted_value = npv * (1 - risk_score)
    
    # Add computed fields to use case
    use_case["near_term_roi_percent"] = round(near_term_roi_percent, 2)
    use_case["long_term_roi_percent"] = round(long_term_roi_percent, 2)
    use_case["npv_10_percent"] = round(npv, 2)
    use_case["payback_period_years"] = payback_period
    use_case["risk_adjusted_value"] = round(risk_adjusted_value, 2)
    
    return use_case


def compute_all_roi(use_cases: list) -> list:
    """Compute ROI metrics for all use cases."""
    return [calculate_roi_metrics(uc.copy()) for uc in use_cases]
