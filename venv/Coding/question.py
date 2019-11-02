#My first time coding, mght be inefficient
item1 = float(input("Enter the cost of item1: "))

item2 = float(input("Enter the cost of item2: "))

item3 = float(input("Enter the cost of item3: "))

item4 = float(input("Enter the cost of item4: "))

item5 = float(input("Enter the cost of item5: "))

item6 = float(input("Enter the cost of item6: "))

Costitem = float(item1+item2+item3+item4+item5+item6)

tax = float(0.06*Costitem)

TotalCost = float(Costitem + tax)

print("Total Cost of items: " + str(TotalCost))
print(Costitem + tax)

