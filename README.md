# Tax-calculator
import time
print("Welcome to your tax calculator!")
print("-----------------------------------------------------")
Hours = int(input("To begin please input your worked hours this week:"))
while Hours > 60 or Hours < 0:
    Hours = int(input("Please enter realistic values: "))
Income = int(input("Please enter weekly income: "))
while Income < 1000:
    Income = int(input("Value is too low, please enter a realistic value: "))
Yearly_Income=Income*52
print("Yearly income amounts to:",Yearly_Income)
time.sleep(1)
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
print("Your income tax payed is:",IncomeTaxPayed)
print("Based on number of hours worked...")
time.sleep(2)

Tax_deductible = ((21**(Hours/60)-1)/100)*IncomeTaxPayed
Tax_deductible = round(Tax_deductible)
print("The amount deductible from tax is:",Tax_deductible)
Total_amount_payed = IncomeTaxPayed - Tax_deductible
Total_amount_payed = round(Total_amount_payed)
time.sleep(1)
print("The outstanding total to be payed after deductions is:",Total_amount_payed)
Real_income = Yearly_Income - Total_amount_payed
print("After taxes, real income remaining:",Real_income )
