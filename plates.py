def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #Rule 1: check the length
    if len(s) < 2 or len(s) > 6:
        return False #only continue to run the function, if value for length is true

    #Rule 2: Check if the beggining is two letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False #only continues the function if the value if true

    #Rule 3: Can only have letters and numbers
    if not s.isalnum(): #function that assures only numbers and text
        return False

    #Rule 4: Position of numbers - must come last
    number_started = False #creation of a variable. Since, at this this point, there is no numbers at the start, this variable as a False value.
    for char in s: #For the values of every character (loop):
        if char.isdigit(): #checking if the character is a number (0-9)
            if not number_started: #if the character is a number - 1st in the plate
                # Rule 5: The first number cannot be 0
                if char == "0":
                    return False
                number_started = True #if the character is a number different than 0, return the value
        elif number_started:
            # Letter after numbers → invalid
            return False

        # If all conditions are valid, return a value and finish the function
        return True
main()
