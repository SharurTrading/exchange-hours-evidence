<!--
Copyright (C) 2026 Kevin Monaghan. All rights reserved.

This file is proprietary and confidential.
Unauthorized copying, use, modification, distribution, or disclosure of this file,
via any medium, is strictly prohibited except under a written agreement with the
copyright owner.
-->

# GLBX.MDP3 catalog audit

- source scope: latest 7 distinct source days
- source files: 7
- selected source dates (YYYYMMDD): 20260422, 20260423, 20260424, 20260426, 20260427, 20260428, 20260429
- artifact bytes: 12888936
- canonical identities: 713867
- semantic versions: 713869
- unique interned definitions: 713869
- decoded records: 6763160
- accepted observations: 5265398
- IRS: 168
- generic MLEG: 133983
- unknown families: 0
- invalid economics: 0
- invalid legs: 0
- excluded explicit test definitions: 3016
- excluded synthetic/no-ready definitions: 162934
- excluded internal monitoring definitions: 28
- future observations emitted using listing-exchange fallback: 318994
- distinct future roots emitted using listing-exchange fallback: 1342
- distinct correlated missing-hours signatures: 1342
- malformed definitions: 0
- unresolved option underlyings: 614660
- unresolved spreads: 0

## Futures using listing-exchange fallback

Correlated source evidence is in [`missing-market-hours.tsv`](missing-market-hours.tsv). These otherwise-valid futures were emitted without an authored product-family selector. The count above is observations across the selected snapshots, not unique contracts.

## Malformed definitions by reason

- none
