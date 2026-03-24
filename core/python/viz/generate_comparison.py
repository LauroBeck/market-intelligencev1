import matplotlib.pyplot as plt
import os

os.makedirs('docs/images', exist_ok=True)

# Comparison Data (Session Transition)
dates = ['Mar 24 (NY)', 'Mar 25 (Tokyo)']
entropy_values = [1.84, 2.45]
regimes = ['Coherent Bearish', 'Decoherent Recovery']
colors = ['#FF4444', '#44AAFF']

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
ax.set_facecolor('#111111')

# Bar Plot
bars = ax.bar(dates, entropy_values, color=colors, edgecolor='white', width=0.5)

# Coherence Threshold Line (Shannon Logic)
ax.axhline(2.0, color='#666666', linestyle='--', label='Coherence Threshold (2.0)')

# Labels and Aesthetics
ax.set_ylabel('ENTROPY BITS (H)', fontsize=12)
ax.set_title('REGIME TRANSITION: MAR 24 VS MAR 25', fontsize=16, color='#FFCC00', pad=20)
ax.set_ylim(0, 3.5)

# Annotate Bars with Regime Labels
for bar, regime in zip(bars, regimes):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
            f'{height} bits\n({regime})',
            ha='center', va='bottom', fontweight='bold', color='white')

ax.legend(facecolor='#181818', edgecolor='#333333')
plt.tight_layout()
plt.savefig('docs/images/Regime_Comparison.png', facecolor='#111111')
print("Successfully Generated: docs/images/Regime_Comparison.png")
