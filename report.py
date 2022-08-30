import webbrowser

from fpdf import FPDF

import os

class PdfReport:
    """
    creates a pdf file that contains data about the Flatmate such as their names,due amount and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self,bill,flatmate_info):

        pdf = FPDF(orientation='P',unit='pt',format='A4')
        pdf.add_page()

        pdf.image('files/img.png',w=100,h=100)

        pdf.set_font(family='Times',size=24,style='B')
        pdf.cell(w=0,h=80,txt='Flatmates Bill',border=0,align='C',ln=1)

        pdf.set_font(family='Times', size=20, style='B')
        pdf.cell(w=100,h=40,txt='Period',border=0)
        pdf.cell(w=150,h=40,txt=bill.period,border=0,align='C',ln=1)

        for x,y in flatmate_info.items():
            pdf.set_font(family='Times', size=14, style='B')
            pdf.cell(w=100,h=40,txt=x,border=0,align='C')
            pdf.cell(w=200,h=40,txt=str(flatmate_info.get(x)),border=0,align='C',ln=1)

        pdf.set_font(family='Times', size=16, style='B')
        pdf.cell(w=100, h=40, txt='Total Bill', border=0, align='C')
        pdf.cell(w=200, h=40, txt=str(bill.amount), border=0, align='C', ln=1)


        os.chdir('files')
        pdf.output(self.filename)
        webbrowser.open(self.filename)