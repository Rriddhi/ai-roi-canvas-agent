"""
Portfolio selection logic following the exact specification rules.
"""

from typing import Dict, Any, List


def normalize_to_scale(values: List[float], max_scale: float = 10.0) -> List[float]:
    """Normalize values to 0-max_scale range."""
    if not values or max(values) == 0:
        return [0.0] * len(values)
    
    max_val = max(values)
    return [(v / max_val) * max_scale for v in values]


def categorize_use_case(impact_score: float, effort: int) -> str:
    """
    Categorize use case based on impact and effort.
    
    Rules:
    - Quick Wins: Impact >= 7 AND Effort <= 4
    - Big Bets: Impact >= 7 AND Effort >= 5
    - Fill-ins: Impact between 4 and 6
    - Low Priority: Impact < 4
    """
    if impact_score >= 7 and effort <= 4:
        return "Quick Win"
    elif impact_score >= 7 and effort >= 5:
        return "Big Bet"
    elif 4 <= impact_score < 7:
        return "Fill-in"
    else:
        return "Low Priority"


def select_portfolio(use_cases: List[Dict[str, Any]], effort_budget: int) -> Dict[str, Any]:
    """
    Select optimal portfolio within effort budget.
    
    Steps:
    1. Compute ImpactScore (normalized risk_adjusted_value to 0-10)
    2. Categorize each use case
    3. Sort by ImpactScore/Effort descending
    4. Select until budget reached
    5. Ensure at least 1 Quick Win and 1 Big Bet (if they exist)
    """
    # Step 1: Compute ImpactScore
    risk_adjusted_values = [uc.get("risk_adjusted_value", 0) for uc in use_cases]
    impact_scores = normalize_to_scale(risk_adjusted_values, 10.0)
    
    # Add impact scores and categories to use cases
    enriched_cases = []
    for i, uc in enumerate(use_cases):
        uc_copy = uc.copy()
        uc_copy["impact_score"] = round(impact_scores[i], 2)
        effort = uc.get("effort_score_1_to_10", 5)  # Default to 5 if missing
        uc_copy["category"] = categorize_use_case(
            impact_scores[i],
            effort
        )
        uc_copy["efficiency"] = (
            impact_scores[i] / effort
            if effort > 0 else 0
        )
        enriched_cases.append(uc_copy)
    
    # Step 2: Sort by efficiency (ImpactScore / Effort) descending
    sorted_cases = sorted(enriched_cases, key=lambda x: x["efficiency"], reverse=True)
    
    # Step 3: Select use cases within budget
    selected = []
    excluded = []
    total_effort = 0
    
    for uc in sorted_cases:
        if total_effort + uc["effort_score_1_to_10"] <= effort_budget:
            selected.append(uc)
            total_effort += uc["effort_score_1_to_10"]
        else:
            excluded.append(uc)
    
    # Step 4: Ensure constraints (at least 1 Quick Win and 1 Big Bet if they exist)
    quick_wins = [uc for uc in enriched_cases if uc["category"] == "Quick Win"]
    big_bets = [uc for uc in enriched_cases if uc["category"] == "Big Bet"]
    
    selected_ids = {uc["id"] for uc in selected}
    
    # Add best Quick Win if none selected
    if quick_wins and not any(uc["category"] == "Quick Win" for uc in selected):
        best_qw = max(quick_wins, key=lambda x: x["efficiency"])
        if best_qw["id"] not in selected_ids:
            selected.append(best_qw)
            total_effort += best_qw["effort_score_1_to_10"]
    
    # Add best Big Bet if none selected
    if big_bets and not any(uc["category"] == "Big Bet" for uc in selected):
        best_bb = max(big_bets, key=lambda x: x["efficiency"])
        if best_bb["id"] not in selected_ids:
            selected.append(best_bb)
            total_effort += best_bb["effort_score_1_to_10"]
    
    # Recalculate excluded
    selected_ids = {uc["id"] for uc in selected}
    excluded = [uc for uc in enriched_cases if uc["id"] not in selected_ids]
    
    # Generate rationale
    category_counts = {}
    for uc in selected:
        cat = uc["category"]
        category_counts[cat] = category_counts.get(cat, 0) + 1
    
    rationale = (
        f"Selected {len(selected)} use cases with total effort {total_effort}/{effort_budget}. "
        f"Portfolio includes: {', '.join(f'{count} {cat}' for cat, count in category_counts.items())}. "
        f"Selection prioritized high-impact, low-effort initiatives."
    )
    
    return {
        "selected_use_cases": selected,
        "excluded_use_cases": excluded,
        "selection_rationale": rationale,
        "total_effort": total_effort,
        "effort_budget": effort_budget
    }
