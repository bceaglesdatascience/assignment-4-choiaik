
# input purchases and sales tax 
purchases= int(input('Number of purchases: '))
sales_tax= float(input('Sales tax: '))

# define add_tax that takes a list and returns a new list 
def add_tax(costs, tax_rate):
    return [cost * (1 + tax_rate) for cost in costs]

# create dictionary for all customers 
customer_all = {}

# take info on each purchase; calculate total

for _ in range(purchases):
    customer = input("Customer: ")
    cost = float(input(f"Cost: "))   

    # calculate the cost with sales tax
    cost_taxed = cost*(1 + sales_tax)
    
    # update all customer total costs in the dictionary
    if customer in customer_all:
        customer_all[customer] += cost_taxed
    else:
        customer_all[customer] = cost_taxed

# print total taxed cost for each customer

total = {customer: total_cost for customer, total_cost in customer_all.items()}
print(total)
