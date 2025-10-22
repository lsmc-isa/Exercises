
MENU = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
# Create a lookup dict with lowercase keys for case-insensitive matching

MENU_LOWER = {item.lower(): price for item, price in MENU.items()} #all characters are now in lowercase - allows for the user to input in any case

def main():
    total = 0.0 #total in the beggining- 0
    try:
        while True: #creating a loop to keep asking for items
            item = input("Item: ").strip().lower() 
            if item in MENU_LOWER: # Ignore invalid items silently - only process items on the dictionary 
                total += MENU_LOWER[item]
                print(f"Running total: ${total:.2f}")
            
    
    except EOFError: #Once the user finishes and presses ctrl + z (windows) 
        print("\nThank you for your order!")
        print(f"Final total: ${total:.2f}") #

main() 