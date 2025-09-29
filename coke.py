#defining the main function
def main():
    amount_due = 50  # Total cost of a Coke
    accepted_coins = [25, 10, 5]  # List of valid denominations (coins)

    while amount_due > 0: #create a loop until the variable "amount_due" is bigger than 0
        print(f"Amount Due: {amount_due}") #print a formatted string with the message: "Amount Due: + the value of the function "amount_due"
        coin = int(input("Insert Coin: ")) #input to get the user to insert another coin to pay for the coke

# Only accept valid coins
        if coin in accepted_coins: #creates a new variable - coin
            amount_due -= coin  #Subtract the coin value to the amount_due variable (only when it is correspondent to accepted_coins)

# If the coin is invalid, ignore it (do nothing)

# When amount_due is 0 or negative, calculate change
    change_owed = abs(amount_due) #returns the absolute value of the amount_due - assures positive value
    print(f"Change Owed: {change_owed}") #output a format string with the text "change owed" + the value of the varaible change_owed


#Run the function
main()
