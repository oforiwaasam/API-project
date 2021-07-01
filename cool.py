import requests
import spotipy

CLIENT_ID = '32289377e7b3432a9b90c1af5250e1ce'
CLIENT_SECRET = '282d8ab89e854171a121b076fd2ade49'

AUTH_URL = 'https://accounts.spotify.com/api/token'
# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

print(auth_response.status_code)

auth_response_data = auth_response.json()

print(auth_response_data)

access_token = auth_response_data['access_token']
