import requests
import json

def get_data():
    response = requests.get('http://localhost:3000/data')
    if response.status_code == 200:
        return response.json()
    else:
        return 'Error: Unable to fetch data'

if __name__ == "__main__":
    
    data = get_data()
    print(data)
    # datajson = json.load(data)
    # print(datajson['message'])

