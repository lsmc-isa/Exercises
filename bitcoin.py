import sys #database to handle terminal information from the user 
import requests #to make http requests to get the bitcoin price

def main():
    # Check for correct number of command-line arguments - 1 argument expected (the number of bitcoins)
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py <number_of_bitcoins>")

    # Try converting the argument to a float
    try:
        n = float(sys.argv[1])
    except ValueError:          #when the conversion fails:
        sys.exit("Error: Please provide a valid number.")

    # Replace with your actual CoinCap API key
    api_key = "9f7e7ee53bfd7db53560566e41a4c02e821cdbbe0056a2978c36aae45114df4f"
    url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"
    # Query the API and handle potential request exceptions
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        data = response.json() 
        print (data) #to check what´s on the inside of the data variable
       
        price = float(data["data"]["priceUsd"]) #gets "inside the data, on the data tab, to the price value"
    except requests.RequestException: 
        sys.exit("Error: Could not retrieve Bitcoin price.")
            #handling request exceptions - network issues, invalid responses, etc.
    except (KeyError, ValueError): 
        sys.exit("Error: Unexpected response format from API.")
            #handling data extraction exceptions - missing keys or invalid data types

    # Calculate total cost
    total_cost = n * price

    # Output the cost formatted with commas and four decimal places
    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main() 
