from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image,
    PageBreak, Table, TableStyle
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
import os

# --------------------------------------------------
# Paths
# --------------------------------------------------

BASE = os.path.expanduser("~/Sales-Performance-Forecasting")
OUTPUT = os.path.join(BASE, "report", "Sales_Performance_Forecasting_Report.pdf")
CHARTS = os.path.join(BASE, "outputs")

# --------------------------------------------------
# PDF setup
# --------------------------------------------------

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    rightMargin=45,
    leftMargin=45,
    topMargin=45,
    bottomMargin=45
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "TitleCustom",
    parent=styles["Title"],
    alignment=TA_CENTER,
    fontSize=22,
    leading=27,
    spaceAfter=15
)

subtitle_style = ParagraphStyle(
    "Subtitle",
    parent=styles["Normal"],
    alignment=TA_CENTER,
    fontSize=12,
    leading=18,
    spaceAfter=25
)

heading_style = ParagraphStyle(
    "HeadingCustom",
    parent=styles["Heading1"],
    fontSize=16,
    leading=20,
    spaceBefore=12,
    spaceAfter=10
)

body_style = ParagraphStyle(
    "BodyCustom",
    parent=styles["BodyText"],
    fontSize=10.5,
    leading=16,
    spaceAfter=8
)

caption_style = ParagraphStyle(
    "Caption",
    parent=styles["Normal"],
    alignment=TA_CENTER,
    fontSize=9,
    leading=12,
    spaceAfter=15
)

# --------------------------------------------------
# Story
# --------------------------------------------------

story = []

# Cover
story.append(Spacer(1, 1.2 * inch))
story.append(Paragraph(
    "Sales Performance & Forecasting Analysis",
    title_style
))
story.append(Paragraph(
    "Python & Data Science Internship Assessment",
    subtitle_style
))

story.append(Paragraph(
    "<b>Project Objective</b><br/>"
    "This project performs an end-to-end analysis of the Superstore retail "
    "sales dataset. The analysis covers data cleaning, exploratory data "
    "analysis, statistical analysis, and machine-learning-based sales "
    "forecasting.",
    body_style
))

story.append(Spacer(1, 20))
story.append(Paragraph(
    "<b>Technologies Used</b><br/>"
    "Python 3, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn and Jupyter Notebook.",
    body_style
))

story.append(Paragraph(
    "<b>Dataset</b><br/>"
    "Superstore Sales Dataset — Kaggle.",
    body_style
))

story.append(PageBreak())

# --------------------------------------------------
# 1. Project Description
# --------------------------------------------------

story.append(Paragraph("1. Project Description", heading_style))

story.append(Paragraph(
    "The objective of this project is to analyze retail sales performance "
    "and develop a basic forecasting model for future monthly sales. "
    "The workflow includes inspection and cleaning of the raw dataset, "
    "exploratory visualizations, statistical summaries, predictive modeling, "
    "model evaluation, and business recommendations.",
    body_style
))

# --------------------------------------------------
# 2. Data Cleaning
# --------------------------------------------------

story.append(Paragraph("2. Data Cleaning & Preparation", heading_style))

story.append(Paragraph(
    "The dataset contains 9,800 rows and 18 columns. The data was inspected "
    "for missing values, duplicate records, and incorrect data types.",
    body_style
))

story.append(Paragraph(
    "There were 11 missing values in the Postal Code column. These values "
    "were replaced with the label 'Unknown' because Postal Code is a "
    "location identifier and replacing it with a numerical average would "
    "not be meaningful.",
    body_style
))

story.append(Paragraph(
    "The Order Date and Ship Date columns were converted from text to "
    "datetime format. After conversion, both date columns contained zero "
    "missing values. No duplicate rows were found in the dataset.",
    body_style
))

# --------------------------------------------------
# 3. Statistical Summary
# --------------------------------------------------

story.append(Paragraph("3. Statistical Summary", heading_style))

table_data = [
    ["Statistic", "Sales"],
    ["Mean", "230.77"],
    ["Median", "54.49"],
    ["Standard Deviation", "626.65"],
    ["Minimum", "0.444"],
    ["Maximum", "22,638.48"],
]

table = Table(table_data, colWidths=[2.5 * inch, 2.5 * inch])
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("ALIGN", (1, 1), (1, -1), "RIGHT"),
    ("PADDING", (0, 0), (-1, -1), 7),
]))

story.append(table)
story.append(Spacer(1, 12))

story.append(Paragraph(
    "<b>Interpretation:</b> The mean sales value of 230.77 is substantially "
    "higher than the median of 54.49. This indicates that a relatively small "
    "number of high-value orders strongly influence the average sales value.",
    body_style
))

story.append(PageBreak())

# --------------------------------------------------
# 4. EDA Visualizations
# --------------------------------------------------

story.append(Paragraph("4. Exploratory Data Analysis", heading_style))

charts = [
    ("monthly_sales_trend.png", "Figure 1 — Monthly Sales Trend"),
    ("category_sales.png", "Figure 2 — Sales by Product Category"),
    ("region_sales.png", "Figure 3 — Sales by Region"),
    ("correlation_heatmap.png", "Figure 4 — Correlation Heatmap"),
    ("top_10_products.png", "Figure 5 — Top 10 Products by Sales"),
    ("actual_vs_predicted.png", "Figure 6 — Actual vs Predicted Monthly Sales"),
]

for filename, caption in charts:
    path = os.path.join(CHARTS, filename)

    if os.path.exists(path):
        story.append(Image(path, width=6.4 * inch, height=3.5 * inch))
        story.append(Paragraph(caption, caption_style))
    else:
        story.append(Paragraph(
            f"Chart file not found: {filename}",
            body_style
        ))

# --------------------------------------------------
# 5. Key Insights
# --------------------------------------------------

story.append(PageBreak())
story.append(Paragraph("5. Key Insights", heading_style))

insights = [
    "<b>Technology is the strongest category:</b> Technology generated "
    "the highest total sales at 827,455.87, followed by Furniture at "
    "728,658.58 and Office Supplies at 705,422.33.",

    "<b>Regional performance varies:</b> The West region recorded the "
    "highest sales at 710,219.68, while the South region recorded the "
    "lowest at 389,151.46.",

    "<b>Sales fluctuate substantially over time:</b> Monthly sales ranged "
    "from 4,519.89 in February 2015 to 117,938.15 in November 2018.",

    "<b>Top product:</b> Canon imageCLASS 2200 Advanced Copier was the "
    "highest-selling product, generating 61,599.82 in total sales."
]

for insight in insights:
    story.append(Paragraph("• " + insight, body_style))

# --------------------------------------------------
# 6. Predictive Modeling
# --------------------------------------------------

story.append(Paragraph("6. Predictive Modeling", heading_style))

story.append(Paragraph(
    "A Linear Regression model was first developed using monthly time "
    "sequence information. The model achieved an RMSE of 23,619.29 and "
    "an R² score of 0.0332, indicating that a simple linear trend was "
    "insufficient to capture the variation in monthly sales.",
    body_style
))

story.append(Paragraph(
    "An improved Random Forest Regression model was then developed using "
    "time-based and seasonal features including month number, year, month, "
    "and cyclical month features. The improved model achieved an RMSE of "
    "<b>16,094.10</b> and an R² score of <b>0.5511</b>.",
    body_style
))

model_table = [
    ["Model", "RMSE", "R² Score"],
    ["Linear Regression", "23,619.29", "0.0332"],
    ["Random Forest", "16,094.10", "0.5511"],
]

table = Table(model_table, colWidths=[2.5 * inch, 1.6 * inch, 1.6 * inch])
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("ALIGN", (1, 1), (-1, -1), "CENTER"),
    ("PADDING", (0, 0), (-1, -1), 7),
]))

story.append(table)

# --------------------------------------------------
# 7. Recommendations
# --------------------------------------------------

story.append(Paragraph("7. Business Recommendations", heading_style))

recommendations = [
    "Focus inventory and promotional activity on Technology products because this category generated the highest total sales.",
    "Investigate the lower-performing South region to identify opportunities related to customer demand, product availability, pricing, and marketing.",
    "Prioritize high-performing products such as the Canon imageCLASS 2200 Advanced Copier in inventory and promotional planning.",
    "Prepare inventory, staffing, and marketing campaigns for high-demand periods based on historical monthly sales patterns.",
    "Continue improving the forecasting model by incorporating additional variables such as customer segment, discount, shipping mode, product category, and lagged sales."
]

for i, recommendation in enumerate(recommendations, 1):
    story.append(Paragraph(
        f"<b>{i}.</b> {recommendation}",
        body_style
    ))

# --------------------------------------------------
# 8. Conclusion
# --------------------------------------------------

story.append(Paragraph("8. Conclusion", heading_style))

story.append(Paragraph(
    "The Sales Performance & Forecasting Analysis identified important "
    "patterns in the Superstore dataset. Technology was the highest-performing "
    "category, while the West was the strongest region. Sales showed substantial "
    "variation across months, with November 2018 recording the highest monthly sales.",
    body_style
))

story.append(Paragraph(
    "The Random Forest model performed substantially better than the initial "
    "Linear Regression model. The final Random Forest model achieved an R² "
    "score of 0.5511 and an RMSE of 16,094.10. The results demonstrate that "
    "time-based and seasonal information can improve monthly sales forecasting.",
    body_style
))

story.append(Paragraph(
    "Future improvements could include additional business variables and "
    "historical lagged sales features to improve predictive performance.",
    body_style
))

# --------------------------------------------------
# 9. GitHub
# --------------------------------------------------

story.append(Paragraph("9. GitHub Repository", heading_style))

story.append(Paragraph(
    "GitHub Repository: <b>To be added after repository creation.</b>",
    body_style
))

# --------------------------------------------------
# Build PDF
# --------------------------------------------------

doc.build(story)

print("PDF created successfully!")
print(OUTPUT)
