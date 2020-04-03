#python file to calculate the total after going grocery shopping
item1 = 20
item2 = 13.33
item3 = 79.99
tax = 1.0825

total =item1+item2+item3
print("Total before Tax: ", total)
totalCost = total* tax
print("Total after tax: ", totalCost)
taxTotal = totalCost-total
print("Tax cost: ", taxTotal)
