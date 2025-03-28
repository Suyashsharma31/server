import requests
import time

URL = "https://vegetable-classifier.onrender.com/"  # Your Render website

while True:
    try:
        response = requests.get(URL)
        print(f"Pinged {URL} - Status: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")
    
    time.sleep(40)  # Ping every 5 minutes (adjust if needed)
