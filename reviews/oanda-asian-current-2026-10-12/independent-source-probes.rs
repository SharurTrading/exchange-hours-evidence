// SPDX-License-Identifier: MIT-0
//! Independent source-derived candle, gap and publication-edge witnesses.
#![allow(clippy::expect_used)]
use chrono::{DateTime,NaiveDate,Utc};
use exchange_hours::{CalendarQueryError,CalendarResolution,DateCoverage,SessionKind,ExchangeCalendar,MarketHoursKey as K,SessionState};
fn utc(s:&str)->DateTime<Utc>{s.parse().expect("UTC witness")}
#[test]
fn source_derived_periods_and_publication_edges() {
 for (key,night,day_end,week_end,gap) in [
 (K::OandaChina50Cfd,"2026-10-12T09:01:00Z","2026-10-13T08:29:00Z","2026-10-16T20:44:00Z","2026-10-12T08:40:00Z"),
 (K::OandaSingapore30Cfd,"2026-10-12T09:51:00Z","2026-10-13T09:19:00Z","2026-10-16T21:14:00Z","2026-10-12T09:30:00Z")]{
 let c=ExchangeCalendar::for_market_hours_key(key);
 assert_eq!(c.candle_end(utc(night),CalendarResolution::Daily),Ok(Some(utc(day_end))));
 assert_eq!(c.candle_end(utc(night),CalendarResolution::Weekly),Ok(Some(utc(week_end))));
 assert_eq!(c.session_state(utc(gap)),Ok(SessionState::Maintenance));
 assert_eq!(c.session_state(utc("2026-10-12T23:30:00Z")),Ok(SessionState::Closed));
 let tail=utc("2026-10-30T10:00:00Z");
 assert_eq!(c.is_open(tail),Ok(true));
 assert!(matches!(c.session_bounds(tail),Ok(Some((_,_)))));
 assert!(matches!(c.trade_date(tail),Err(CalendarQueryError::OutsideCoveredRange{..})));
 let outside=NaiveDate::from_ymd_opt(2026,10,31).expect("date");
 assert_eq!(c.coverage().coverage_on(outside),DateCoverage::OutsideCoveredRange);
 assert!(matches!(c.is_closed_trade_date(outside,SessionKind::Both),Err(CalendarQueryError::OutsideCoveredRange{..})));
 assert!(matches!(c.candle_end(tail,CalendarResolution::Daily),Err(CalendarQueryError::OutsideCoveredRange{..})));
 for t in ["2026-10-30T18:00:00Z","2026-10-30T23:00:00Z","2026-10-31T10:00:00Z","2026-11-02T02:00:00Z"] {
 assert!(matches!(c.is_open(utc(t)),Err(CalendarQueryError::OutsideCoveredRange{..})));
 }
 assert!(matches!(c.candle_end(utc(night),CalendarResolution::Monthly),Err(CalendarQueryError::OutsideCoveredRange{..})));

 }
}
