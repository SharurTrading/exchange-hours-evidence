# INDEX — artifacts retrieved by the ADVERSARIAL VERIFIER (round 3) for `cme-2016-2018`

Retrieved 2026-09-12 (UTC). cmegroup.com refuses this machine (403); every document below is the
Internet Archive's raw `id_` replay of the original cmegroup.com URL. Tier T1 throughout.

## Enumerations (fresh, unfiltered, taken this round)

| file | CDX query | notes |
|---|---|---|
| `cdx_2017_fresh.json` | `url=cmegroup.com/tools-information/holiday-calendar/files/2017*&collapse=digest` | 108 rows. Confirms 2017-holiday-calendars.zip has exactly one capture (2021-01-26T09:48:35Z) and that no 2017 per-file schedule has a 200 capture after 2017-10-25. |
| `cdx_2018_fresh_r3.json` | `url=cmegroup.com/tools-information/holiday-calendar/files/2018*` (no date filter) | 108 rows, set-identical to the round-1 verifier's `cme-2016-2018-fix/cdx_2018_fresh.json` (0 rows either way). Confirms no 2018 per-file schedule has a 200 capture after 2018-05-08 and that 2018-holiday-calendars.zip is captured only at 2026-08-30T10:02:25Z. |

A CDX probe of `cmegroup.com/CmeWS/mvc/Session/*` (CME's trading-hours service) returned an
empty result set: the Internet Archive holds no capture of that endpoint. Not load-bearing —
the dataset's `missing` list contains no 2019-or-later holiday.

## Re-fetched documents (byte comparison against the store)

| file | archive timestamp | sha256 | bytes | matches store |
|---|---|---|---|---|
| `refetch/2017-holiday-calendars.zip` | 20210126094835 | `f0dd1b522fc8ff8838861129a9a3966f874339f9a7bd9dd65c132616c0e1c1b2` | 491152 | yes |
| `refetch/2018-holiday-calendars.zip` | 20260830100225 | `aa0ac87005319be45d91d2a91fef907757dd8e5f0c6e3fb19875329940d9c5a2` | 940879 | yes |
| `refetch/2018-new-years--20170628.xls` | 20170628173831 | `b219cfdb1f2661efed139fc5849359bfd6f78c725d9ecd4e1a170bda8f25b15e` | 61440 | yes |
| `refetch/2018-new-years--20171025.xls` | 20171025111143 | `a05414192d7c8417ed03d4584d489f67bb03d96e838c4e5c808b5cefe5f401df` | 61952 | yes |
| `refetch/2017-christmas--20171025.xls` | 20171025104928 | `e75263b9fb837f0d679cd9ed8cc7f54dc18fa53930ef42e885ef237746b2ae3c` | 68096 | yes |
| `refetch/2017-4th-of-july--20171025.xls` | 20171025104918 | `3e87d972cc318bdbece668b0d213708d515d80519369afe56a021de43c29b1ce` | 93696 | yes |
| `refetch/2016-new-years--20160108.pdf` | 20160108203007 | `118196a469dd40ad6a40594da273f726f6cb3e503f9cc1b8fd2057cf2fa32c61` | 64156 | yes |
| `refetch/2016-holiday-calendars.zip` | 20170628115819 | `ce15abba12ee187796eb950570fec111f103e743ec2f67f4f3ed040ec64a8ad7` | 619386 | yes |

All 53 members of the two re-fetched bundles were re-extracted and hashed: 53/53 identical
to the copies in `raw/cme-2016-2018-fix/docs/zip2017` and `.../zip2018`.

All 108 sha256 rows of `raw/cme-2016-2018/INDEX.md` and all 59 of
`raw/cme-2016-2018-fix/INDEX.md` were recomputed: 167/167 match, 0 files missing,
0 files under either `docs/` tree absent from its INDEX.
