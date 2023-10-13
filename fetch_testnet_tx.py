import requests
import time

# Function to fetch and print the latest transactions from the Bitcoin testnet
def fetch_latest_transactions():
    # API endpoint for the latest transactions on the Bitcoin testnet
    url = "https://api.blockchain.info/testnet3/transactions?format=json"
    
    try:
        # Sending a request to the API and getting the response
        response = requests.get(url)
        
        # Checking if the request was successful (status code 200)
        if response.status_code == 200:
            # Parsing the JSON response
            transactions = response.json()
            
            # Looping through the transactions and printing details
            for tx in transactions:
                print(f"Transaction Hash: {tx['hash']}")
                print(f"Time: {tx['time']}")
                print(f"Size: {tx['size']} bytes")
                print(f"Inputs: {len(tx['inputs'])}, Outputs: {len(tx['outputs'])}")
                print("\n-----\n")
        else:
            print(f"Failed to retrieve data: {response.status_code}")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Polling for new transactions every 60 seconds
while True:
    print("Fetching latest transactions...\n")
    fetch_latest_transactions()
    time.sleep(60)