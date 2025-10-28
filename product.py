shop={}
def add_item():
    id = input("Enter Product ID: ")
    if id in shop:
        print(" Item already exists!")
        return
    name = input("Enter Product Name: ")
    brand=input("Enter item brand: ")
    price = input("Enter Item Price: ")
    category = input("Enter Category: ")
    stock=int(input("Enter Current Stock"))
    shop[id] = {"name": name, "brand":brand, "price":price , "category":category , "stock":stock}
    print("item added successfully")

def search_item():
    s = input("Enter product name to look for: ")
    print("\nList of Matching Item Records:")
    found=0
    for id, info in shop.items():
        if s in info["name"].lower():
            print(f"ID: {id}, Name: {info['name']}, Brand: {info['brand']}, Price: {info['price']}, Category: {info['category']}, Stock Available: {info['stock']}")
            found = True
    if not found:
        print("No items found!")
def sell_item():
    id = input("Enter Product ID to sell: ")
    if id not in shop:
        print(" Item not found!")
        return
    qty = int(input("Enter Quantity to Sell: "))
    if qty <= 0:
        print("Quantity must be positive!")
        return
    if qty > shop[id]["stock"]:
        print(" Not enough stock available!")
        return
    total = shop[id]["price"] * qty
    shop[id]["stock"] -= qty
    print(f"\n {qty} unit(s) of '{shop[id]['name']}' sold successfully!")
    print(f"Total Bill Amount: ₹{total:.2f}")
    print(f"Remaining Stock: {shop[id]['stock']}")

        
while(1):
    ch=int(input("Enter 1 to add item\n Enter 2 to search\n Enter 3 to Sell Item:"))
    match(ch):
        case(1):
            add_item()
        case(2):
            search_item()
        case(3):
            sell_item()
        case(4):
            break