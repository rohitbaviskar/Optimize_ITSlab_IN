gross = int(input("Please Enter Gross Salary. This includes - Basic, HRA, DA, Allowances, Bonuses, etc.: Rs. "))

if gross >= 1000000:
    old_tax30 = (gross - 1000000) * 0.3
    old_tax20 = 500000 * 0.20
    old_tax5 = 250000 * 0.05
    old_tax0 = 0
elif gross < 1000000 and gross > 500000:
    old_tax30 = 0
    old_tax20 = (gross - 500000) * 0.2
    old_tax5 = 250000 * 0.05
    old_tax0 = 0
elif gross < 500000:
    old_tax30 = 0
    old_tax20 = 0
    old_tax5 = 0
    old_tax0 = 0


old_it_tax = old_tax30 + old_tax20 + old_tax5 + old_tax0

# Cess is 4% of the tax which needs to be paid additionally
old_cess = old_it_tax * 0.04

old_total_tax = old_it_tax + old_cess

old_effective_tax_rate = round((old_total_tax/gross)*100, 2)

print(old_total_tax)

print(old_effective_tax_rate)