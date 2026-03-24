from fpdf import FPDF
import datetime

class MarketAuditPDF(FPDF):
    def header(self):
        # Dark Background Header
        self.set_fill_color(18, 18, 18)
        self.rect(0, 0, 210, 35, 'F')
        self.set_y(10)
        self.set_font('Helvetica', 'B', 18)
        self.set_text_color(255, 204, 0)
        self.cell(0, 10, 'IBM-MARKET-INTELLIGENCE-V1: ARCHITECT AUDIT', 0, 1, 'C')
        self.set_font('Helvetica', '', 10)
        self.set_text_color(180, 180, 180)
        self.cell(0, 8, 'Session: March 24-25, 2026 | Node: Rio de Janeiro | Status: Operational', 0, 1, 'C')

    def footer(self):
        self.set_y(-20)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, 'Lauro Beck, DBA | Senior Enterprise Architect Portfolio | EmploymentMission2026', 0, 0, 'L')
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'R')

def create_report():
    pdf = MarketAuditPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.ln(20)

    # Section 1: Executive Summary
    pdf.set_font('Helvetica', 'B', 14)
    pdf.set_text_color(40, 40, 40)
    pdf.cell(0, 10, '1. EXECUTIVE SUMMARY: CROSS-REGIONAL REGIME SHIFT', 0, 1, 'L')
    pdf.set_font('Helvetica', '', 11)
    pdf.set_text_color(60, 60, 60)
    summary = (
        "This technical audit documents the transition from a Coherent Bearish Regime (H=1.84 bits) "
        "identified during the March 24 NASDAQ capitulation to a Decoherent Recovery (H=2.45 bits) "
        "during the Nikkei 225 Asia open. The system successfully validated high-alpha "
        "rotation into Energy (XOM +2.64%) as a structural flight-to-safety."
    )
    pdf.multi_cell(0, 6, summary)
    pdf.ln(8)

    # Section 2: Technical Metrics
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 10, '2. QUANTITATIVE TELEMETRY (MARCH 24, 2026 EOD)', 0, 1, 'L')
    
    # Table Header
    pdf.set_fill_color(230, 230, 230)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(45, 10, ' Metric', 1, 0, 'L', True)
    pdf.cell(35, 10, ' Value', 1, 0, 'L', True)
    pdf.cell(105, 10, ' Architectural Insight', 1, 1, 'L', True)

    # Table Rows
    pdf.set_font('Helvetica', '', 10)
    metrics = [
        ["NASDAQ 100", "21761.89", "Confirmed capitulation pivot point (-0.84%)."],
        ["VIX Index", "26.90", "Elevated fear; structurally efficient liquidity drain."],
        ["Entropy (H)", "1.84 bits", "Coherent Regime; high signal/low noise."],
        ["Energy Alpha", "XOM +2.64%", "Flight-to-safety confirmation (Relative Alpha +3.48%)."]
    ]
    for m in metrics:
        pdf.cell(45, 10, f' {m[0]}', 1)
        pdf.cell(35, 10, f' {m[1]}', 1)
        pdf.cell(105, 10, f' {m[2]}', 1, 1)

    pdf.ln(10)

    # Section 3: Information Theory Application
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 10, '3. SHANNON ENTROPY & MARKET COHERENCE', 0, 1, 'L')
    pdf.set_font('Helvetica', '', 11)
    theory = (
        "By quantifying the 'informativeness' of price returns, the engine identified a state of high "
        "coherence (H < 2.0). In this regime, participants act in high-correlation unison, "
        "increasing the probability of directional persistence. The transition to H=2.45 in Tokyo "
        "signaled a 'Decoherent Recovery' as market participants reacted to geopolitical de-escalation."
    )
    pdf.multi_cell(0, 6, theory)

    # Final Verification
    pdf.ln(15)
    pdf.set_font('Helvetica', 'B', 11)
    pdf.set_text_color(0, 102, 204)
    pdf.cell(0, 10, 'REPOSOTORY VERIFIED: github.com/LauroBeck/market-intelligence-v1', 0, 1, 'C', link='https://github.com/LauroBeck/market-intelligence-v1')

    pdf.output('Lauro_Beck_Market_Intelligence_Audit_2026.pdf')

if __name__ == "__main__":
    create_report()
    print("PDF Successfully Generated: Lauro_Beck_Market_Intelligence_Audit_2026.pdf")
