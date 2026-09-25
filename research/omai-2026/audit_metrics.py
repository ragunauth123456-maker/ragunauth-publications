#!/usr/bin/env python3
"""Reproduce key public-source arithmetic from the August 2026 Omai PEA.

This verifies the supplied seven-case sensitivity table and surfaces unit-cost
reconciliation questions. It is not a substitute for the undisclosed financial model.
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXPECTED = [
    (3000, 2444.932, 18, 5.3, 5460),
    (3300, 3206.175, 21, 4.6, 6777),
    (3600, 3966.422, 24, 4.1, 8094),
    (3900, 4726.593, 27, 3.7, 9411),
    (4200, 5484.923, 30, 3.4, 10728),
    (4500, 6243.253, 32, 3.1, 12044),
    (5000, 7507.136, 36, 2.8, 14239),
]
with (ROOT / "pea_sensitivity.csv").open(newline="") as f:
    rows = [tuple(map(float, r)) for r in list(csv.reader(f))[1:]]
assert len(rows) == len(EXPECTED), "Missing or duplicate price case"
for source, expected in zip(rows, EXPECTED):
    assert all(abs(a-b) < 0.002 for a,b in zip(source, expected)), source
ore_t = 156_670_000
ounces = 6_326_775
waste_t = 788_434_000
assert waste_t + ore_t == 945_104_000
recoverable = ore_t * 1.35 * 0.93 / 31.1034768
assert abs(recoverable / ounces - 1) < 0.001
assert abs(ore_t / (18*365) - 23_846.27) < 0.01
royalty_reported_m = 1456.0
royalty_per_oz_pool_m = 266.0 * ounces / 1e6
royalty_per_t_pool_m = 10.74 * ore_t / 1e6
assert abs(royalty_per_oz_pool_m-royalty_per_t_pool_m) < 1.5
assert 220 < royalty_per_oz_pool_m - royalty_reported_m < 235
cash_per_oz = 9325e6 / ounces
aisc_per_oz = 10000e6 / ounces
site_per_oz = 7825e6 / ounces
assert 1473 < cash_per_oz < 1475
assert 1580 < aisc_per_oz < 1582
assert 1236 < site_per_oz < 1238
print("PASS: 7 price cases, mine mass balance, throughput, and cost cross-checks")
print(f"OPEN ISSUE: royalties reported USD {royalty_reported_m:,.0f}m, "
      f"unit metrics imply USD {royalty_per_oz_pool_m:,.1f}m / "
      f"{royalty_per_t_pool_m:,.1f}m. Obtain the full PEA model.")
