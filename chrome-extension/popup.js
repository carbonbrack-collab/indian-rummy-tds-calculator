function calc() {
  const wd = Math.max(0, Number(document.getElementById('wd').value) || 0);
  const dep = Math.max(0, Number(document.getElementById('dep').value) || 0);
  const cb = Math.max(0, Number(document.getElementById('cb').value) || 0);
  const net = wd + cb - dep;
  const taxable = Math.max(0, net);
  const tds = taxable * 0.3;
  const netPayout = Math.max(0, wd - tds);

  document.getElementById('out').innerHTML =
    `Net Winnings: <strong>₹${net.toFixed(0)}</strong><br>` +
    `30% TDS (194BA): <strong>₹${tds.toFixed(0)}</strong><br>` +
    `Est. Net Payout: <strong>₹${netPayout.toFixed(0)}</strong>`;
}

['wd', 'dep', 'cb'].forEach((id) => {
  document.getElementById(id).addEventListener('input', calc);
});
calc();
