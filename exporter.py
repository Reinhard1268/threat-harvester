import csv
from fpdf import FPDF

def export_to_csv(data, filename="threat_report.csv"):
    with open(filename, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Type", "Value", "Threat", "Location", "Abuse Score"])
        for row in data:
            writer.writerow([
                row.get("type", "N/A"),
                row.get("value", "N/A"),
                row.get("threat", "N/A"),
                row.get("location", "N/A"),
                row.get("abuse_score", "N/A")
            ])

def export_to_pdf(data, filename="threat_report.pdf"):
    pdf = FPDF()
    pdf.set_font("Arial", size=10)
    pdf.add_page()
    pdf.cell(200, 10, txt="Threat Intelligence Report", ln=True, align="C")

    for row in data:
        for key, value in row.items():
            pdf.cell(200, 10, txt=f"{key.capitalize()}: {value}", ln=True)
        pdf.cell(200, 5, txt="-" * 50, ln=True)

    pdf.output(filename)
