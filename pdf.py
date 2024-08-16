from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv", sep=",")
# print(df)
pdf = FPDF(orientation="P", unit="mm", format="A4")
# pdf.add_page()
pdf.set_font(family="Times",style="B",size=24)
pdf.set_text_color(100,100,100)
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], border=0, ln=1, align="L", )
    # pdf.line(x1=10,y1=20,x2=200,y2=20)
    pdf.ln(242)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(130, 130, 130)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="R", )
    for y in range(20,290,12):
        pdf.line(x1=10,y1=y,x2=200,y2=y)
    for i in range(row['Pages'] - 1):
        pdf.add_page()
        pdf.ln(254)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(130, 130, 130)
        pdf.cell(w=0, h=12, txt=row['Topic'], align="R", )
        for y in range(20, 290, 12):
            pdf.line(x1=10, y1=y, x2=200, y2=y)

pdf.output("output.pdf")
