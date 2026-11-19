# Indian Rummy Section 194BA TDS & 13-Card Points Toolkit

Open-source reference implementations for Indian online skill-gaming tax and scoring rules:

1. **Section 194BA 30% Net Winnings TDS Calculator** (Income Tax Act, India — effective April 1, 2023)
2. **13-Card Indian Rummy Deadwood & Drop Points Calculator** (Points Rummy, 101 Pool, 201 Pool)

> **Live Interactive Web Calculators:**
> - [Rummy 30% TDS Calculator (Section 194BA)](https://www.rummy-game.com/tools/rummy-tds-calculator/) on Rummy-Game.com
> - [13-Card Rummy Points & Drop Calculator](https://www.rummy-game.com/tools/rummy-points-calculator/) on Rummy-Game.com

---

## 1. Section 194BA Net Winnings Formula

Under **Section 194BA** of the Indian Income Tax Act, online gaming operators deduct **30% TDS** on **Net Winnings** at the time of withdrawal (and on any remaining year-end balance as of March 31):

```text
Net Winnings = (Total Withdrawals + Closing Balance) - (Total Deposits + Opening Balance)
TDS (30%)    = max(0, Net Winnings) * 0.30
Net Payout   = Withdrawal Amount - TDS
```

### Python Quickstart (`tds_calculator.py`)

```python
from tds_calculator import calculate_section_194ba_tds

result = calculate_section_194ba_tds(
    total_withdrawals=15000,
    total_deposits=5000,
    opening_balance=0,
    closing_balance=2000,
    tds_already_deducted=0,
)
print(result)
# {'net_winnings': 12000.0, 'total_tds_liability': 3600.0, 'tds_due_now': 3600.0}
```

### JavaScript Quickstart (`tds-calculator.js`)

```js
import { calculateSection194baTds } from './tds-calculator.js';

const res = calculateSection194baTds({
  totalWithdrawals: 15000,
  totalDeposits: 5000,
});
console.log(res);
```

---

## 2. 13-Card Indian Rummy Scoring (`points_calculator.py`)

- **Face Cards (`A, K, Q, J`)**: `10 points` each
- **Number Cards (`2–10`)**: Face value (`2–10 points`)
- **Printed & Wild Jokers**: `0 points`
- **Maximum Hand Penalty (Full Count)**: Capped at `80 points`
- **Drops**:
  - Points / 101 Pool: First Drop = `20 pts`, Middle Drop = `40 pts`
  - 201 Pool: First Drop = `25 pts`, Middle Drop = `50 pts`

---

## Reference Guides

- [Rummy UPI Withdrawal, KYC & 30% TDS Rules Explained](https://www.rummy-game.com/guides/rummy-upi-withdrawal-kyc-tds-rules/)
- [How to Play 13-Card Indian Rummy: Rules & Scoring](https://www.rummy-game.com/guides/how-to-play-indian-rummy/)
- [Rummy Points Calculation & Drop Rules](https://www.rummy-game.com/guides/rummy-points-calculation-drop-rules/)

## License

MIT
