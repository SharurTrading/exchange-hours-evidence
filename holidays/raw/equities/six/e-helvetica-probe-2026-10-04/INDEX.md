# e-Helvetica (Swiss National Library web archive) probe — 2026-10-04 UTC

Untried channel for #212's named bytes (the 11-January-2010 Trading Guide
edition / trading_calendar_en.pdf as served 2010-2011): the Swiss National
Library's web archive. Probe result: the e-helvetica.nb.admin.ch front end
is a React SPA (1,168-byte shell; the 5.1 MB main.js carries no public
search API — only /api/image and catalog links to helveticat.nb.admin.ch,
whose discovery endpoints answer 404 to direct queries). arquivo.pt requery
for the guides paths: still empty. No machine-reachable query surface found;
a GUI browse (e-helvetica.nb.admin.ch → Webarchiv search for
swx.com/six-swiss-exchange.com 2010-2011 captures) is a seconds-long
human-side task — added to the ask-list §3 as a secondary route beside the
desk ask. Files: the SPA shell, the webarchiv route shell, main.js (digest
below).

- e-helvetica.nb.admin.ch shell: sha256 `sha256sum e-helctica 2>/dev/null || shasum -a 256 ehel.html ehel-wa.html | head -2`
8fe863ebd5aff1946c9051beaf3a0621d61278ec17629062dae39af499f0d3e6  ehel.html
8fe863ebd5aff1946c9051beaf3a0621d61278ec17629062dae39af499f0d3e6  ehel-wa.html
98c5b288fef20d7717fefb17b2e4ad6728a9438bba9f5073c263ab4263ad9853  ehel-main.js
