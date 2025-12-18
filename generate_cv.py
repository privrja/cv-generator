from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Frame, PageTemplate
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from PIL import Image, ImageDraw
from reportlab.platypus import FrameBreak


# ---------- CONFIG ----------
OUTPUT = "Jan_Privratsky_CV_EN.pdf"
PHOTO = "photo.jpg"

# GREEN = colors.HexColor("#2f6f5f")
# LIGHT_BG = colors.HexColor("#e8f0ed")
GREEN = colors.HexColor("#1f5c4d")      # darker green
LIGHT_BG = colors.HexColor("#dbe7e3")   # darker mint background
LINK_BLUE = colors.HexColor("#1a0dab")  # clasic web blue
SIDEBAR_BG = colors.HexColor("#184f45")   # dark green
SIDEBAR_TEXT = colors.HexColor("#ffffff")
SIDEBAR_ACCENT = colors.HexColor("#b7e0d6")  # soft mint accent
GREEN = colors.HexColor("#1f6f5c")        # main green on right


# ---------- IMAGE HELPERS ----------
def rounded_image(input_path, output_path, radius=30):
    img = Image.open(input_path).convert("RGBA")
    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle(
        (0, 0, img.size[0], img.size[1]),
        radius=radius,
        fill=255
    )
    img.putalpha(mask)
    img.save(output_path)

rounded_image(PHOTO, "photo_rounded.png")

# ---------- DOCUMENT ----------
doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    leftMargin=0,
    rightMargin=0,
    topMargin=0,
    bottomMargin=0
)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="Name",
    fontSize=22,
    spaceAfter=8,
    textColor=colors.black
))
styles.add(ParagraphStyle(
    name="JobTitle",
    fontSize=13.5,
    textColor=GREEN,
    spaceBefore=6,
    spaceAfter=20
))
styles.add(ParagraphStyle(
    name="Section",
    fontSize=12,
    textColor=GREEN,
    spaceBefore=14,
    spaceAfter=8
))
styles.add(ParagraphStyle(
    name="Body",
    fontSize=10.2,
    leading=14
))

styles.add(ParagraphStyle(
    name="Sidebar",
    fontSize=10.8,
    textColor=SIDEBAR_TEXT,
    leading=15
))

styles.add(ParagraphStyle(
    name="CV_Sidebar_Section",
    fontSize=11.5,
    leading=16,
    textColor=SIDEBAR_ACCENT,
    spaceBefore=16,
    spaceAfter=8
))

styles.add(ParagraphStyle(
    name="CV_Link",
    fontSize=10.2,
    leading=14,
    textColor=LINK_BLUE,
    underline=True
))

# ---------- SIDEBAR ----------
sidebar = []
sidebar.append(Spacer(1, 15))
sidebar.append(Paragraph("CONTACT", styles["CV_Sidebar_Section"]))
sidebar.append(Paragraph("+420 603 466 674", styles["Sidebar"]))
sidebar.append(Paragraph("privrja@gmail.com", styles["Sidebar"]))
sidebar.append(Paragraph("Prague", styles["Sidebar"]))
#sidebar.append(Paragraph("Driver’s license (B)", styles["Sidebar"]))
sidebar.append(Paragraph("<a href='www.linkedin.com/in/privratskyjan'>linkedin.com/in/privratskyjan</a>", styles["Sidebar"]))
sidebar.append(Spacer(1, 10))

sidebar.append(Paragraph("SKILLS", styles["CV_Sidebar_Section"]))
skills = [
    "Team Leadership",
    "Data Warehousing",
    "Data Analysis",
    "Data Governance",
    "Snowflake",
    "SQL (MSSQL)",
    "Azure Data Factory",
    "ETL",
    "SQL Tuning",
    "Git",
    "CI/CD",
    "Power BI"
]
for s in skills:
    sidebar.append(Paragraph(f"{s}", styles["Sidebar"]))

sidebar.append(Spacer(1, 10))
sidebar.append(Paragraph("LANGUAGES", styles["CV_Sidebar_Section"]))
sidebar.append(Paragraph("Czech – Native", styles["Sidebar"]))
sidebar.append(Paragraph("English – B2", styles["Sidebar"]))

# ---------- MAIN CONTENT ----------
main = []
main.append(Paragraph("Jan Privratsky", styles["Name"]))
main.append(Spacer(1, 6))
main.append(Paragraph("DWH Team Leader", styles["JobTitle"]))

main.append(Paragraph(
    "Data & BI professional with 6+ years of experience in data warehousing, "
    "BI solutions, and modern data platforms. Currently leading a DWH team at "
    "Allwyn CZ with a strong focus on Snowflake cloud migration and team leadership.",
    styles["Body"]
))

main.append(Paragraph("Work Experience", styles["Section"]))

main.append(Paragraph(
    "<b>DWH Team Leader – Sazka / Allwyn CZ</b> (Jan 2025 – Present)<br/>"
    "• Leading DWH team, prioritization, release management<br/>"
    "• On-prem DWH migration to Snowflake<br/>"
    "• Launch of DWH for Allwyn SK<br/>"
    "• Rebranding from Sazka to Allwyn<br/>"
    "• Migration of Sazka Mobil data to Vodafone",
    styles["Body"]
))

main.append(Spacer(1, 6))
main.append(Paragraph(
    "<b>BI Developer – Sazka</b> (Jan 2024 - Dec 2024)<br/>"
    "• DWH & BI ETL development<br/>"
    "• Upgrade DWH SQL Server to version 2022<br/>"
    "• Azure Data Factory and ETL orchestration",
    styles["Body"]
))

main.append(Spacer(1, 6))
main.append(Paragraph(
    "<b>BI Developer – Pivovary Staropramen</b> (Jul 2021 – Dec 2023)<br/>"
    "• Datamarts, Tableau & Power BI<br/>"
    "• SSRS & ETL (Pentaho)",
    styles["Body"]
))

main.append(Spacer(1, 6))
main.append(Paragraph(
    "<b>Junior Java Developer – Pivovary Staropramen</b> (Jul 2019 – Jun 2021)<br/>"
    "• Backend development supporting DWH solutions<br/>"
    "• SQL, Java, Groovy",
    styles["Body"]
))

main.append(Spacer(1, 6))
main.append(Paragraph(
    "<b>Developer & DevOps Hatchery – Unicorn</b> (Feb 2019 – Mar 2019)<br/>"
    "• Spring Boot backend development<br/>"
    "• REST & database integration, CI/CD",
    styles["Body"]
))

main.append(Spacer(1, 6))
main.append(Paragraph(
    "<b>Backend Developer Intern – Tipsport</b> (Jul 2018 – Aug 2018)<br/>"
    "• Java backend development for internal systems",
    styles["Body"]
))

main.append(Paragraph("Education", styles["Section"]))
main.append(Paragraph(
    "<b>Master’s degree, Software Engineering</b><br/>"
    "Czech Technical University – FIT, Prague (2019–2021)",
    styles["Body"]
))
main.append(Spacer(1, 4))
main.append(Paragraph(
    "<b>Bachelor’s degree, Software Engineering</b><br/>"
    "Czech Technical University – FIT, Prague (2016–2019)",
    styles["Body"]
))

main.append(Paragraph("Publications & Media", styles["Section"]))
main.append(Paragraph(
    '<a href="https://www.buzzsprout.com/2034779/episodes/17019771-data-talk-133-jan-privratsky-sazka-a-s">'
    'Podcast: Data Talk #133</a>',
    styles["CV_Link"]
))

main.append(Paragraph(
    '<a href="https://link.springer.com/article/10.1186/s13321-021-00530-2">'
    'Publication: MassSpecBlocks (2021)</a>',
    styles["CV_Link"]
))


# ---------- LAYOUT ----------
sidebar_frame = Frame(
    0,
    0,
    60 * mm,
    A4[1],
    leftPadding=12,
    topPadding=130,
    bottomPadding=20,
    showBoundary=0
)

main_frame = Frame(
    65 * mm,
    20,
    A4[0] - 70 * mm,
    A4[1] - 40,
    showBoundary=0
)

def draw_background(canvas, doc):
    canvas.setFillColor(SIDEBAR_BG)
    canvas.rect(0, 0, 60 * mm, A4[1], stroke=0, fill=1)

    canvas.drawImage(
      "photo_rounded.png",
      10 * mm,              # slightly more to the left
      A4[1] - 48 * mm,      # slightly lower
      width=40 * mm,
      height=40 * mm,
      mask='auto'
    )


doc.addPageTemplates([
    PageTemplate(
        frames=[sidebar_frame, main_frame],
        onPage=draw_background
    )
])

story = []

# sidebar first
story.extend(sidebar)

# switch to main frame
story.append(FrameBreak())

# then main content
story.extend(main)

doc.build(story)

print("CV generated:", OUTPUT)
