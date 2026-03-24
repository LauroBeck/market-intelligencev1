import sqlite3
import pandas as pd

def get_session_summary(date):
    conn = sqlite3.connect('market_intel.db')
    query = f"SELECT * FROM market_regimes WHERE session_date = '{date}'"
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    if not df.empty:
        print(f"\n--- ARCHITECT AUDIT: {date} ---")
        print(df.to_string(index=False))
        print(f"\nINTELLIGENCE: The {df['regime_label'][0]} regime is verified by H={df['entropy_bits'][0]} bits.")
    else:
        print("No telemetry found for this session.")

if __name__ == "__main__":
    get_session_summary('2026-03-24')
