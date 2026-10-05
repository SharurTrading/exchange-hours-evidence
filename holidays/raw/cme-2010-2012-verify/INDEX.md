# INDEX — cme-2010-2012.verify (adversarial re-verification)

Verifier task: cme-2010-2012.verify. All retrieval performed 2026-09-12 (UTC) from this machine.
cmegroup.com 403s directly; every document below was re-fetched independently from the Internet Archive with `id_` raw replay:
`https://web.archive.org/web/<wayback_timestamp>id_/<original_url>`. Tier T1 (CME Group's own holiday-calendar documents).

## Independently re-fetched documents (compared byte-for-byte against raw/cme-2010-2012/docs/)

| file | wayback capture (UTC) | bytes | sha256 | matches target task |
|---|---|---|---|---|
| refetch/2010-good-friday.pdf | 2010-06-01T11:19:16Z | 44125 | d196ca746c20ecd416d38f8f95020e2e7d6cb7fa9ead089e0d58c88bed0ab1f5 | YES |
| refetch/2010-new-years.pdf | 2010-02-15T05:16:52Z | 41934 | c30a6cef73fca23c54b25907f307ad52a2922d1e4b76c0a12de126dc6fc31a6d | YES |
| refetch/2010-presidents-day.pdf | 2010-02-15T06:46:41Z | 49335 | ba379a7fa57efef43820583ada0002ea6cd8ccf0caf1b650d1cb6e8561f84253 | YES |
| refetch/2010-thanksgiving.pdf | 2010-11-22T09:40:12Z | 97946 | 4732afab4ca78ce21b3640f8ac41ced714123179c7cee1cb2b8c044bf9f2e2b5 | YES |
| refetch/2011-christmas.pdf | 2012-01-25T02:05:48Z | 108183 | a0d34878fd70534afb2e0a2585a04ce1efc8c4aa0451575266cfb5f9dcf08029 | YES |
| refetch/2011-good-friday.pdf | 2011-10-28T02:37:07Z | 107634 | 6cf10359bb438eb49287dcef7c1e75a484df4d6e3b538fa9ee59dc3832210bda | YES |
| refetch/2011-memorial-day.pdf | 2013-09-30T10:56:52Z | 66172 | 5482f7bf47e0ee61448cf5f60fd4a5373cc39cb0e46220150c1f6a2ab2d6caec | YES |
| refetch/2011-new-years.pdf | 2011-11-01T14:39:45Z | 125412 | 42c289804cd3fa0830556ecb7fcc31493c452ba9e7325ebe7d7ce29613e41476 | YES |
| refetch/2012-christmas.pdf | 2013-04-14T19:40:27Z | 125821 | de3b16aaae2ef887e46c965f902d8d0e43afa6e18dc1f721baaa40ea6b18b5e9 | YES |
| refetch/2012-thanksgiving.pdf | 2013-01-27T22:39:01Z | 73205 | 052e381bbd4eb0790c6d38e3866874738d6da081da62643e525c25674b2608e1 | YES |
| refetch/2013-new-years.pdf | 2012-09-15T00:32:25Z | 55474 | d1056fbd7e0572dcd712c10deac353f2eeb586fe5e2db7af023e6a88d95556be | YES |
| gf2012_canon.pdf (2012-good-friday.pdf, CANONICAL url, not the ?-variant) | 2012-05-05T16:16:49Z | 60600 | 81440c44afb97ea4b3a44b86aa4cf21e2e4cb7ba5839fabd95b29d0c928b2ea8 | YES |

## Other artifacts

| file | what it is |
|---|---|
| cdx_hc.json | fresh CDX prefix enumeration `https://web.archive.org/cdx/search/cdx?url=cmegroup.com/tools-information/holiday-calendar*&output=json&fl=timestamp,original,statuscode,mimetype,digest,length&from=2009&to=2014` retrieved 2026-09-12T04:5xZ; 608 rows, 248 distinct originals; sha256 0f8ee34cd0b2f86e6c74120c29156819f5a72567e1d92d287e1fa995e1be68df — byte- and hash-identical to the target task's saved cdx_holiday_calendar_2009_2014.json |
| txt/*.txt | my own `pdftotext -layout` extraction of all 36 PDFs in raw/cme-2010-2012/docs/, made independently of the target task's txt/ |
| refetch/*.txt | `pdftotext -layout` of the re-fetched PDFs |

## Negative CDX results (both confirmed)

- `https://web.archive.org/cdx/search/cdx?url=cmegroup.com/trading-hours*&output=json&fl=timestamp,original,statuscode&from=2009&to=2014` → `[]`
- `https://web.archive.org/cdx/search/cdx?url=cmegroup.com/content/dam/cmegroup/tools-information/holiday-calendar/*&output=json&fl=timestamp,original,statuscode&from=2009&to=2014` → `[]`
