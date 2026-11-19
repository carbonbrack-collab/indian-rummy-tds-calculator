/**
 * Calculate Indian Section 194BA 30% Net Winnings TDS.
 * @param {object} params
 * @param {number} params.totalWithdrawals
 * @param {number} params.totalDeposits
 * @param {number} [params.openingBalance=0]
 * @param {number} [params.closingBalance=0]
 * @param {number} [params.tdsAlreadyDeducted=0]
 */
export function calculateSection194baTds({
  totalWithdrawals,
  totalDeposits,
  openingBalance = 0,
  closingBalance = 0,
  tdsAlreadyDeducted = 0,
}) {
  const netWinnings =
    Math.max(0, totalWithdrawals) +
    Math.max(0, closingBalance) -
    Math.max(0, totalDeposits) -
    Math.max(0, openingBalance);

  const taxableWinnings = Math.max(0, netWinnings);
  const totalTdsLiability = Number((taxableWinnings * 0.3).toFixed(2));
  const tdsDueNow = Number(
    Math.max(0, totalTdsLiability - Math.max(0, tdsAlreadyDeducted)).toFixed(2)
  );

  return {
    netWinnings: Number(netWinnings.toFixed(2)),
    taxableWinnings: Number(taxableWinnings.toFixed(2)),
    totalTdsLiability,
    tdsDueNow,
  };
}
