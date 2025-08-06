import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from ytshortsgenerator.config import settings

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def get_saved_credentials(token_path="youtube_token.json"):
    if os.path.exists(token_path):
        return Credentials.from_authorized_user_file(token_path, SCOPES)

    client_config = {
      "installed": {
        "client_id": settings.youtube_client_id,
        "client_secret": settings.youtube_client_secret,
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob","http://localhost"]
      }
    }

    flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
    creds = flow.run_local_server(port=0)
    with open(token_path, "w", encoding="utf-8") as f:
        f.write(creds.to_json())
    return creds
