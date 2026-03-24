import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Set visual style
plt.style.use('dark_background')

COLORS = {
    'Index': '#FFFFFF',
    'Energy': '#66CC66',
    'Crypto': '#FF4444',
    'Consumer': '#CC3333',
    'Highlight': '#FFCC00'
}

def generate_divergence_alpha_chart():
    if not os.path.exists('toolkit/data/market_telemetry.csv'):
        print("Error: telemetry file missing.")
        return
        
    df = pd.read_csv('toolkit/data/market_telemetry.csv')
    nasdaq_perf = df.loc[df['Ticker'] == '^IXIC', 'Pct_Change'].values[0]
    df['Relative_Alpha'] = df['Pct_Change'] - nasdaq_perf
    df = df.sort_values(by='Relative_Alpha', ascending=True)
    
    # Corrected Figure Initialization
    fig, ax = plt.subplots(figsize=(12, 8), dpi=100)
    ax.set_facecolor('#111111')

    bar_colors = [COLORS.get(sector, '#888888') for sector in df['Sector']]
    bars = ax.barh(df['Ticker'], df['Relative_Alpha'], color=bar_colors, edgecolor='#181818')

    ax.set_xlabel('RELATIVE ALPHA vs. NASDAQ BENCHMARK (%)', fontsize=12)
    ax.set_title('MAR 24, 2026: SECTOR DIVERGENCE (FLIGHT-TO-SAFETY)', color=COLORS['Highlight'], fontsize=16)

    for bar in bars:
        width = bar.get_width()
        ax.text(width + (0.1 if width > 0 else -1.2), bar.get_y() + bar.get_height()/2, 
                f'{width:+.2f}%', va='center', fontweight='bold')

    plt.tight_layout()
    plt.savefig('docs/images/Mar24_Divergence_Alpha.png')
    plt.close()

def generate_regime_heatmap():
    df = pd.read_csv('toolkit/data/market_telemetry.csv')
    
    fig, ax = plt.subplots(figsize=(10, 8), dpi=100)
    ax.set_facecolor('#111111')

    ax.scatter(df['VIX'], df['H_Entropy'], s=300, c='#FFCC00', marker='D', edgecolor='black')

    for i, txt in enumerate(df['Ticker']):
        ax.annotate(txt, (df['VIX'][i] + 0.05, df['H_Entropy'][i] + 0.02), color='white')

    ax.set_title('MAR 24, 2026: REGIME COHERENCE (VIX vs. ENTROPY)', color=COLORS['Highlight'], fontsize=16)
    ax.set_xlabel('VIX INDEX')
    ax.set_ylabel('SESSION ENTROPY (bits)')
    ax.axhline(2.0, color='#666666', linestyle='--')

    plt.tight_layout()
    plt.savefig('docs/images/Mar24_Regime_Coherence.png')
    plt.close()

if __name__ == "__main__":
    os.makedirs('docs/images', exist_ok=True)
    generate_divergence_alpha_chart()
    generate_regime_heatmap()
    print("Audit Visuals Re-Generated Successfully.")
