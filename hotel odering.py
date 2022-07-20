
items="Idly , uthappam , Dosa , Poratta , Kichadi"
name=input("What is your name? \n")
print("Hello, " + name + " here is our menu: \n " + items + " select the item to serve to you\n")
order=input()
if order =="Idly":
    price = 5
elif order == "uthappam":
    price = 12
elif order == "Dosa":
    price =10
elif order == "Poratta":
    price = 15
elif order == "Poratta & salna":
    price = 15+10
elif order == "Kichadi":
    price=8
else:
    print("this item is not in the menu")

quantity=input("how much do you like to have:\n ")
total=price * int(quantity)
print("Price of "+str(quantity) + " " + str(order) + " is " + str(total))



print("Hey!,great your order  " + str(quantity)  + " " + str(order) + " will be served in minutes!........Have great day ")