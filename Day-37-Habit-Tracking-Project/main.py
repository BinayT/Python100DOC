import requests
from datetime import datetime as dt

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
today_date = dt.now().strftime('%Y%m%d')

pixel_params = {
    'date': today_date,
    'quantity': '50'
}
delete_date = '20200308'

pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'
delete_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{delete_date}'
put_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_date}'

# post_pixel = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(post_pixel.text)

# delete_pixel = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(delete_pixel.text)

put_pixel_params = {
    "quantity": "90"
}

put_pixel = requests.put(url=put_pixel_endpoint, json=put_pixel_params, headers=headers)
print(put_pixel.text)