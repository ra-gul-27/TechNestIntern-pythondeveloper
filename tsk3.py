import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
df = pd.read_csv("data.csv")
summary = df.describe()

num_cols = df.select_dtypes(include='number').columns
if not num_cols.empty:
    col = num_cols[0]
    plt.figure(figsize=(6, 4))
    plt.hist(df[col].dropna(), bins=10, color='skyblue', edgecolor='black')
    plt.title(f'{col} Distribution')
    plt.xlabel(col)               
    plt.ylabel('Frequency')     
    plt.tight_layout()
    plt.savefig('plot.png')
    plt.close()
else:
    col = None

# Step 4: Create PDF report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "Data Report", ln=True, align='C')

pdf.set_font("Arial", size=11)
pdf.ln(10)
pdf.cell(0, 10, "Summary Stats:", ln=True)

for c in summary.columns:
    stats = summary[c]
    pdf.cell(0, 10, f"{c} -> Mean: {stats['mean']:.2f}, Min: {stats['min']:.2f}, Max: {stats['max']:.2f}", ln=True)

if col:
    pdf.ln(10)
    pdf.cell(0, 10, f"{col} Histogram:", ln=True)
    pdf.image('plot.png', x=30, w=150)

pdf.output("report.pdf")
print(" PDF report saved as 'report.pdf'")
