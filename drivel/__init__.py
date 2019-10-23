from __future__ import print_function
import pickle
import sys
import os.path
import io 
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload


def drlist(file_path, number=10):
    service = worker(file_path)
    service.print_list(number)
       
def drget(file_path, file_name):
    service = worker(file_path)
    service.dl_file(file_name)

class worker(): 
    def __init__(self, file_path):
        self.client = drive_client(file_path)

    def print_list(self, number):
        file_list = self.client.list_all_files()[:int(number)]
        for item in file_list:    
            print('{0} - {1} - {2}'.format(
                item['name'], 
                item['id'], 
                item['mimeType'], 
                ))

    def dl_file(self, file_name):
        file_list = self.client.list_all_files()
        for item in file_list:
            if file_name == item['name']:
                self.client.download_file(file_name, item['id'])



class drive_client():
    def __init__(self, file_path):
        # If modifying these scopes, delete the file token.pickle.
        self.SCOPES = ['https://www.googleapis.com/auth/drive']
        self.SERVICE = None
        self.file_path = file_path[:-11]
        self.login()
    
    def login(self):
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(str(self.file_path) + 'creds/token.pickle'):
            with open(str(self.file_path) + 'creds/token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(str(self.file_path) + 'creds/credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(str(self.file_path) + 'creds/token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        self.SERVICE = build('drive', 'v3', credentials=creds)

    def download_file(self, name, id_of_file):
        file_id = id_of_file 
        request = self.SERVICE.files().export_media(fileId=file_id, mimeType='text/plain')
        fh = io.FileIO(name, 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print ("Download %d%%." % int(status.progress() * 100))

    def list_all_files(self):
        result = []
        page_token = None
        while True:
            try:
                param = {}
                if page_token:
                    param['pageToken'] = page_token
                files = self.SERVICE.files().list(**param).execute()
                result.extend(files['files'])
                page_token = files.get('nextPageToken')
                if not page_token:
                    break
            except errors.HttpError as error:
                print ('An error occurred: %s' % error)
                break
        return result

