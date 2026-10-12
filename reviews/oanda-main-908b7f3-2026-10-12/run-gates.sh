set -e
export CARGO_PROFILE_TEST_OPT_LEVEL=1 EXCHANGE_HOURS_RESEARCH=/tmp/oanda-current-evidence-frozen
cargo fmt --all --check
cargo clippy --all-targets -- -D warnings
cargo nextest run --all-targets
cargo test --doc
RUSTDOCFLAGS='-D warnings' cargo doc --no-deps
cargo deny check
cargo +1.95 check --all-targets
cargo xtask verify-evidence EURONEXT-CASH-CALENDAR-CURRENT-2026-10-12
