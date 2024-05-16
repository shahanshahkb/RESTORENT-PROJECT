#Define the menue of restaurant
menu={
    "Pizza":50,
     "Pasta":80,
     "Burger":100,
     "Saled":75,
     "Coffe":45,
}

#great
print(" WELCOME TO MAC RESTORENT ")
print("Pizza: Rs50\nPasta: Rs80 \nBurger: Rs100\nSaled: Rs75\nCoffe:Rs45")


order_total=0
#50+80=130

item_1=input("enter the name of items you want to irder =")
if item_1 in menu:
    order_total+=menu[item_1]  #0+75
    print(f"your item {item_1} has been add to your order ")


else :
    print(f" order item {item_1} is not avaialable  ")

another_order=input(f" do you want to add another items (Yes/No)")
if another_order=="Yes":
    item_2=input("enter the name of second item = ")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"item{item_2} has been added to order ")
    else:
        print(f"order item {item_2} is not avaialabel !")


print(f"The total amount of items to pay  {order_total}")
