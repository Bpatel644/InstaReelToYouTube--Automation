from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os

# Replace the placeholders with your own values
CLIENT_SECRETS_FILE = 'C:/Users/Dell/Desktop/scratches/client_secret_xxxxxxxxxxxxxxxxxxxxxxx.apps.googleusercontent.com.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

# Authenticate the user with the YouTube API
flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
credentials = flow.run_local_server(port=0)

# Build the YouTube API client
youtube = build(API_NAME, API_VERSION, credentials=credentials)

# Create a new video resource
request = youtube.videos().insert(
    part='snippet,status',
    body={
        'snippet': {
            'title': 'Modi is great',
            'description': 'This is a demo video',
            'tags': ['demo', 'test'],
            'categoryId': 22  # Replace with your own category ID
        },
        'status': {
            'privacyStatus': 'private'  # Replace with your desired privacy setting
        }
    },
    media_body=MediaFileUpload('C:/Users/Dell/Desktop/scratches/mp4.mp4')
)

# Execute the request to upload the video
response = None
try:
    response = request.execute()
except HttpError as e:
    print(f'An error occurred: {e}')
finally:
    if response is not None:
        print(f'Successfully uploaded video ID: {response["id"]}')
