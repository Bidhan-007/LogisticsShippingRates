# Shipping Cost Calculator

## Input package weight and shipping rate
kindOfItem=input("Is it Fragile Item or Non-Fragile ? : ")
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

#Fragile Item Added Cost 
# per1kg - 0.5USD
if(kindOfItem=='fragile' | kindOfItem=='FRAGILE' | kindOfItem=='Fragile')
    shipping_cost+=(weight*0.5)

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")