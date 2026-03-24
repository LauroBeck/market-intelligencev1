import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import os

def generate_dashboard():
    os.makedirs('docs/images', exist_ok=True)
    fig = plt.figure(figsize=(16, 9), dpi=100, facecolor='#111111')
    gs = gridspec.GridSpec(2, 3, figure=fig, height_ratios=[1.5, 1], width_ratios=[1.5, 1, 1])

    # Panel 1: Macro Metrics
    ax1 = fig.add_subplot(gs[0, 0], facecolor='#181818')
    data = [("NASDAQ 100", 21759.22, -0.85), ("VIX INDEX", 26.90, 2.87), ("2YR YIELD", 3.92, 0.07)]
    ax1.set_title("INTRA-SESSION TELEMETRY", color='orange', fontsize=14)
    for i, (label, val, pct) in enumerate(data):
        ax1.text(0.1, 0.8 - i*0.2, f"{label}: {val}", color='white', fontsize=12, transform=ax1.transAxes)
    ax1.axis('off')

    # Panel 2: Trend Projection
    ax2 = fig.add_subplot(gs[0, 1:], facecolor='#181818')
    ax2.plot(np.linspace(0, 10, 50), 38500 - (np.linspace(0, 10, 50)**2), color='cyan')
    ax2.set_title("NIKKEI 225 PROJECTION (COHERENT REGIME)", color='orange')

    output_path = 'docs/images/EOD_Market_Dashboard.png'
    plt.savefig(output_path, facecolor=fig.get_facecolor())
    print(f"Successfully generated: {output_path}")

if __name__ == "__main__":
    generate_dashboard()
