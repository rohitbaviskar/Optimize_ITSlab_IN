gross = int(input("Please Enter Gross Salary. This includes - Basic, HRA, DA, Allowances, Bonuses, etc.: Rs. "))

tax0 = 0

if gross < 500001:
    tax5 = 0
else:
    tax5 = 250000 * 0.05

if gross < 500001:
    tax10 = 0
else:
    if gross > 500000 and gross < 750001:
        tax10 = (gross - 500000) * 0.1
    else:
        if gross > 750000:
            tax10 = 250000 * 0.1

if gross < 750001:
    tax15 = 0
else:
    if gross > 750000 and gross < 1000001:
        tax15 = (gross - 750000) * 0.15
    else:
        if gross > 1000000:
            tax15 = 250000 * 0.15

if gross < 1000001:
    tax20 = 0
else:
    if gross > 1000000 and gross < 1250001:
        tax20 = (gross - 1000000) * 0.2
    else:
        if gross > 1250000:
            tax20 = 250000 * 0.2

if gross < 1250001:
    tax25 = 0
else:
    if gross >= 1250000 and gross < 1500001:
        tax25 = (gross - 1250000) * 0.25
    else:
        if gross > 1500000:
            tax25 = 250000 * 0.25


if gross < 1500001:
    tax30 = 0
else:
    tax30 = (gross - 1500000)*0.3


total_tax = tax30 + tax25 + tax20 + tax15 + tax10 + tax5 + tax0

effective_tax_rate = round((total_tax/gross)*100, 2)

print(tax0)
print(tax5)
print(tax10)
print(tax15)
print(tax20)
print(tax25)
print(tax30)



print(total_tax)

print(effective_tax_rate)