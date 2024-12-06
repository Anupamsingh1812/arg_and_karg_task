def shopping_cart(*items, **deductions):
    total_cost = 0
    item_details = []
    
    for item, price, quantity in items:
        cost = price * quantity
        total_cost += cost
        item_details.append(f"{item}: ${price} x {quantity} = ${cost}")
    
    print("Detailed Bill:")
    print("Items:")
    for detail in item_details:
        print(f"  {detail}")
    
    print(f"Subtotal: ${total_cost}")
    
    if 'discount' in deductions:
        discount = deductions['discount']
        total_cost -= total_cost * (discount / 100)
        print(f"Discount ({discount}%): -${total_cost * (discount / 100):.2f}")
    
    if 'promo_code' in deductions:
        promo_code_discount = deductions['promo_code']
        total_cost += promo_code_discount
        print(f"Promo Code Applied! ${promo_code_discount}")
    
    if 'delivery_charge' in deductions:
        delivery_charge = deductions['delivery_charge']
        if total_cost > 500:
            print("You Got Free Delivery!")
        else:
            total_cost += delivery_charge
            print(f"Delivery Charge: ${delivery_charge}")
    
    print(f"Total: ${total_cost:.2f}")

Items = [("Laptop", 1000, 1), ("Mouse", 20, 2), ("Keyboard", 50, 1)]
shopping_cart(*Items, discount=10, promo_code=-10, delivery_charge=50)
