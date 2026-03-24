-- market-intelligencev1 Database Schema
CREATE TABLE IF NOT EXISTS market_regimes (
    session_date DATE PRIMARY KEY,
    nasdaq_close DECIMAL(12, 2),
    entropy_bits DECIMAL(4, 2),
    vix_value DECIMAL(5, 2),
    alpha_ticker VARCHAR(10),
    regime_label VARCHAR(50)
);

-- Record the March 24th Pivot (NASDAQ 21761.89 | 1.84 Bits)
INSERT OR REPLACE INTO market_regimes VALUES ('2026-03-24', 21761.89, 1.84, 26.90, 'XOM', 'Coherent Bearish');
