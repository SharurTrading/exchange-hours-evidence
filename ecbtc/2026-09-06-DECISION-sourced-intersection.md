# ECBTC after 2026-05-29 — decision: found a key on the sourced intersection

Decided 2026-09-06 after two workflows (unblock-45-and-57, 8 agents; all four hunt
results adversarially verified and held). Relates to issue #57.

## What is now established, on primary text

1. **Both CME channels are exhausted.** The wiki page has exactly four versions, the
   last 2026-04-23, no nextVersion, v5 404s. Every CME channel (ContractSpecs API,
   session service, SERs, Globex notices 2026-03-23..08-31 read in full, clearing,
   Daily Bulletin, product pages, rule filings) restates nothing about ECBTC's weekday
   close after 2026-05-29. Waiting for "CME republishing the cell" has no endpoint.

2. **The two primaries are ordered, not simultaneous.** The wiki's `3:00:00 p.m.` row
   was authored 2026-04-22 (its own Revision History row; table absent from v1-v3).
   SER-9740R is 2026-05-28. Rule filing 26-266 (2026-06-04, a 40.6(d) NOTIFICATION —
   not a certification) reproduces SER-9740R verbatim as Exhibit A; it is the same
   document, not a second statement.

3. **Each primary has a demonstrable weakness.**
   - SER-9740R's Table 2 is the crypto-complex cell carried over unchanged: the SER
     itself says "No other changes have been made to the original SER" (ECBTC was only
     blacklined into Table 1), and its "Current" column gives ECBTC a 16:00 close with a
     16:00-17:00 maintenance period — but ECBTC's actual pre-cutover cell, double-sourced
     in session language by SER-9092 and rule filing 23-014, was "Sunday 5:00 p.m.-
     Friday 3:00 p.m." So the SER misdescribes ECBTC's own prior hours.
   - The wiki's 15:00 is the only ECBTC-specific document, but it is the earlier one,
     was authored by a Confluence sync tool, and was never revised. CME's own July 2026
     gold/crude deck prints the identical row template with `4:00:00 p.m.` for a product
     migrating onto channel 329 "shared with events contracts" — a strong practical
     argument for 16:00, but about other products, so NOT a statement about ECBTC.

4. **Everything else is agreed AND independently confirmed post-cutover.** Saturday
   02:00-04:00 CT with 03:45 pre-open (Globex Notices 2026-08-24/31 place channel 329 in
   the "24/7 markets" list with that "standard schedule"); weekday pre-open 16:01-16:02
   and open 16:02 (both primaries).

## The decision

Serve the **sourced intersection**: the window true under BOTH primaries.

    Mon-Fri   open 16:02 CT -> close 15:00 CT next day   (order_entry 16:01-16:02)
    Sat       close 02:00-04:00 CT                        (order_entry 03:45-04:00)
    Sun       open all day
    weekend   Fri 16:02 -> Sat 02:00 open; Sat 04:00 -> Mon 15:00 one connected block

The disputed 15:00-16:00 weekday hour is served CLOSED. Under the SER reading that
under-reports one executable hour per weekday; under the wiki reading it is exactly
right. It never over-reports. That is the crate's declared safe direction.

## Why this is law, not judgement

AGENTS.md: "Prefer the sourced intersection to omission... Dropping the whole phase
because part of it is disputed under-reports the venue far more than the uncertainty
warrants." And: "absence is a claim too." Today the crate reports ECBTC as unmodelled
after 2026-05-28 — ~23 agreed-open hours a day, six days a week, withheld to protect
against a one-hour dispute. The issue itself said "if overturned, the intersection is
16:02->15:00 CT with Saturday 02:00-04:00".

The issue's counter-argument was that the intersection bullet is scoped to TEMPORAL
ambiguity (undated changeover between two sourced states), not SOURCE conflict (two
documents, same period). That textual reading is fair, and it is a gap in the law: the
bullet's rationale applies with equal force to both. The PR therefore ALSO amends the
bullet to cover source conflict explicitly, so this is the second worked example rather
than a one-off.

## Shape of the key

A new `MarketHoursKey` variant carrying ECBTC's WHOLE life, so a caller never switches
keys on a date:

    < 2023-03-12          sessionless (pre-listing)
    2023-03-12..05-28-26  the event-contracts grid (SER-9092 reprints it unchanged)
    2026-05-29            transition day (opens 16:02 CT Friday, like crypto's 26-114 row)
    2026-05-30 ->         the 24/7 intersection above

Ledger basis: Partial, Gap: executable — the disputed hour is where trades print.
`joins_adjacent_same_kind` and `assign_normal` in identity.rs must include the new key
(weekend blocks carry the following open business date — both primaries say "with
Trade Date roll").

## Do NOT ship

- the word "certified" for 26-266
- "15:00 is ECBTC's inherited termination instant" as sourced text (it is reasoning)
- the gold/crude deck as evidence about ECBTC (it is about other products)
- trading-hours.html's "Event-Based Contracts 16:01/16:00" row (stale, describes
  Event Contracts II, still advertises a Tuesday window cancelled 2026-03-03)
