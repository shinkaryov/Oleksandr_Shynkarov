import requests
import json


class Tester:

    def __init__(self, access_token, file, path):
        self.access_token = access_token
        self.file = file
        self.path = path

    def upload(self):
        url = 'https://content.dropboxapi.com/2/files/upload'
        headers = {'Authorization': f'Bearer {self.access_token}',
                   'Dropbox-API-Arg': json.dumps({'mode': 'add',
                                                  'autorename': True,
                                                  'mute': False,
                                                  'strict_conflict': False,
                                                  'path': f'/{self.file}'}),
                   'Content-Type': 'application/octet-stream'}
        with open(self.path, 'rb') as file:
            data_file = file.read()
            return requests.post(url=url, headers=headers, data=data_file)

    def get_metadata(self):
        url = 'https://api.dropboxapi.com/2/files/alpha/get_metadata'
        headers = {'Authorization': f'Bearer {self.access_token}',
                   'Content-Type': 'application/json'}
        data = json.dumps({'path': f'/{self.file}'})
        return requests.post(url=url, headers=headers, data=data)

    def delete(self):
        url = 'https://api.dropboxapi.com/2/files/delete'
        headers = {'Authorization': f'Bearer {self.access_token}',
                   'Content-Type': 'application/json'}
        data = json.dumps({'path': f'/{self.file}'})
        return requests.post(url, headers=headers, data=data)
