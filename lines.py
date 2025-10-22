import sys #imports database to handle user's input in the terminal 
import os #imports databse to check if files exist (later) 

# Check for exactly 1 command-line argument
if len(sys.argv) != 2: 
    sys.exit("Usage: python lines.py filename.py")

filename = sys.argv[1]

# Check that the file ends with .py
if not filename.endswith(".py"):
    sys.exit("File must have a .py extension")

# Check that the file exists - uses the os database 
if not os.path.exists(filename):
    sys.exit(f"File '{filename}' does not exist")

# Initialize a counter for lines of code
loc = 0

# Open the file and process it line by line
with open(filename, "r", encoding="utf-8") as f: #opens file (name from terminal, in reading mode, and in a safe format for text), and creates a variable
    for line in f: #creates a loop to run every line in the file 
        stripped_line = line.strip()  # Remove leading/trailing whitespace
        
        if stripped_line and not stripped_line.startswith("#"):
            loc += 1
                # Skip blank lines and lines that start with #, add 1 line 
# Output the result
print(loc) 
