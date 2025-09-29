def main():
    # Ask the user for a file name
    filename = input("File name: ").strip().lower()
#input - What the user sees in the terminal to input a value
#.strip - removes extra spaces
#.lower - all input value is now in lower case
    #allows the information to be "readible" for the next step

    # Dictionary mapping extensions to media types
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    } #creates a quick an easy to read match for the value (easier than using if function repeatdly)

# Check if filename ends with a known extension
    for ext, mime in media_types.items(): #ext - format; mime - match; name.items - calls dictionary
        if filename.endswith(ext): #if the format is on the dictionary:
            print(mime) #print the look-up value
            return  # Stop once a match is found


    print("application/octet-stream") #if the function cannot be executed, print this instead


# Run the program
main()
