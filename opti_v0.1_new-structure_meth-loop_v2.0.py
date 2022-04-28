gross = int(input("Please Enter Gross Salary. This includes - Basic, HRA, DA, Allowances, Bonuses, etc.: Rs. "))

income_slab = (1500000, 1250000, 1000000, 750000, 500000, 250000, 0)
rate = (0.3, 0.25, 0.2, 0.15, 0.1, 0.05, 0)
a = [0, 0, 0, 0, 0, 0, 0]
tax_v = ['tax30', 'tax25', 'tax20', 'tax15', 'tax10', 'tax5', 'tax0']
tax = [0, 0, 0, 0, 0, 0, 0]

a[0] = gross - income_slab[0]
if a[0] < 0:
    a[0] = 0

for i in range(1, len(income_slab)):
    a[i] = gross - income_slab[i]
    if a[i] > 250000:
        a[i] = 250000
    elif a[i] < 0:
        a[i] = 0

#Below block is used to compute tax in the slab
for i in range(0, len(tax)):
    tax[i] = round((a[i] * rate[i]), 4)

#"tax_v" is the variable list. The below block of code is used to call any variable from the below list.
for x, y in zip(tax_v, tax):
    globals()[x] = y

# Cess is 4% of the tax which needs to be paid additionally
it_tax = sum(tax)
cess = it_tax * 0.04

total_tax = it_tax + cess

effective_tax_rate = round((total_tax/gross)*100, 2)

print(total_tax)
print(effective_tax_rate)
