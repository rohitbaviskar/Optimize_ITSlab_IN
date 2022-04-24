gross = int(input("Please Enter Gross Salary. This includes - Basic, HRA, DA, Allowances, Bonuses, etc.: Rs. "))

if gross > 1500000:
    tax30 = (gross - 1500000) * 0.3
    tax25 = 250000 * 0.25
    tax20 = 250000 * 0.20
    tax15 = 250000 * 0.15
    tax10 = 250000 * 0.10
    tax5 = 250000 * 0.05
    tax0 = 0
else:
    if gross < 1500000 and gross > 1250000:
        tax30 = 0
        tax25 = (gross - 1250000) * 0.25
        tax20 = 250000 * 0.20
        tax15 = 250000 * 0.15
        tax10 = 250000 * 0.10
        tax5 = 250000 * 0.05
        tax0 = 0

    else:
        if gross < 1250000 and gross > 1000000:
            tax30 = 0
            tax25 = 0
            tax20 = (gross - 1000000) * 0.20
            tax15 = 250000 * 0.15
            tax10 = 250000 * 0.10
            tax5 = 250000 * 0.05
            tax0 = 0

        else:
            if gross < 1000000 and gross > 750000:
                tax30 = 0
                tax25 = 0
                tax20 = 0
                tax15 = (gross - 750000) * 0.15
                tax10 = 250000 * 0.10
                tax5 = 250000 * 0.05
                tax0 = 0

            else:
                if gross < 750000 and gross > 500000:
                    tax30 = 0
                    tax25 = 0
                    tax20 = 0
                    tax15 = 0
                    tax10 = (gross - 500000) * 0.10
                    tax5 = 250000 * 0.05
                    tax0 = 0

                else:
                    if gross < 500000:
                        tax30 = 0
                        tax25 = 0
                        tax20 = 0
                        tax15 = 0
                        tax10 = 0
                        tax5 = 0
                        tax0 = 0

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