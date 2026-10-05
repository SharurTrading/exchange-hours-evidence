# INDEX — stage 2.2 wave 5, the PDF half of CME's in-place revision history

Retrieved and dumped 2026-09-17 UTC for repair item 3 of
`holidays/cme-2013-2015.verify.json` (round 2, `matches: false`). The round-2 verdict
found that round 1 had enumerated only the `.xls`/`.zip` half of CME's in-place
revision history: the 32 PDF URLs the block cites carry **73** distinct-digest
status-200 captures in CME's own archived responses for 2013-2015, of which 31 are
cited and **42** are earlier revisions that no round had retrieved. Two of the 42 had
already been pulled by the verifier (`../cme-2013-2015-verify-r2/new/`); the remaining
**40** were retrieved here, together with the cited captures of 31 of the 32 URLs and
the out-of-scope 2016 New Year's URL, so this directory is a complete dump of every
capture the reconciliation reads.

Bytes were fetched through the Internet Archive `id_` raw replay (byte-identical mirror
of the operator's response). Tier **T1** — CME Group's own published Globex holiday
schedules. `pdf/` holds the responses, `txt/` their `pdftotext -layout` renderings;
`retrieval.json` is the retrieval manifest (`base`, `timestamp`, `original_url`,
`cdx_digest`, `cdx_length`, `saved`, `sha256`, `bytes`, `note`) and `cdx_candidates.json`
the candidate list computed from `../cme-2013-2015/cdx_holiday_calendar.json`.

## What the reconciliation found

`tools/wave5_reconcile.py` re-reads every capture, groups its printed values by product
section and day heading, and compares each earlier capture against the one the block
cites. Its output is `tools/out/wave5/reconciliation.json` in the crate checkout. Two of
the 42 earlier captures state a session value the cited revision does not:

* `2015-4th-of-july-holiday-schedule.pdf@20150326113353` (footer 'Last updated
  12/29/2014', sha256 `664f4b885e090fccfe15152781ba62014aaa1650d1dfdf41564483d457d4ce2b`,
  112477 bytes) gives the **Equity Products** line `1215 CT / 1315 ET / 1715 UTC - Early
  close` on Thursday, July 2 2015, where the cited 6/1/2015 revision gives `1615 CT /
  1715 ET / 2115 UTC - Regular close`.
* `2014-4th-of-july-holiday-schedule.pdf@20140326153233` (footer 'Last updated
  2/26/2014', sha256 `61ef891b5f43164317814b0d5de6619337e1e11f5df1251b0ced886a7193827b`,
  113700 bytes) prints `1200 CT / 1330 ET / 1700 UTC - Early close` for the **Grain,
  Oilseed & MGEX Products** line where the cited 7/1/2014 revision prints `1300 ET`.

Lineage settles both without moving a recorded value: in each pair the cited capture is
CME's later revision, by the operator's own 'Last updated' footer (6/1/2015 after
12/29/2014; 7/1/2014 after 2/26/2014) and by capture time. Neither change touches a
date the block records a row for — 2015-07-02 is `normal` for every crate family on both
revisions, and the 2014 pair differs only in the ET column of a line whose CT value is
unchanged.

## Captures

| file | cited? | capture (UTC) | sha256 | bytes | Last updated | retrieval |
|---|---|---|---|---|---|---|
| `pdf/2013-4th-of-july__20121118211122.pdf` | earlier revision | 20121118211122 | `76ca10a532068b4df2f21c86e7c43cfe1e005e0688a988a82127c2a82581b53f` | 129329 | 11/12/2012 | http 200 129329 |
| `pdf/2013-4th-of-july__20130309115311.pdf` | earlier revision | 20130309115311 | `469162794d1ca51f1783d5b2352f41358b405067f5634b5e8521a04983d65680` | 68997 | 1/4/2013 | http 200 68997 |
| `pdf/2013-4th-of-july__20130623205825.pdf` | **cited** | 20130623205825 | `52c62e72329866f12726363d762335c8dadfdd3407c3643f38d7ed74608e8eb7` | 71527 | 6/4/2013 | http 200 71527 |
| `pdf/2013-christmas__20121119021305.pdf` | earlier revision | 20121119021305 | `b1c5403ccca2771a26de13ae87102f20093275c4d8234e5adac8fce71f43a091` | 122687 | 11/13/2012 | http 200 122687 |
| `pdf/2013-christmas__20130309115253.pdf` | earlier revision | 20130309115253 | `2a6353c4f56cf5d4beed454920fe8b2147c5f81a68b77e7434c4ff7ce12b141d` | 62942 | 1/4/2013 | http 200 62942 |
| `pdf/2013-christmas__20130623201646.pdf` | earlier revision | 20130623201646 | `1f56d47f2b156b971882a0be3836a75c8265873f958a273a17df3e9e90d63ee3` | 147519 | 6/11/2013 | http 200 147519 |
| `pdf/2013-christmas__20131007172634.pdf` | earlier revision | 20131007172634 | `4b48f6daf092865aa743ae64730401e278951deb3b514686f12c0dac13919add` | 147870 | 10/4/2013 | http 200 147870 |
| `pdf/2013-christmas__20140412062428.pdf` | **cited** | 20140412062428 | `1389ade6b120383d05e8d6e8ed9c38f1e2394dd250c86b19606548618285e848` | 146485 | 12/4/2013 | http 200 146485 |
| `pdf/2013-columbus-day__20121119001554.pdf` | **cited** | 20121119001554 | `9679853fc45be642403cf58cac17852bd267f228706a696128223f7093005d2d` | 85678 | — | http 200 85678 |
| `pdf/2013-good-friday__20121119001558.pdf` | earlier revision | 20121119001558 | `6499a0bde549335f6a66c577d4c2c32f05664393949e4e13ccc319e51609e291` | 122185 | 11/14/2012 | http 200 122185 |
| `pdf/2013-good-friday__20130309115341.pdf` | earlier revision | 20130309115341 | `0807550ed2f50ec9f5285b8793da94543b7ab27b0c02df3fd3b292ecb7ceda48` | 64755 | 2/20/2013 | http 200 64755 |
| `pdf/2013-good-friday__20130623195925.pdf` | **cited** | 20130623195925 | `c05e590c950581e19ac2e8ee5327ebcfb4fc111b231b506abefae44534ee9b68` | 63251 | 3/14/2013 | http 200 63251 |
| `pdf/2013-labor-day__20121119001605.pdf` | earlier revision | 20121119001605 | `2aa7e133032982bc936177552f35f5471079821d108f35dd79227b70d331885a` | 128357 | 11/12/2012 | http 200 128357 |
| `pdf/2013-labor-day__20130309115345.pdf` | earlier revision | 20130309115345 | `d8a6ec6a819378815a53f6f0bc93aa08c79e68b52cf1d9bbb8d4735335750455` | 71745 | 1/10/2013 | http 200 71745 |
| `pdf/2013-labor-day__20130623201023.pdf` | earlier revision | 20130623201023 | `6812b6fa78544c8b0543005c18d4a4922b09d874d4039f944f5d0b3436b6e7ef` | 70901 | 5/2/2013 | http 200 70901 |
| `pdf/2013-labor-day__20130902170841.pdf` | **cited** | 20130902170841 | `8f22671fa723d33fe36d58bb29e80ebd15370d3bf9000a9b45d56a0cab0608ef` | 81507 | 8/23/2013 | http 200 81507 |
| `pdf/2013-martin-luther-king__20121119001609.pdf` | **cited** | 20121119001609 | `43a646480cc7ffca137890901c0fc716ed04403e0dabc1ef07749d2b21b70c4c` | 128212 | 11/12/2012 | http 200 128212 |
| `pdf/2013-memorial-day__20121119001616.pdf` | earlier revision | 20121119001616 | `adf9cc5a2b5d106d70b286ff8e7eaf57bd6aecb43c9c9abcfe22972f2085cf32` | 128615 | 11/14/2012 | http 200 128615 |
| `pdf/2013-memorial-day__20130309115320.pdf` | earlier revision | 20130309115320 | `31eb4599c5865e43f7de7d1c43c1cb0f1285fd1b1a675831578fa8115115eb1c` | 76240 | 2/6/2013 | http 200 76240 |
| `pdf/2013-memorial-day__20130623203604.pdf` | **cited** | 20130623203604 | `7cc47e352ff4874614fdb583cecd41b3ac3fcf95be6199ea5d489b8b34d2afe7` | 70520 | 5/2/2013 | http 200 70520 |
| `pdf/2013-new-years__20120107085242.pdf` | earlier revision | 20120107085242 | `ae7d763c95b7ddb0af74d48d6e406f10ad06aad354552dda8e562822e1f1e4d2` | 114898 | — | http 200 (attempt 1) |
| `pdf/2013-new-years__20120505161531.pdf` | earlier revision | 20120505161531 | `6edb1bf953267d7ac0ce8bd93f8c1ddbcc7c236093fd41e1a4de259b9909bfa6` | 49965 | — | http 200 (attempt 1) |
| `pdf/2013-new-years__20120915003225.pdf` | earlier revision | 20120915003225 | `d1056fbd7e0572dcd712c10deac353f2eeb586fe5e2db7af023e6a88d95556be` | 55474 | — | http 200 (attempt 1) |
| `pdf/2013-new-years__20121118211106.pdf` | earlier revision | 20121118211106 | `9a4bee5d6eb31bc124ea6a84a9f7bb09b0f245a4b9003907d80651a1365b4cfa` | 55454 | — | http 200 (attempt 1) |
| `pdf/2013-new-years__20130414194146.pdf` | **cited** | 20130414194146 | `e29c2c968cdf20883d55acd13bab50e9df02c547826bca9d2867f5bf9b2df3f7` | 52390 | — | http 200 (attempt 1) |
| `pdf/2013-presidents-day__20121119001620.pdf` | earlier revision | 20121119001620 | `a1798740490609a021a8e674a6a8b83a47f3ea9267b9fd0d5fe429305f67eaec` | 185759 | 11/12/2012 | http 200 (attempt 1) |
| `pdf/2013-presidents-day__20130309115337.pdf` | **cited** | 20130309115337 | `e1242116eec5b7f3c5748e61adbf5bf7a809f48739ad456391f1d8b4bafceff6` | 71660 | 1/10/2013 | http 200 (attempt 1) |
| `pdf/2013-thanksgiving__20121119001625.pdf` | earlier revision | 20121119001625 | `cf84e2472d131c9aeec50196c16b1e0a12f623995c1c0309779892298b407ff0` | 130164 | 11/16/2012 | http 200 (attempt 1) |
| `pdf/2013-thanksgiving__20130309115244.pdf` | earlier revision | 20130309115244 | `778305ba3adcb1c8de8ada9ddad20ee222bebe0f004d049bb69da665b9330e06` | 69884 | 1/4/2013 | http 200 (attempt 1) |
| `pdf/2013-thanksgiving__20130623204528.pdf` | earlier revision | 20130623204528 | `f78ed26cad42202493a1f2b8788ff34fe47e3c66bec3ceaf92b68d48e7a4e564` | 70066 | 5/2/2013 | http 200 (attempt 1) |
| `pdf/2013-thanksgiving__20131007205747.pdf` | earlier revision | 20131007205747 | `0a472c8581002b1495469ce7df7e56d595355b94c180e8434122cbacf150ecfb` | 134969 | 7/5/2013 | http 200 (attempt 1) |
| `pdf/2013-thanksgiving__20140214062836.pdf` | **cited** | 20140214062836 | `1f7f6428990a5bd01065f31c4388bf5aeeb12d9219e5af6d16b1cec86bbc158b` | 75026 | 11/13/2013 | http 200 (attempt 1) |
| `pdf/2013-veterans-day__20121119001630.pdf` | **cited** | 20121119001630 | `7e5bd54859002a29f50ef3f1eec1f46f3fd3a7d51e9aed303f189a097719252b` | 85574 | — | http 200 (attempt 1) |
| `pdf/2014-4th-of-july-holiday-schedule__20140326153233.pdf` | earlier revision | 20140326153233 | `61ef891b5f43164317814b0d5de6619337e1e11f5df1251b0ced886a7193827b` | 113700 | 2/26/2014 | http 200 (attempt 1) |
| `pdf/2014-4th-of-july-holiday-schedule__20140630024247.pdf` | earlier revision | 20140630024247 | `70824557a946c7e7c2099cef4daa73626d76206b1901a0e8b288f858c1511b8a` | 56040 | 5/30/2014 | http 200 (attempt 1) |
| `pdf/2014-4th-of-july-holiday-schedule__20140708015736.pdf` | **cited** | 20140708015736 | `34faa82435c6d8bb1088593c8945b6a5faaaa67b36c6a6422a24e4a25572ba77` | 56112 | 7/1/2014 | http 200 (attempt 1) |
| `pdf/2014-christmas-holiday-schedule__20140326153852.pdf` | earlier revision | 20140326153852 | `96b4b3fe068310a410a867fe0dae443a4e668e556f352c834ceba20c5df4b9fd` | 111515 | 2/26/2014 | http 200 (attempt 1) |
| `pdf/2014-christmas-holiday-schedule__20150121141000.pdf` | **cited** | 20150121141000 | `8125a18c9cad9b770be39b89c3193ee419240d409e39aa510d6eb3e8eba94e25` | 54124 | 12/9/2014 | http 200 (attempt 1) |
| `pdf/2014-good-friday-holiday-schedule__20140326152735.pdf` | **cited** | 20140326152735 | `4e8593e96eb42af2cde99f6ed906d4fe4a2ea8f976fc9f8d8f561f3049cc7f0e` | 105279 | 3/17/2014 | http 200 (attempt 1) |
| `pdf/2014-labor-day-holiday-schedule__20140326193120.pdf` | earlier revision | 20140326193120 | `afd75410337447b94f4aeae428a0a4a917035876b8e0d739ae3fa7480534c201` | 117322 | 2/26/2014 | http 200 (attempt 1) |
| `pdf/2014-labor-day-holiday-schedule__20140912071608.pdf` | **cited** | 20140912071608 | `dfd92a530d114a1f1c68dd52be4315fd307d8f8cfb344d71de78334b9c73e4d6` | 60291 | 8/12/2014 | http 200 (attempt 1) |
| `pdf/2014-martin-luther-king-holiday-schedule__20140326160215.pdf` | **cited** | 20140326160215 | `5069a46a6acfb69bf05261abc23097fd675d159cf55e45361fb7e1e41dc0dcd4` | 138368 | 2/13/2014 | http 200 (attempt 1) |
| `pdf/2014-memorial-day-holiday-schedule__20140326153335.pdf` | earlier revision | 20140326153335 | `a438deab9cedf1df4cc8d4f4d86131ac1c25704ad74a86c93585f8096b2b4e28` | 117706 | 2/26/2014 | http 200 (attempt 1) |
| `pdf/2014-memorial-day-holiday-schedule__20140708020155.pdf` | **cited** | 20140708020155 | `a8e020149657b4e4730c2a357015d096a9fd47e2054ca59a85d6e6548ccb6023` | 60121 | 5/16/2014 | http 200 (attempt 1) |
| `pdf/2014-new-years__20121119021316.pdf` | earlier revision | 20121119021316 | `8f22d9eadd5b833bc8c0eb2b2be48d33eb1c27b0404a331fee2ce724967a1158` | 179725 | 11/12/2012 | http 200 (attempt 1) |
| `pdf/2014-new-years__20130309115333.pdf` | earlier revision | 20130309115333 | `4adcf2fdcc386ec5435bbc4455b19c9e01b625af65209eb2e21d71108118e41c` | 63644 | 1/4/2013 | http 200 (attempt 1) |
| `pdf/2014-new-years__20130623200646.pdf` | earlier revision | 20130623200646 | `419fd2b1fb952c2f0307436cdd3d36405227db2233595e674468d5bb911a307a` | 63917 | 5/2/2013 | http 200 (attempt 1) |
| `pdf/2014-new-years__20131007205800.pdf` | **cited** | 20131007205800 | `ca6da5edc26537d341b5148781c43c8ef00e33e832c8e602b97c57d6508b8f28` | 205983 | 10/4/2013 | http 200 (attempt 1) |
| `pdf/2014-presidents-day-holiday-schedule__20140214192332.pdf` | **cited** | 20140214192332 | `b689b4f8e9f62ba6f8c32bba46d35923a4017d1edbc83cc9ffcc2a85baded4fb` | 116612 | 2/13/2014 | http 200 (attempt 1) |
| `pdf/2014-thanksgiving-holiday-schedule__20140326153754.pdf` | earlier revision | 20140326153754 | `436214e8c3f9a4c38b639ffb2ab755c15f0e3d6691a7148a560bd0806e4b818c` | 120554 | 2/26/2014 | http 200 (attempt 1) |
| `pdf/2014-thanksgiving-holiday-schedule__20150121145456.pdf` | **cited** | 20150121145456 | `a90ae1f39414337f1a8600f55bf3a0a587214d987074885a47cfea307bc8054a` | 60428 | 11/18/2014 | http 200 (attempt 1) |
| `pdf/2014-veterans-day-holiday-schedule__20141113193450.pdf` | **cited** | 20141113193450 | `53ea2a8b03d8b71640a2a054eb1d4cc5dd220d4ebc0fd21f7f2890e21a55c2b6` | 97624 | — | http 200 (attempt 1) |
| `pdf/2015-4th-of-july-holiday-schedule__20141212013838.pdf` | earlier revision | 20141212013838 | `2c8831c207c60a421d3d1ae283632b77959198de83a07d16db4b4bc713abbaeb` | 55960 | 11/25/2014 | http 200 (attempt 1) |
| `pdf/2015-4th-of-july-holiday-schedule__20150326113353.pdf` | earlier revision | 20150326113353 | `664f4b885e090fccfe15152781ba62014aaa1650d1dfdf41564483d457d4ce2b` | 112477 | 12/29/2014 | http 200 (attempt 1) |
| `pdf/2015-4th-of-july-holiday-schedule__20150905222733.pdf` | **cited** | 20150905222733 | `1013e6ebea1829591946c9aa513ec6e3f99c64d99be14814610e601bb5dcc0fb` | 122744 | 6/1/2015 | http 200 (attempt 1) |
| `pdf/2015-christmas-holiday-schedule__20141212013852.pdf` | earlier revision | 20141212013852 | `318c37eb9ecf9cf456816a5f61a5ba38f343a2bb898d632f8fb62606cecde151` | 54830 | 12/9/2014 | http 200 (attempt 1) |
| `pdf/2015-christmas-holiday-schedule__20150326113907.pdf` | earlier revision | 20150326113907 | `6f053249db4527fbab27163e3e1d1a1331e8d8b0f4d6f38ca9584e202d52902c` | 108829 | 12/29/2014 | http 200 (attempt 1) |
| `pdf/2015-christmas-holiday-schedule__20150905223708.pdf` | earlier revision | 20150905223708 | `8a38717baac72c48b723b64e9fbe61582d2c3a386c06938ff5fc8399021efa03` | 112895 | 8/20/2015 | http 200 (attempt 1) |
| `pdf/2015-christmas-holiday-schedule__20151123061520.pdf` | **cited** | 20151123061520 | `7fde46210798f2cb4299903400b41ef6e2cb9aa287f8d3d360ba59d835b482ec` | 54852 | 10/27/2015 | http 200 (attempt 1) |
| `pdf/2015-good-friday-holiday-schedule__20141212013901.pdf` | earlier revision | 20141212013901 | `014d84cbab74f073adf4bf0c6ab973ea7a9e51831182c7886819f49325bc626b` | 122599 | 11/13/2014 | http 200 (attempt 1) |
| `pdf/2015-good-friday-holiday-schedule__20150326121904.pdf` | earlier revision | 20150326121904 | `bbd7439361cb71f9683f1960058d225e7dcd0002d2c273209183cd2c83594df1` | 54238 | 3/16/2015 | http 200 (attempt 1) |
| `pdf/2015-good-friday-holiday-schedule__20150905223230.pdf` | **cited** | 20150905223230 | `67873caa987c9eee8de38d02a5c18d8f7d46fd82a486bab34821f6e6f6363e0b` | 54240 | 3/31/2015 | http 200 (attempt 1) |
| `pdf/2015-labor-day-holiday-schedule__20150326113810.pdf` | earlier revision | 20150326113810 | `56d4554c99031fb8ba0fe3cb305e7900bb92e6fad6ecea7c43c23e230a079917` | 139294 | 11/13/2014 | http 200 (attempt 1) |
| `pdf/2015-labor-day-holiday-schedule__20150824023039.pdf` | **cited** | 20150824023039 | `4aab7fdb5e57420a243bbc26be6ecfa00a6317937afe3b772dfcdd8db1dd50fd` | 107305 | 7/20/2015 | http 200 (attempt 1) |
| `pdf/2015-martin-luther-king-holiday-schedule__20150121141012.pdf` | **cited** | 20150121141012 | `67395dcb63d86b6e1f573a5aa37269a685dfe1b17d23edd7d95449899bce090a` | 59439 | 1/7/2015 | http 200 (attempt 1) |
| `pdf/2015-memorial-day-holiday-schedule__20150326113938.pdf` | **cited** | 20150326113938 | `4ad4398fa092393fa77cd8ed9c58ecc0f1669a41fd38a9b4cab5b05790d2dfec` | 139573 | 11/13/2014 | http 200 (attempt 1) |
| `pdf/2015-new-years-holiday-schedule__20140326155048.pdf` | earlier revision | 20140326155048 | `8c161bd0f937cb2efa0a7caa17a91d99c2b09dafe1cbf0eca02733f39c7a3b54` | 119749 | 2/26/2014 | http 200 (attempt 1) |
| `pdf/2015-new-years-holiday-schedule__20150121141043.pdf` | **cited** | 20150121141043 | `196b4ec04bcfce2cfd9783262023afe9da73bcdef1b983c8c4b464b2e115bb8a` | 59206 | 10/7/2014 | http 200 (attempt 1) |
| `pdf/2015-presidents-day-holiday-schedule__20150121192401.pdf` | **cited** | 20150121192401 | `c81b04bcf43dbfd2b7c2f7aba559992cde8bb8eee59e7b310b643b636d290b94` | 60496 | 1/7/2015 | http 200 (attempt 1) |
| `pdf/2015-thanksgiving-holiday-schedule__20141212013936.pdf` | earlier revision | 20141212013936 | `f92e56dcf991f6a1c84b78e1d178e0ffebd1e3faa6bb291881e40ee6c3692d74` | 59841 | 11/17/2014 | http 200 (attempt 1) |
| `pdf/2015-thanksgiving-holiday-schedule__20150905222823.pdf` | earlier revision | 20150905222823 | `5919101744a777f5859b9fd896ca0d8a206955a1b07034fbfe62f7d9cddb1e13` | 117050 | 8/20/2015 | http 200 (attempt 1) |
| `pdf/2015-thanksgiving-holiday-schedule__20160205162519.pdf` | **cited** | 20160205162519 | `ef96d05289667c635f435884a0a2407bcbec63149ff96e802b719100c85c887f` | 60424 | 10/27/2015 | http 200 (attempt 1) |
| `pdf/2015-veterans-day-schedule__20151122230920.pdf` | **cited** | 20151122230920 | `50300dd36faff3b7d52128ea48a04e4c27012a78985b6c390ea9883e1696f98e` | 94646 | — | http 200 (attempt 1) |
| `pdf/2016-new-years-holiday-schedule__20141212034039.pdf` | earlier revision | 20141212034039 | `7d032ee5457cc5c06acb512e54006fa0678761e12d2b60bf625d924741896755` | 193907 | 11/13/2014 | http 200 (attempt 1) |
| `pdf/2016-new-years-holiday-schedule__20150326121913.pdf` | earlier revision | 20150326121913 | `4740dd708b418d47d07dbf8f155603b8f8a7d97091235e500290360215899e45` | 59260 | 1/8/2015 | http 200 (attempt 1) |
| `pdf/2016-new-years-holiday-schedule__20150905223456.pdf` | earlier revision | 20150905223456 | `0a0d98ef93343d9d4b316e322f95a434358ec8fcac094f993e24ea69d08e4b50` | 111525 | 8/20/2015 | http 200 (attempt 1) |
| `pdf/2016-new-years-holiday-schedule__20160108203007.pdf` | **cited** | 20160108203007 | `118196a469dd40ad6a40594da273f726f6cb3e503f9cc1b8fd2057cf2fa32c61` | 64156 | 12/16/2015 | http 200 (attempt 1) |
