"""Section 194BA Net Winnings 30% TDS Calculator for Indian Online Rummy."""


def calculate_section_194ba_tds(
    total_withdrawals: float,
    total_deposits: float,
    opening_balance: float = 0.0,
    closing_balance: float = 0.0,
    tds_already_deducted: float = 0.0,
) -> dict[str, float]:
    """Calculate Net Winnings and 30% TDS liability under Section 194BA."""
    net_winnings = (
        max(0.0, total_withdrawals) + max(0.0, closing_balance)
        - max(0.0, total_deposits) - max(0.0, opening_balance)
    )
    taxable_winnings = max(0.0, net_winnings)
    total_tds_liability = round(taxable_winnings * 0.30, 2)
    tds_due_now = round(max(0.0, total_tds_liability - max(0.0, tds_already_deducted)), 2)

    return {
        "net_winnings": round(net_winnings, 2),
        "taxable_winnings": round(taxable_winnings, 2),
        "total_tds_liability": total_tds_liability,
        "tds_due_now": tds_due_now,
    }


if __name__ == "__main__":
    sample = calculate_section_194ba_tds(
        total_withdrawals=15000,
        total_deposits=5000,
        opening_balance=0,
        closing_balance=2000,
    )
    print("Sample Section 194BA Calculation:", sample)
