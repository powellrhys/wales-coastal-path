from functions.connect import authorization, get_access_token
from functions.data import get_data, get_segment_data

from dotenv import load_dotenv
import webbrowser
import json
import os

# Load Environment Variables
load_dotenv()
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

# Authorise User
redirect_uri = 'http://localhost/'
request_url = authorization(client_id, redirect_uri)
webbrowser.open(request_url)

# Prompt user to input refresh token
code = input('insert code here: ')

# Retrieve access token for user
access_token = get_access_token(client_id, client_secret, code)

# Retrieve list of starred segments
segment_data = []
for page_number in range(1, 11):
    page_data = get_data(access_token, "https://www.strava.com/api/v3/segments/starred", page=page_number)
    if page_data == []:
        break
    segment_data = segment_data + page_data

# Filter out segments not related to the welsh coastal path
welsh_coastal_path_segments = [activity for activity in segment_data if 'WCP' in activity['name']]

# Append polyline data to each segment entry
welsh_coastal_path_segment_data = []
for segment in welsh_coastal_path_segments:
    segment_data = get_segment_data(segment['id'], access_token)
    segment['polyline'] = segment_data['map']['polyline']
    welsh_coastal_path_segment_data.append(segment)

# Upload data to local file storage
with open('welsh_coastal_path_segments.json', 'w') as f:
    json.dump(welsh_coastal_path_segments, f)
