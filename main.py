from Flat import Bill, Flatmate
from report import PdfReport

amount = float(input("Enter the bill amount : "))
period = input("For the month : ")

bills = Bill(amount, period)

n = int(input("No of people in the flat : "))

info= Flatmate.f_info(n)

Flatmate.pays(bills, info)

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(bills, info)
