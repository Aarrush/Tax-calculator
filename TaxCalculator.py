from tkinter import *
from tkinter import messagebox
import time

Yearly_Income = 0
IncomeTaxPayed = 0
Tax_deductible = 0
Total_amount_payed = 0

def main():
  Hours = E1.get()
  Hours = int(Hours)
  if Hours < 0 or Hours > 60:
    messagebox.showinfo("Error", "Value is inconsistent, please enter realistic values")
    exit()

  Income = E2.get()
  Income = int(Income)
  if Income < 100 or Income > 10000:
    messagebox.showinfo("Error", "Value is inconsistent, please enter realistic values")
    exit()

  global Yearly_Income
  Yearly_Income=Income*52
  global IncomeTaxPayed

  IncomeTaxPayed = 0
  if Yearly_Income < 30000:  
    IncomeTaxPayed = ((30000 - Yearly_Income) * 0.02)
  elif Yearly_Income < 40000 and Yearly_Income >= 30000:
    IncomeTaxPayed = (200 + (40000 - Yearly_Income) * 0.035 )
  elif Yearly_Income >= 40000 and Yearly_Income < 80000:
    IncomeTaxPayed = (550 + (80000 - Yearly_Income) * 0.07)
  elif Yearly_Income >= 80000 and Yearly_Income < 120000:
    IncomeTaxPayed = (3350 + (120000 - Yearly_Income) * 0.115)
  elif Yearly_Income >= 120000 and Yearly_Income < 160000:
    IncomeTaxPayed = (7950 + (160000 - Yearly_Income) * 0.15)
  elif Yearly_Income >=160000 and Yearly_Income < 200000:
    IncomeTaxPayed = (13950 + (200000 - Yearly_Income) * 0.18)
  elif Yearly_Income >= 200000 and Yearly_Income < 240000:
    IncomeTaxPayed = (21150 + (240000 - Yearly_Income) * 0.19)
  elif Yearly_Income >= 240000 and Yearly_Income < 280000:
    IncomeTaxPayed = (28750 + (280000 - Yearly_Income) * 0.195)
  elif Yearly_Income >= 280000 and Yearly_Income < 320000:
    IncomeTaxPayed = (36550 + (320000 - Yearly_Income) * 0.2)
  elif Yearly_Income >= 320000:
    IncomeTaxPayed = 44550 + ((Yearly_Income - 320000) * 0.22)

  IncomeTaxPayed = round(IncomeTaxPayed)

  global Tax_deductible
  Tax_deductible = ((21**(Hours/60)-1)/100)*IncomeTaxPayed
  Tax_deductible = round(Tax_deductible)

  global Total_amount_payed
  Total_amount_payed = IncomeTaxPayed - Tax_deductible
  Total_amount_payed = round(Total_amount_payed)

  global Real_income
  Real_income = Yearly_Income - Total_amount_payed

  time.sleep(1)

  final_yearly_come = "Yearly income is: " + str(Yearly_Income)
  L3 = Label(top, text=final_yearly_come)
  L3.pack(side = TOP)

  final_tax_payed = "Income tax payed: " + str(IncomeTaxPayed)
  L4 = Label(top, text = final_tax_payed)
  L4.pack(side = TOP)

  final_tax_deductible = "Tax deductible: " + str(Tax_deductible)
  L5 = Label(top, text = final_tax_deductible)
  L5.pack(side = TOP)

  final_total_payed = "Final tax payed: " + str(Total_amount_payed)
  L6 = Label(top, text = final_total_payed)
  L6.pack(side = TOP)

  final_real_income = "Real income: " + str(Real_income)
  L7 = Label(top, text = final_real_income)
  L7.pack(side = TOP)


top = Tk()
top.title("Tax Calculator")

L1 = Label(top, text="Please enter weekly hours worked.")
L1.pack( side = TOP)
E1 = Entry(top, bd =5)
E1.pack(side = TOP)

L2 = Label(top, text="Please enter weekly income.")
L2.pack( side = TOP)
E2 = Entry(top, bd =5)
E2.pack(side = TOP)

B = Button(top, text ="Enter", command = main)
B.pack(side = TOP)

top.mainloop()
