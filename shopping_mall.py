#Welcome message
print("=== Welcome To Kifaya Mart Payment Portal ===")

#Step 1 : Total Bill Input
total_bill = float(input("Enter the total bill amount \n: "))

#Step 2 : Apply Discount
if total_bill == 17000 :
    discount = total_bill * 0.25
elif total_bill == 70000 :
    discount = total_bill * 0.50
elif total_bill == 80000 :
    discount = total_bill * 0.75
else:
    discount = 0

#Step 3 : Final Bill After Discount
final_amount = total_bill - discount
print(f" Your final bill after discount is : {final_amount} Rs \n ")

#Step 4 : Payment Method & GST
payment_method = input("Enter your payment method (Cash/ATM/Credit Card): \n ")

if payment_method.lower() == "atm" or payment_method.lower() == "credit card" :
    num_products = int(input("enter the number of products : \n "))
    gst = num_products * 23
    final_amount += gst
    print(f"An additional GST of {gst} Rs has been added. \n ")

#Step 5 : Display Final Amount
print(f" Your total payable amount is : {final_amount} Rs ")
