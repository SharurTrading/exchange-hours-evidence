# SGX rulebook is NOT a channel for trading hours — closed by SGX's own design

Checked 2026-09-06 against the live rulebook (https://rulebook.sgx.com/rulebook/futures-trading-rules)
and the Wayback archive of the previous Drupal site (rulebook.sgx.com, rbid=3271).
Relates to: exchange-hours-rs issue #45.

## Why this channel looked promising

The SGX rulebook portal annotates every rule with "Amended on <date>" (135 such
annotations in the Futures Trading Rules alone) and offers a date-filterable
"View Updates" feed. The Wayback archive holds ~2,950 captures of the old site from
2019 alone — 801 of them in **November 2019**, straddling the suspected 2019-11-11
T+1 cutover. If trading hours were a rule, this would date the change to the day.

## Why it is closed

They are not a rule. **Futures Trading Rules 4.1.5**, verbatim:

    4.1.5 Trading Hours, Opening and Closing Routines and Closing Range
    Trades may only be executed during the hours in which the Markets are open for
    trading. The Markets' normal trading hours for each Contract are set forth in
    the relevant Contract Specifications. The Exchange may determine for a Contract:
    (a) the duration of trading sessions; (b) the opening and closing routines; and
    (c) the closing range.

And the Definitions chapter, verbatim:

    Contract Specifications  Refers to the commercial and technical terms of a
    Contract, including the Contract size, Contract Month, trading hours, Underlying,
    exercise price, minimum price fluctuation, Last Trading Day, settlement basis and
    method of exercise; Unless otherwise stated, Contract Specifications are distinct
    and separate documents which are not part of this Rules.

Rule 4.1.4 adds: "*Contract Specifications will be posted on the Exchange's website*."

So the rulebook **delegates** hours to the Contract Specifications and explicitly
excludes those from the rules. No amount of rulebook amendment history can date a
trading-hours change, because a trading-hours change is not a rule amendment. The
"Amended on" annotations and the updates feed are structurally incapable of carrying
the answer.

This routes the question straight back to the Contract Specifications / Derivatives
Product Catalogue channel, whose pre-2020 editions are already established as not
surviving in the archive.

## The one T+1 hit in the rulebook, and why it is not the answer

The only "T+1" text in the Futures Trading Rules is in a Negotiated Large Trade
practice note:

    3.1.1 All NLTs executed during or before the Contract "T" trading hours shall be
    "T Trades" while NLTs executed after the Contract "T" trading hours shall be
    "T+1 Trades".

This *defines* the T/T+1 split by reference to the contract's hours. It does not state
any clock time and cannot date a change to them. Recorded so a future reader does not
mistake the keyword match for evidence.

## Status

Channel **CLOSED — structurally, not for lack of searching.** Do not re-attempt.
