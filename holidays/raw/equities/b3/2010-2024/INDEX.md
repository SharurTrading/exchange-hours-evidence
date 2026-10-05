# INDEX — b3-2010-2024 (B3 / BM&FBOVESPA holiday calendars, trade years 2011-2024)

Task: phase2 backfill of the `b3` built-in holiday table for 2010-2024.
Retrieval performed 2026-09-29 (UTC) from this machine; every pre-2025 artifact
was read from the Internet Archive with `id_` raw replay
(`https://web.archive.org/web/<capture>id_/<original_url>`), except the two
live PDFs noted below. The Wayback capture stamp dates the observation, not the
state; each announcement page carries the operator's own publication date in
its text (quoted in `docs/evidence/b3.md`). Tier: T1 throughout — the
operator's own news articles, calendar pages and circulars.

Per-row derivations live in the repository's `docs/evidence/b3.md`. Digests
below are the cells the evidence file's `### Documents` table cites.

| file | original URL | wayback capture (UTC) | sha256 | what it is |
|---|---|---|---|---|
| wayback_20101113014923_bmf_noticia_calendario_2011.html | <http://www.bmfbovespa.com.br/pt-br/noticias/2010/Confira-o-calendario-de-feriados-do-mercado-para-2011-2010-11-05.aspx?idioma=pt-br> | 20101113014923 | `15ef6b0d1a170938f2a068021595ca92e96e76426770b55823f908de9cc1e671` | `B3-NEWS-CAL-2011` — the 2011 calendar announcement (published 2010-11-05) |
| wayback_20111202101657_bmf_noticia_calendario_2012.html | <http://www.bmfbovespa.com.br/pt-br/noticias/2011/BMFBOVESPA-divulga-o-calendario-do-mercado-2012-2011-11-29.aspx?tipoNoticia=1&idioma=pt-br> | 20111202101657 | `ea57acfdac300b222d3dee92480378d237ede62c2ffd1f5fa02b3992941d812c` | `B3-NEWS-CAL-2012` — the 2012 calendar announcement (published 2011-11-29) |
| wayback_20120428002450_bmf_calendario_2012.html | <http://www.bmfbovespa.com.br/pt-br/regulacao/calendario-do-mercado/calendario2012/calendario-do-mercado.aspx?idioma=pt-br> | 20120428002450 | `8d31d6a44736ed24ab6a4f752613dead03c70c5595a077ea34096fb623704969` | `B3-REG-CAL-2012` — the operator's 2012 market-calendar page (corroboration) |
| wayback_20131216105739_bmf_noticia_calendario_2013.html | <http://www.bmfbovespa.com.br/pt-br/noticias/2012/BMFBOVESPA-divulga-o-calendario-do-mercado-2013-2012-12-07.aspx?idioma=pt-br> | 20131216105739 | `35a98e4875e1192af5b8ca9708f88929bd24411544a5a1989d0c7bdc51ae9944` | `B3-NEWS-CAL-2013` — the 2013 calendar announcement (published 2012-12-07) |
| wayback_20130216100707_bmf_calendario_do_mercado.html | <http://www.bmfbovespa.com.br/pt-br/regulacao/calendario-do-mercado/calendario-do-mercado.aspx?WT.ac=PT_FullBanner-Horario-Carnaval&idioma=pt-br> | 20130216100707 | `27a1f72c6e4d0e328ec84ea3762b54626c4a2e9f1665fcaa9086ac7fbae9a06a` | `B3-REG-CAL-2013` — the operator's 2013 market-calendar page (key artifact) |
| wayback_20140209120013_bmf_calendario_do_mercado.html | <http://www.bmfbovespa.com.br/pt-br/regulacao/calendario-do-mercado/calendario-do-mercado.aspx?idioma=pt-br> | 20140209120013 | `e1b8c76eb2a0988a772047a82c1e3769b7b49e73ee93004004a4c059148f45e4` | `B3-REG-CAL-2014-FEB` — the operator's 2014 market-calendar page, February capture |
| wayback_20140326075704_bmf_calendario_do_mercado.html | <http://www.bmfbovespa.com.br/pt-br/regulacao/calendario-do-mercado/calendario-do-mercado.aspx?idioma=pt-br> | 20140326075704 | `919afff9cd22c85f891f3db9d9f538612b8a74beab134502757b7d3699f3a00c` | `B3-REG-CAL-2014-MAR` — the same page, March capture (summary block with the 04 March icon) |
| wayback_20140303224541_bmf_noticia_cinzas_2014.html | <http://www.bmfbovespa.com.br/pt-br/noticias/2014/Horarios-de-Negociacao-em-05-03-2014-Quarta-Feira-de-Cinzas-2014-02-27.aspx?idioma=pt-br> | 20140303224541 | `6a457ec72c84498f25277a3e722e6f4b14d217f1066f34f4429066d62fb4b2f4` | `B3-NEWS-CINZAS-2014` — the 05 March 2014 Ash Wednesday hours notice (published 2014-02-27) |
| wayback_20141123090025_bmf_noticia_calendario_2015.html | <http://www.bmfbovespa.com.br/pt-br/noticias/2014/BMFBOVESPA-divulga-calendario-de-feriados-de-2015-2014-11-19.aspx?idioma=pt-br> | 20141123090025 | `725ee4b9cf7bc04ccc1f8f038724f7f04d0ea38c26c532327ddcbcb0effa0394` | `B3-NEWS-CAL-2015` — the 2015 calendar announcement (published 2014-11-19) |
| wayback_20150410045304_bmf_noticia_cinzas_2015.html | <http://www.bmfbovespa.com.br/pt-br/noticias/2015/Horarios-de-Negociacao-em-18022015-Quarta-Feira-de-Cinzas-2015-02-04.aspx?idioma=pt-br> | 20150410045304 | `b74c0a8b0639de89416c2250cbdf1ad94d95d05e3f058e27a4cbe6b95e94daac` | `B3-NEWS-CINZAS-2015` — the 18 February 2015 Ash Wednesday hours notice |
| wayback_20160411112845_bmf_noticia_calendario_de_feriados.html | <http://www.bmfbovespa.com.br/pt_br/noticias/calendario-de-feriados.htm> | 20160411112845 | `c8b185ad24045fd600228c168b365d13d26ec7e6f002d589705152a99a99bc21` | `B3-NEWS-CAL-2016` — the 2016 calendar announcement article (published 2015-12-09) |
| wayback_20160414070538_b3_puma_feriados.html | <http://www.bmfbovespa.com.br/pt_br/servicos/negociacao/puma-trading-system-bm-fbovespa/para-participantes-e-traders/calendario-de-negociacao/feriados/> | 20160414070538 | `6fb35ccc8a85d963e2de746b40f09d297497b78f2c75fd23f9968c889b0ff69b` | `B3-PUMA-FER-2016` — the PUMA trading-calendar Feriados page printing 2016 |
| wayback_20170201175439_b3_puma_feriados.html | (same old-domain URL) | 20170201175439 | `6180ca7070789ff471128260105cde8790e46bb5a405d9f2f69e5f7739527d00` | `B3-PUMA-FER-2017` — the same page printing 2017 |
| wayback_20180106170521_b3_puma_feriados.html | (same old-domain URL) | 20180106170521 | `51bf14fc7e72222c9949b10545d738f828d98a6caa88ed8c62dfb3848a8dd87e` | `B3-PUMA-FER-2018` — the same page printing 2018 |
| wayback_20181224025230_b3_puma_feriados.html | <https://www.b3.com.br/pt_br/solucoes/plataformas/puma-trading-system/para-participantes-e-traders/calendario-de-negociacao/feriados/> | 20181224025230 | `0ae67912b50e640d216f2dab85e622fc8d7e2a7c860112c3c82f058506efe05d` | `B3-PUMA-FER-2018-DEC` — the new-domain page, 24 December 2018 capture (December table) |
| wayback_20190102062220_b3_puma_feriados.html | (new-domain URL) | 20190102062220 | `120f145b422cc39339c30559d2d759a0b792f63f61276fc070c592f48031d143` | `B3-PUMA-FER-2019` — the page printing 2019 |
| wayback_20200128192203_b3_puma_feriados.html | (new-domain URL) | 20200128192203 | `dcc511d0e12a76e18221386fb2cf7df865139ec69eb9e43a757e51cb9fe132ce` | `B3-PUMA-FER-2020` — the page printing 2020 |
| wayback_20240227205223_b3_puma_feriados.html | (new-domain URL) | 20240227205223 | `ac7ab61b20699de9bd9e2f322735608bd94989f9e8ff20ff31e97429db302330` | `B3-PUMA-FER-2021-2024` — the page embedding the 2021, 2022, 2023 and 2024 calendars |
| live_OC_062-2009DP.pdf | <https://www.b3.com.br/data/files/5F/52/26/49/AF0B25107399EA25790D8AA8/062-2009DP.pdf> | live retrieval | `17e358fe9a83e12dcfe2667bb69ec376084ef1854efad5ec9ed5e92c5fb0d619` | OC 062/2009-DP (2009-10-06) — trading-hours circular, no holiday list; kept as the 2010-gap probe record |

Not saved (no holiday content): `wayback_20091119230303` and
`wayback_20100102053721` captures of the 2009-2010 `calendario-do-mercado`
page (wallpaper-download widget), the 2010-08-02 derivatives
`calendario-de-feriados.aspx` capture (same widget), the 2021-01-30,
2022-03-06 and 2023-05-06 captures of the new-domain PUMA page (stale default
year superseded by `B3-PUMA-FER-2021-2024`, which embeds all four years).

## 2010 — recorded gap

No operator artifact stating the 2010 holiday arrangement was found. Searched
2026-09-29 UTC: CDX over `bmfbovespa.com.br` (domain, `feriado`/`calendario`
filters), the `pt-br/noticias/2009/` and `pt-br/noticias/2010/` prefixes (the
2011 announcement of 2010-11-05 is the only calendar article captured), the
2009-2010 `calendario-do-mercado.aspx` captures (wallpaper widget, no table),
the 2010-08-02 derivatives feriados page (same widget), the old
`bovespa.com.br` domain (holiday pages stop at 2003), and OC 062/2009-DP (the
January-2010 hours circular; image-only PDF, 6 pages, no holiday list — page
images read visually). **Closing condition:** a capture of the operator's
"Calendário do mercado 2010" announcement or of the 2010 holiday Ofício
Circular; the backfill window for `b3` therefore starts at 2011-01-01.
