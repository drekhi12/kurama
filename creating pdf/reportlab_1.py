from reportlab.pdfgen import canvas

c=canvas.Canvas("sample.pdf")
c.drawString(0,1000,"Hello World")
c.save()
