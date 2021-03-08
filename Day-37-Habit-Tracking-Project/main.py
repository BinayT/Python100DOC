import requests

USERNAME = 'binay'
Token = "binaytoken"
GRAPH_ID = "graph1"


pixela_endpoint = 'https://pixe.la/v1/users'

create_user_params = {
    "token": "binaytoken",
    "username": "binay",
    "agreeTermsOfService": "yes",
    "notMinor": 'yes'
}

# response = requests.post(url=pixela_endpoint, json=create_user_params)
# print(response.text)

graph_config = {
    "id": "graph1",
    "name": "My Graph",
    "unit": "minute",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": Token
}

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

# post_graph = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(post_graph.text)

pixel_params = {
    'date': '20200309',
    'quantity': '20'
}

pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

post_pixel = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(post_pixel.text)
