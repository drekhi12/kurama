from reportlab.pdfgen import canvas
from reportlab.platypus import (SimpleDocTemplate, Paragraph, PageBreak)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import LETTER


class FooterCanvas(canvas.Canvas):

    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.pages = []

    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        page_count = len(self.pages)
        for page in self.pages:
            self.__dict__.update(page)
            self.draw_canvas(page_count)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_canvas(self, page_count):
        page = "Page %s of %s" % (self._pageNumber, page_count)
        x = 128
        self.saveState()
        self.setStrokeColorRGB(0, 0, 0)
        self.setLineWidth(0.5)
        self.line(66, 78, LETTER[0] - 66, 78)
        self.setFont('Times-Roman', 10)
        self.drawString(LETTER[0]-x, 65, page)
        self.restoreState()


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
    doc.multiBuild(elements, canvasmaker=FooterCanvas)
