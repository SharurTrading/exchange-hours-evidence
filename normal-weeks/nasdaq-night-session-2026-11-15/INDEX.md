# Evidence index — `normal-weeks/nasdaq-night-session-2026-11-15`

Rule-text, operator-channel and press-corroboration passes for the Nasdaq
Expanded 23/5 / Night Session work-up (crate issue #396), run 2026-11-15 UTC.

## The determination this evidence carries

1. **Commencement gate (T1).** Nasdaq Equity 1 §1(a)(19) (live rulebook, `nasdaq-equity-1-rulebook.html`) requires, before the Night Session commences, that the Equity Data Plans establish an equivalent consolidated-data mechanism AND notify the Exchange they are prepared, and that **Nasdaq file a 'Night Session Proposed Rule Change' under Section 19(b)** confirming compliance and the Plans' readiness. The SEC approval order for SR-NASDAQ-2025-109 (Release 34-105199, 2026-04-10, `sr-nasdaq-2025-109-approval.pdf`) states the gate plainly: 'The proposed rule change must be filed with the Commission and approved, or otherwise become effective pursuant to Section 19(b) of the Exchange Act, before Nasdaq can commence trading in the Night Session.'

2. **Discharge status as of retrieval: not witnessed.** A Federal Register API search for the phrase (2026-11-15, `fr-api-night-session-proposed.json`, coverage through 2026-11-13) returns nine documents: the original filing notice (FR 2026-00416, 2026-01-13), the Amendments-2/3-and-order publication (FR 2026-07259, 2026-04-15), and seven ancillary immediate-effectiveness filings that recite the obligation (ports pricing, clearing/settlement, MWCB, ETP halts, clearly erroneous, Rule 4759 data sources, Equity 7 §115). None is the confirming change. Nasdaq's own 2026 filings list (`listingcenter-rulefilings.html`, through SR-NASDAQ-2026-098) contains no Night Session confirming filing; SR-NASDAQ-2026-064 describes the 23/5 rules as 'previously approved but not yet operative'. The Commission's 24X exemptive order (Release 34-106061, 2026-08-07, `fr-2026-16572-24x-exemptive-relief.pdf`) records the Equity Data Plans 'have not established readiness' and 'will be ready to accommodate overnight hours by December 6, 2026, or a later date soon thereafter'. The 18-month deadline for the confirming filing runs to 2027-10-10.

3. **Topology (T1/T2, for the encoding work-up once the gate discharges).** The Night Session is a tradable matching session: approval order p.20224 'All NMS Stocks would be eligible to trade during the proposed Night Session'; Equity 4 Rule 4120(b)(1)(B)(v) 'will trade thereafter throughout the Night Session'; a distinct matching instance with 9 p.m.-4 a.m. ports; quotes and trades disseminated to the SIPs. Bounds: Equity 1 §1(a)(9) System Hours '9:00 p.m. ET on one calendar day … 8:00 p.m. ET … from Sunday at 9:00 p.m. ET through Friday at 8:00 p.m. ET'; §1(a)(19) Night Session '9:00 p.m. … through 4:00 a.m. the next calendar day Sunday through Thursday provided that each such next calendar day is a Business Day'; the 8-9 p.m. Mon-Thu pause cancels all outstanding orders at 8:00 p.m. and again just prior to 4:00 a.m. Trade date: executions 9 p.m.-midnight carry the next calendar day's trade date (CTA/CQ + UTP approval orders 34-105779/34-105780 define the Processor trade-date window 8 p.m.-to-8 p.m.; the TRF FAQ and the operator hub state the 9 p.m.-midnight next-day rule) — the Sunday 21:00 open belongs to Monday's trade date. Holiday shape (approval order): closure effective as of 8:00 p.m. the calendar day prior; reopen 9:00 p.m. on the closure date unless Friday, in which case reopen Sunday 9:00 p.m.; early-close days resume 9:00 p.m. the same day. Order-type restrictions (limit orders only; no unpriced/pegs; LOP) shape the profile but do not demote the session.

4. **Press (T3/T4, corroboration only).** Every outlet describing mechanics uses execution language (Jones Day's 'T' sale condition; 'lit national securities exchange'; Friedman's 'more lit market environment'). No article describes an order-entry-only exchange phase. Contradictions flagged in the sweep report are press errors (PYMNTS' '8 p.m. start'; Euronews' stale 'subject to SEC approval'; NYSE/NYSE Arca conflation).

## Artifacts

Retrieval window 2026-11-15T01:04-01:27Z window (three parallel passes; per-file instants in retrieval_*.txt sidecars and MANIFEST.sha256). Derived `.txt` extractions sit beside their sources (pdftotext -layout) — cite the source, never the extraction. Press files carry `retrieval_*.txt` sidecars with per-file URL/instant/sha. One relay-cache caveat: `data-nasdaq-GTH-faq.relay.md` was served from r.jina.ai's cache after the live URL 404'd (`data-nasdaq-GTH-faq.live.html` is the JS shell) — weaker channel, quotations used only where the hub/FAQs corroborate. `nasdaq_sys_hours.pdf` re-verified byte-identical to the 2026-11-14 bank (0439-26): not republished.

| File | sha256 | Bytes |
|---|---|---|
| `DN2026-3.html` | `b46860628e1982b82422b0a534ef75abc9e47441be75ef54596534ff2c8902cc` | 87568 |
| `DN2026-3.txt` | `09ab303a5257aa845f9a43e6dfb568728594a5180a2b26be345e53497dfcdf12` | 20452 |
| `DN2026-8.html` | `1e8b2a7efdee220027e266d2b71060c0723af43713e270d5d44484b0c2bac36a` | 80297 |
| `DN2026-8.txt` | `2c946b5c889904acc02d64070d9d9bc0186b69fa5a72ce06c2574c5f5604a6c8` | 17979 |
| `ETA2026-39.html` | `557b98095fb27503948c5edce9e071c70140f5e66d97f364d7fbc58a065aeed7` | 74873 |
| `ETA2026-39.txt` | `28681e3c89004924f8180bd430026386b0df4357fc5c97ea0a1b5ba6a0a21dba` | 12807 |
| `ETA2026-55-retry.html` | `5ccfff0e25524ccd6ce05ff8ba718985ab535cc3db3df0b04844589d5448f25c` | 83743 |
| `ETA2026-55-retry.txt` | `6cd0433e130c6481e69175c253b650544f9853601f242c58697da7a44387debf` | 14760 |
| `ETA2026-55.html` | `492e2e6cb3304675662c06817a15ac2951b82cdf9706fbc28c5cdf47ab99719b` | 42894 |
| `ETA2026-55.txt` | `c91c41fd30eb77d1e90b8b82606539c04b67a846f1ba32dd2c2f93148cbf89da` | 7736 |
| `ETA2026-67.live.html` | `278b9d19e7104f392164e00b013d67ece38b4400b2c465cc3be452a9d30d87b8` | 61651 |
| `ETA2026-68.live.html` | `fa3d5e7e7cfed638b199683532fe977ba97c13db0ece19086e0aade3efd958e1` | 83861 |
| `ETA2026-68.text.txt` | `85ecfbc0bedb1ab63493da29ca53d0a7d0aa2d7adb48835f4d4f9c43e4161539` | 9815 |
| `ETA2026-69.live.html` | `94e9e46640675efca1a1643a85e70ce415324d1846a97781a573d10f19146e46` | 71933 |
| `ETA2026-69.text.txt` | `9e714f7337c1ef0dc31aa3565d0730bd7f7a3bd9921ddf330c012522a662e631` | 8669 |
| `GTH-corp-actions-faqs.pdf` | `fe69703e3dcd14c0bc9319b251e75ad941a2209f47430710b6d2620c1e1f62da` | 171960 |
| `GTH-corp-actions-faqs.text.txt` | `4d385fadd005fc79b4bf912188ee7e33cbe0817c805d361afc9d643f32785499` | 9205 |
| `GTH-faqs.pdf` | `67dcf8cbd75570496849b1e734b81dad75909e367ee6f50f0a706adb7da2a966` | 859659 |
| `GTH-faqs.text.txt` | `ba695771f03cc4b9611b04a18904040b9329becac50100dd57b74305fea47645` | 10276 |
| `GTH-hub.live.html` | `c4da333127db70726adffbd7d1ccf3912574e728d5cae1d462de80e886518757` | 185635 |
| `GTH-hub.text.txt` | `4316e6a0a7d69ff42697b0328ada71e6726626a0b8834b042d5057f2abab0654` | 8945 |
| `GTH-post-trade-faq.pdf` | `e696da2c1c0acd9a59d799bbf3ab3fbf213f59a76834d403e9a78d0e3cc1af53` | 245511 |
| `GTH-post-trade-faq.text.txt` | `c9c63ab4af2f42116fe04276e1ba3d5c126f5723de8fa1b2b0c496a513d8476e` | 15342 |
| `UTP2026-34.live.html` | `4af6dd5f70df95e65c6c0fdf779c6f8fd9df210054509f3d326f40e45f2f9edf` | 55707 |
| `UTP2026-34.text.txt` | `461539a55ec44c27106787ecf1f5df6342ab0f9f82b9be5213d62985f9837287` | 7108 |
| `alston-looking-ahead-nasdaq-extended-hours.html` | `e7ea87cf93452a4170e9d0ef88a81e3a03717f4b143b624cd8981128bef24267` | 121943 |
| `biggo-nasdaq-23-hour-dec-6.html` | `f055be95e82c169dafc4f0e13e0f99291e634085d6c25e81a771f0a02384affa` | 141661 |
| `biggo-nasdaq-takes-on-crypto-23-hour.html` | `d5f6901106005f2c81cf002c81254279bc508737efff00d695ab543370bf2677` | 152599 |
| `cooley-23x5-trading-almost-here.html` | `a2273865b191236f148ff2a9e85d588aef39b953e713d704274e48cd609eed0d` | 71510 |
| `data-nasdaq-GTH-faq.live.html` | `2f90f4ca2601d521d211c72d36d5ca3b9e9d1e2e01ee742f6e124b190646b722` | 3185 |
| `data-nasdaq-GTH-faq.relay.md` | `34fbdc0b5f05de1661838bcca659045edd25ab1b5156dcc110e54ef333a5ed80` | 22817 |
| `edgar-fts-night-session-all.json` | `f1a86f25b72c47a4642198ba748bc5f04b7326a09a1ce51eab9643ffa65753cb` | 12333 |
| `eta2026-64.html` | `f2e57dd854c3312413e433c7b910c3adca660f11ab94d2219dc320606f7b59a4` | 74271 |
| `eta2026-64.txt` | `35f22793941b6f29170137de544abef337c713e80c9f8bd42f198c18a81170c2` | 14188 |
| `fr-2026-00416-original-filing-notice.pdf` | `53542fcd02863fc1a243c5491a0d0120e59e6f7724977510463656081383ce40` | 244440 |
| `fr-2026-07783-cta-oip.pdf` | `b051e582b8a6ffd601c5049719e317ddb3f59250d5c9203176b0cc4acc80a020` | 488864 |
| `fr-2026-07787-utp-oip.pdf` | `19606e6ff1dbbe14d2718feeef67f5d33c01c49f7247e219eb16979eb8357550` | 484996 |
| `fr-2026-13212-utp-approval.pdf` | `e26190ad7f07bdead92ec1b90d4bcb69ee37b4c5a475983d1b44d757a9e713e6` | 224120 |
| `fr-2026-13212-utp-approval.txt` | `9f98ac6b23d5a3f52a566277791b50a77093aa700ecc695839fadebe9f0e227a` | 66391 |
| `fr-2026-13234-cta-cq-approval.pdf` | `1b30551f7c61bbf44de4dd8bad3de9c6b8ff11421cd53d7da01f7ec3806bb910` | 222180 |
| `fr-2026-13234-cta-cq-approval.txt` | `99117b4bf14d13395d87baa75dcd0e0a62b7012e61c9de893b8fcaf1850722da` | 64432 |
| `fr-2026-16572-24x-exemptive-relief.pdf` | `e85f643300798ac9f29f62af12dc2e742e86b86c3712bd9b5ce08eeeef2ed028` | 267174 |
| `fr-2026-16572-24x-exemptive-relief.txt` | `8a34790051f2d8b0834cd70d2c958ab6a667252b2656a4ee922a63a30e7ae8e7` | 190080 |
| `fr-2026-20297-nasdaq-clearing-settlement-23-5.pdf` | `29a5002459aca2453037417dc262cd8d94fdd630bbf5eebd521d61c1bc049ec9` | 218240 |
| `fr-2026-20297-nasdaq-clearing-settlement-23-5.txt` | `099e6abb6f1aa1157dfae07f1bc7c269ba14dbc0ce6121ff193776a703db78e6` | 45365 |
| `fr-api-34-105268.json` | `a8cbdf6bfe1ceee4b53232d3e83de7ecaa413e3a1aba0f116ccbf621cabc552c` | 903 |
| `fr-api-34-105269.json` | `9610d8ba6e5e013d2e996eb7665598015a2d7ccfd3bb0d0012a2ef2eb9596e9d` | 1270 |
| `fr-api-equity-data-plan.json` | `c8bcc63fb43438896d0f207937bcd21996e5bcbc6c90768639d455088a8e4317` | 3316 |
| `fr-api-nasdaq-night-session.json` | `d2f9fdd785d37fb06ba33337658c3315264720783ae1905e1342ccc6129240b9` | 4149 |
| `fr-api-night-session-proposed.json` | `7f15a59ae73d15d690c6e420aba0a3cca7235cd28fe3a23d03821dd93e4c43e9` | 3736 |
| `fr-api-utp-hours.json` | `451675a3dc957d5386c794c591c72b9193a58d01f5d961816ac937c70f578413` | 8654 |
| `globeandmail-up-all-night-nasdaq.html` | `c8b66071be0faa3788fb2441e855704a6a4e70b5f91be95e61d18ca092a791b9` | 627069 |
| `harvard-corgov-skadden-nyse-arca-nasdaq-extended-trading.html` | `5f0f159bc2dc6848526b6529be9179dab8099abcdb3fa1a34278ebe5e747f0ee` | 112199 |
| `investmentnews-round-the-clock-trading.html` | `ace9227ae73c0c8fbf8b36d958284417985d71ebfd13977a5ac7be9eccc2440f` | 81534 |
| `jdsupra-skadden-nyse-arca-nasdaq-extended.html` | `b2c94dbb6d7f94eb19c5ead8f80200a76d1d9edecc70ddbed630e5d16738361b` | 184033 |
| `jones-day-overnight-session-evolution.html` | `eef1c8b918c3ad34bd3f47a5203fe2cf8aea1461ef79de7f7b9abb24e9299cec` | 108113 |
| `listingcenter-rulefilings.html` | `25ec9b208edb4bc8fcbea63b133a7169a82606d34bcde1044d809d092fffadf3` | 2531939 |
| `marketsmedia-nasdaq-debut-23-5-dec-6.html` | `3a139b20ca92c7c250fde1e92b198c134160f88c7f56f75349435398d9f206a0` | 129883 |
| `moneytoday-en-brokerages-empty-hour.html` | `2e0a1214257a6286eaede258bb3eeb9c0f12bfe420f6fe852247dc652a9a9e60` | 38380 |
| `nasdaq-com-23-5-trading-hub.html` | `c662102820c5560537abef4e64ad7c3f70891bd47de7401f53127c2a4569f85c` | 185635 |
| `nasdaq-equity-1-rulebook.html` | `9f1d836f4666a77718c58a2a8d68df1df22950f2ba0e3b57a46ee9f9d252fc08` | 102953 |
| `nasdaq-equity-1-rulebook.txt` | `a0e29cf6dee937939afa732505f981aa2b20f011a255da844e367f524e9dbf10` | 17355 |
| `nasdaq-equity-2-rulebook.html` | `d1f0cc63e3c477db877a758cfa18bd42e808398febeaaff8ca90d08a8ec3a7d8` | 244477 |
| `nasdaq-equity-2-rulebook.txt` | `b5327e54178df8c37d7c94726672af487ac5012eb97e542b7b5cb6c33692a5d2` | 70263 |
| `nasdaq-equity-4-rulebook.html` | `31df3e32782f204e639fd9130df506a56bd25bd4c1d660b743128586891e622a` | 1116129 |
| `nasdaq-equity-4-rulebook.txt` | `48dc27623de432d2a1ad37202a36370b1be25b760dba1d1bfaf8bd98bcb606bd` | 379399 |
| `nasdaq-explains-23-5.html` | `547fbe3ffe60d042bdc6df8bfdbb1edf02657639fb4dfc2e5492b35a2ee9100b` | 184227 |
| `nasdaq-explains-23-5.text.txt` | `8432ad64bcf8766da55c59c303f721099c733c8e92fe408b1417dcb693535d9a` | 12139 |
| `nasdaq-explains-what-is-23-5-trading.html` | `c64f63e2e927c648f35499dae81440b83b955313f822baffd0ed8d14122dad81` | 184226 |
| `nasdaq-global-trading-hours-corporate-actions-faqs.pdf` | `fe69703e3dcd14c0bc9319b251e75ad941a2209f47430710b6d2620c1e1f62da` | 171960 |
| `nasdaq-global-trading-hours-corporate-actions-faqs.txt` | `4d385fadd005fc79b4bf912188ee7e33cbe0817c805d361afc9d643f32785499` | 9205 |
| `nasdaq-global-trading-what-participants-need-to-know.html` | `63c4050996663676cacd1444360888575b0ea5d3c55973dd9f488013ca99e641` | 170254 |
| `nasdaq-post-trade-23x5-faq.pdf` | `e696da2c1c0acd9a59d799bbf3ab3fbf213f59a76834d403e9a78d0e3cc1af53` | 245511 |
| `nasdaq-post-trade-23x5-faq.txt` | `c9c63ab4af2f42116fe04276e1ba3d5c126f5723de8fa1b2b0c496a513d8476e` | 15342 |
| `nasdaq-roundtable-chuck-mack-overnight.html` | `9a2b7f153cec1b668c17478aeef7d8899c1debc6ee3ea780aaf6b5022c723b31` | 172945 |
| `nasdaq_sys_hours.pdf` | `7f2bbf723729c2465711b26a26937a35b78dbf9b8f638b3843c47fd12cc361f8` | 36023 |
| `nasdaq_sys_hours.text.txt` | `7ee136afd13db4ff385dfb0ac4b492dfff12bd482640bd93198cf1b115e16a67` | 2605 |
| `newsbitcoin-nasdaq-23-hour-december-launch.html` | `07c8289e11eb60ae6949700acf65d6be5c5b966c45f5f353c43fe7682fe36635` | 1037378 |
| `newsrss-page.live.html` | `a3677a7b97296c76ef174e4c662695dda0e8442de9914c230cca66a83657e29d` | 56902 |
| `pr-sips-sec-approval-extended-hours.html` | `8cb0a9a9fca50e5414679e163e5423dd4383f97c1c35ac9ce7bf92a37174bd61` | 181110 |
| `pr-sips-sec-approval-extended-hours.txt` | `01746985b0d68440400c41826e0d72307d06c005a415618288b93a28a1b4beb1` | 25477 |
| `pymnts-us-exchanges-extend-trading-hours.html` | `d0655fef2290fbcc96c6dab7ba16b40c637214ff2989822cb061575e394de67a` | 158625 |
| `rss-data-all.xml` | `2b3ca1c1afcaa92b933bd7d3c8d42ca6c129af0a594b4d8b98ddc613d263e21b` | 5807 |
| `rss-equity-all.xml` | `3fddb7959c2f7c59a191c19758d3c0cccee1bf6f830e33f10ef7886ddc41438b` | 31984 |
| `rss-general.xml` | `87c4325fc7556681dbc114bb12affae9c48fda09d6627d2ff4a284f89ceae6db` | 544 |
| `sec-34-105779.pdf` | `047d12d34883a4c3e2ab42403bbea597d232dca9e165d59a9c1419742d142982` | 156353 |
| `sec-34-105780.pdf` | `061f2fa1a2144a1aad692fcb56a453151b06145a35a0d98b91b611e749d0e978` | 154872 |
| `sr-nasdaq-2025-109-amendment2.pdf` | `8f3cdd993d875ceab8b4bc14633445c6ea9d88f6211acc3a1c099a5e24a0613b` | 2852137 |
| `sr-nasdaq-2025-109-amendment2.txt` | `58b755cc93a9d04922878cc7e564187aea8554910ea4379582b9fb05c1cfc712` | 666793 |
| `sr-nasdaq-2025-109-approval.pdf` | `7abf8ed33f22c6426fa23fb6b5f3242afdab6457f0c0cde67eea14b5f3a8b172` | 281434 |
| `sr-nasdaq-2025-109-approval.txt` | `eb208fd2200859fb9a30e1458f7b8f07d93f7e262d46a42fb6c9044f2fc32c61` | 241058 |
| `sr-nasdaq-2025-109-filing.pdf` | `ab18e9c7f8f5fc2249570a706e5060376dc28c39f9dc6c9fa9ea2c6a8562ab5d` | 1115240 |
| `sr-nasdaq-2025-109-filing.txt` | `dc0e7fb56c9371cdf138c14e1cad05a7e1db3e1e911553882b343bb98cf4feea` | 393909 |
| `trader-calendar.live.html` | `8467b4e2067e97d8f13ca4030c254504cb1f1b66644660f3dbe3eeddd61322c2` | 54662 |
| `trader-tradingday.live.html` | `90cc715758c992c46f0e96758dc86bae14d0a3f8af4b7e0e7e71e608d6f05659` | 21210 |
| `yahoo-au-nasdaq-confirms-23-hour-overnight.html` | `96e7259215d10071a4e828422a12ffe7f5c830d145da2513d873201defbad600` | 435810 |
| `yahoo-au-nasdaq-plans-nearly-23-hour.html` | `7063a62e6eaaadf7eb5e46e7dc791697c2d395b3d65b1fb115e1a23b5e6168f1` | 429797 |
| `yahoo-nasdaq-red-flag-overnight-risks.html` | `2c9d6be895cbc6b00731d679d8a534c036d47e567b3f059699ddaae353f8d803` | 915941 |
