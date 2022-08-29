import webbrowser
from fpdf import FPDF

class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


def pays(bill,flatmate_info):
        ni =0
        for i in flatmate_info.values():
            ni =ni+i
        for x,y in flatmate_info.items():
            dd = y/ni
            individual_amt = round(bill.amount*dd,2)
            flatmate_info[x]=individual_amt
            print(f"{x} pays ", individual_amt)


class PdfReport:
    """
    creates a pdf file that contains data about the Flatmate such as their names,due amount and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self,bill,flatmate_info):

        pdf = FPDF(orientation='P',unit='pt',format='A4')
        pdf.add_page()

        pdf.image('img.png',w=100,h=100)

        pdf.set_font(family='Times',size=24,style='B')
        pdf.cell(w=0,h=80,txt='Flatmates Bill',border=0,align='C',ln=1)

        pdf.set_font(family='Times', size=20, style='B')
        pdf.cell(w=100,h=40,txt='Period',border=0)
        pdf.cell(w=150,h=40,txt=bill.period,border=0,align='C',ln=1)

        for x,y in flatmate_info.items():
            pdf.set_font(family='Times', size=14, style='B')
            pdf.cell(w=100,h=40,txt=x,border=0,align='C')
            pdf.cell(w=200,h=40,txt=str(flatmate_info.get(x)),border=0,align='C',ln=1)


        pdf.output(self.filename)

        webbrowser.open(self.filename)


amount = float(input("Enter the bill amount : "))
period = input("For the month : ")

billss = Bill(amount,period)

n = int(input("No of people in the flat : "))

flatmate_info ={}

for i in range(n):
    name=input("Name of flatmate "+str(i+1)+" is : ")
    days_in_house=int(input("No of days in the house: "))
    flatmate_info[name]=days_in_house

for x,y in flatmate_info.items():
    print(f"Flatmate {x} stayed for {y} days")

pays(billss,flatmate_info)


pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(billss,flatmate_info)
