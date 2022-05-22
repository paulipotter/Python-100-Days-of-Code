import requests, os
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'
USER = os.environ.get('PIXELA_USER')
TOKEN = os.environ.get('PIXELA_TOKEN')
GRAPH_ID = 'graph2'

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

## POST - Create a new user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Pages Read",
    "unit": "Pages",
    "type": "int",
    "color": "shibafu"
}

# Use headers for more security 🔐
headers = {
    "X-USER-TOKEN": TOKEN
}

# Create a new graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}"

# Get today's date
today = datetime.now()

pixel_data = {
    # Format the day according to the api doc requirements
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages did you read today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)
