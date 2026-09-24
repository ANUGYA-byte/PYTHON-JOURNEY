# ---------------------------------------
# Program 40: Profit or Loss Calculator
# Description:Calculates profit or loss based on cost price and selling price.
# Author: Anugya Agrawal
#---------------------------------------
cost_price = float(input("ENTER COST PRICE: "))
selling_price = float(input("ENTER SELLING PRICE: "))

if cost_price < 0 or selling_price < 0:
    print("INVALID PRICE")
elif selling_price > cost_price:
    profit = selling_price - cost_price
    print("PROFIT - ₹", profit)
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("LOSS - ₹", loss)
else:
    print("NO PROFIT AND NO LOSS")

# ---------------------------------------
#SAMPLE -
#ENTER COST PRICE-230
#ENTER SELLING PRICE-44
#LOSS-Rs 186.0
# ---------------------------------------
#SAMPLE -
#ENTER COST PRICE-45
#ENTER SELLING PRICE-45
#NO PROFIT AND LOSS
# ---------------------------------------
#SAMPLE -
#ENTER COST PRICE-33
#ENTER SELLING PRICE-333
#PROFIT-Rs 300.0
