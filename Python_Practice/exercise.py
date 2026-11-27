# 1. Variables & Data Types
item_name = "Wireless Headphones"  # String
quantity = 2                       # Integer
unit_price = 49.99                 # Float
is_member = True                   # Boolean

# 2. Maths with Numbers
subtotal = quantity * unit_price

# 3. Formatting Strings & Outputting
print(f"Order Summary: {quantity}x {item_name.upper()}")
print(f"Total Due: £{subtotal}")
print(f"Data type of subtotal: {type(subtotal)}")
