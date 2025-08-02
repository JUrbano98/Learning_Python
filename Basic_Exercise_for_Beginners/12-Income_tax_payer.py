'''
Calculate income tax for the given income by adhering to the rules below:

Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20
'''


def tax(income):
    if income <= 10000:
        return 0
    if 10000 < income <= 20000:
        return 0.1*(income-10000)
    else:
        return 1000 + 0.2*(income-20000)


amount = 45000
print("Tax payed for $", amount, "is $", tax(45000))
