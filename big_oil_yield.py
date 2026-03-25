import pandas as pd
import matplotlib.pyplot as plt

def audit_energy_yields():
    print("\033[1;36m[AUDIT] 2026 BIG-OIL & JPM DIVIDEND STRATEGY\033[0m")
    
    # Live 2026 March Data & Dividend Projections
    data = {
        'Asset': ['Chevron (CVX)', 'Exxon (XOM)', 'Shell', 'Conoco (COP)', 'Aramco', 'Halliburton', 'JPM'],
        'Price': [205.31, 122.45, 72.10, 115.80, 8.50, 42.15, 198.40],
        'Div_Yield (%)': [4.1, 3.8, 3.9, 3.5, 4.5, 2.8, 2.4]
    }

    df = pd.DataFrame(data)
    df['Quarterly_Payout'] = (df['Price'] * (df['Div_Yield (%)'] / 100)) / 4

    # Visualizing the Yield Landscape
    plt.figure(figsize=(12, 6), facecolor='black')
    plt.style.use('dark_background')
    
    colors = ['#FFD700' if x == 'Aramco' else '#00FF00' for x in df['Asset']]
    plt.bar(df['Asset'], df['Div_Yield (%)'], color=colors, alpha=0.8)
    
    plt.title("Lauro Beck, DBA | BigOil & JPM Dividend Yield Audit", color='#BC8CF2', fontsize=16)
    plt.ylabel("Annual Yield (%)")
    plt.grid(axis='y', alpha=0.2)

    filename = 'Energy_Dividend_Audit.png'
    plt.savefig(filename, facecolor='black')
    print(df[['Asset', 'Price', 'Div_Yield (%)', 'Quarterly_Payout']])
    print(f"\n\033[1;32m[SUCCESS]\033[0m Yield Map Saved: {filename}")

if __name__ == "__main__":
    audit_energy_yields()
