import matplotlib.pyplot as plt
import os

def create_dashboard():
    # Live Bloomberg data point from your verification
    sp500_live = 6612.59
    resistance = 6620.00
    is_breakout = sp500_live >= resistance

    print(f"\033[1;33m[AUDIT] S&P 500: {sp500_live} | Resistance: {resistance}\033[0m")
    
    fig = plt.figure(figsize=(12, 7), facecolor='black')
    ax = fig.add_subplot(111)
    plt.style.use('dark_background')

    if is_breakout:
        status_color = '#00FF00' # Green for Breakout
        status_text = "STATUS: BREAKOUT CONFIRMED"
    else:
        status_color = '#FFFF00' # Yellow for Impending
        status_text = f"STATUS: APPROACHING RESISTANCE (Gap: {resistance - sp500_live:.2f} pts)"

    # Visualizing the Alert
    plt.text(0.5, 0.7, "S&P 500 MARKET AUDIT", color='white', ha='center', fontsize=20)
    plt.text(0.5, 0.5, f"{sp500_live}", color=status_color, ha='center', fontsize=45, fontweight='bold')
    plt.text(0.5, 0.3, status_text, color=status_color, ha='center', fontsize=15)
    
    plt.title("Lauro Beck, DBA | Executive Breakout Monitor", color='#BC8CF2', pad=20)
    plt.axis('off')

    filename = 'Market_Breakout_Alert.png'
    plt.savefig(filename, facecolor='black')
    print(f"\033[1;32m[SAVED]\033[0m Alert Dashboard: {os.getcwd()}/{filename}")

if __name__ == "__main__":
    create_dashboard()
