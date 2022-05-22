import requests, os

USER = os.environ.get('PIXELA_USER')
TOKEN = os.environ.get('PIXELA_TOKEN')
pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USER,
    'agreeTermsOfService':'yes',
    'notMinor': 'yes'
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)