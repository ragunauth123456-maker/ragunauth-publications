"""Reproduce Appendix A arithmetic. Institutional estimates are cited in the paper."""
from math import isclose
e2025, e2030 = 485.0, 950.0
cagr = (e2030 / e2025) ** 0.2 - 1
avg_gw = e2030 * 1000 / 8760
nameplate_gw = avg_gw / 0.8
site_twh = 250 * 0.75 * 8760 / 1_000_000
assert isclose(cagr, 0.1439, abs_tol=0.0001)
assert isclose(avg_gw, 108.45, abs_tol=0.01)
assert isclose(nameplate_gw, 135.56, abs_tol=0.01)
assert isclose(site_twh, 1.6425, abs_tol=1e-9)
print(f'PASS: CAGR={cagr:.2%}, average load={avg_gw:.2f} GW, nameplate={nameplate_gw:.2f} GW, site={site_twh:.4f} TWh')
print('These are arithmetic checks, not a grid model or ASI forecast.')