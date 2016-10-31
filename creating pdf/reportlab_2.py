from reportlab.platypus import (SimpleDocTemplate, Paragraph, PageBreak)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import LETTER


if __name__ == '__main__':

    # Content
    styles = getSampleStyleSheet()
    elements = []
    elements.append(Paragraph("Hello", styles["Normal"]))
    elements.append(Paragraph("World", styles["Normal"]))
    elements.append(PageBreak())
    elements.append(Paragraph("You are in page 2", styles["Normal"]))

    # Build
    doc = SimpleDocTemplate("my_file.pdf", pagesize=LETTER)
    doc.build(elements)
