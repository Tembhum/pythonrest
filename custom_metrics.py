# Import the necessary libraries
from datadog import initialize, statsd
import requests
import time
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('API_KEY')
app_key=os.getenv('APP_KEY')

# Initialize the Datadog client with your API and application keys
options = {
    'api_key': api_key,
    'app_key': app_key
}

initialize(**options)

# Function to simulate fetching data from your HTTPD server
def fetch_server_data():
    # Replace with your server's URL or specific endpoint
    response = requests.get("http://localhost")
    return response

# Main function to send custom metrics
def send_custom_metrics():
    while True:
        response = fetch_server_data()

        # Check if the HTTP request was successful
        if response.status_code == 200:
            # Send a metric for a successful request
            statsd.increment('httpd.request.success.count', tags=["environment:dev"])
            print("sent increment")
            # Send a gauge for the response time
            statsd.gauge('httpd.response.time', response.elapsed.total_seconds())
        else:
            # Send a metric for a failed request
            statsd.increment('httpd.request.failure.count', tags=["environment:dev"])

        # Wait for a specified interval (in seconds) before sending the next metric
        time.sleep(120)  # Adjust this interval as needed

# Replace this with your actual server-checking logic
if __name__ == "__main__":
    send_custom_metrics()
