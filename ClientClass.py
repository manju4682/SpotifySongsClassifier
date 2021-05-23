import base64
import datetime
from urllib.parse import urlencode
import requests
import json

class SpotifyAPI(object):

    token_url = "https://accounts.spotify.com/api/token"
    
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None
        self.access_token_expires = None
        self.access_token_did_expire = True

    def get_client_credentials(self):
        
        #Returns a base64 encoded string
        if self.client_secret == None or self.client_id == None:
            raise Exception("You must set client_id and client_secret")
        client_creds = f"{self.client_id}:{self.client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()
    
    def get_token_headers(self):
        client_creds_b64 = self.get_client_credentials()
        return {
            "Authorization": f"Basic {client_creds_b64}"
        }
    
    def get_token_data(self):
        return {
            "grant_type": "client_credentials"
        } 
    
    def perform_auth(self):
        token_url = self.token_url
        token_data = self.get_token_data()
        token_headers = self.get_token_headers()
        r = requests.post(token_url, data=token_data, headers=token_headers)
        if r.status_code not in range(200, 299):
            raise Exception("Could not authenticate client.")
            # return False
        data = r.json()
        now = datetime.datetime.now()
        access_token = data['access_token']
        expires_in = data['expires_in'] # seconds
        expires = now + datetime.timedelta(seconds=expires_in)
        self.access_token = access_token
        self.access_token_expires = expires
        self.access_token_did_expire = expires < now
        return True
    
    def get_access_token(self):
        token = self.access_token
        expires = self.access_token_expires
        now = datetime.datetime.now()
        if token == None:
            self.perform_auth()
            return self.get_access_token()
        elif expires < now:
            self.perform_auth()
            return self.get_access_token()
         
        return token
    
    def get_resource_header(self):
        access_token = self.get_access_token()
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        return headers
        
        
    def get_resource(self, lookup_id,offset,limit,resource_type='playlists', version='v1'):
        endpoint = f"https://api.spotify.com/{version}/{resource_type}/{lookup_id}/tracks?offset={offset}&limit={limit}"
        headers = self.get_resource_header()
        r = requests.get(endpoint, headers=headers)
        if r.status_code not in range(200, 299):
            return {}
        return r.json()

    def get_audio_features(self,songs_ids, resource_type='audio-features', version='v1' ):
        endpoint = f"https://api.spotify.com/{version}/{resource_type}?ids={songs_ids}"
        headers = self.get_resource_header()
        r = requests.get(endpoint, headers=headers)
        if r.status_code not in range(200, 299):
            return {}
        return r.json()

       
    