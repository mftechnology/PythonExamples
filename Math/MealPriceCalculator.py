## Milestone - Meal Price Calculator
## by Marcelo Duarte
child_meal = input("What is the price of a child's meal?")
adult_meal = input("What is the price of an adult's meal?")
children = input("How many children are there?")
adults = input("How many adults are there?")
tax = input("What is the sales tax rate?")
subtotal=(float(child_meal)*int(children))+(float(adult_meal)*int(adults))
sales=float(subtotal)*float(tax)/100
sales2 = round(sales,2)
total = float(sales)+float(subtotal)
total2 = round(total,2)
print()
print("Subtotal: $"+str(subtotal))
print("Sales Tax: $"+str(sales2))
print("Total: $"+str(total2))
print()
payment = input("What is the payment amount?")
result = float(payment)-float(total)
change = round(result,2)
print("Change: $" + str(change))
