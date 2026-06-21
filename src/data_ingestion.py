import json
from dataclasses import dataclass
from datetime import datetime
import os
from typing import List

@dataclass
class Document:
    file_name: str
    owner: str
    last_modified_date: str
    extracted_text: str

class DataIngestion:
    def __init__(self):
        self.documents = []

    def parse_document(self, file_path: str, file_name: str, owner: str, last_modified_date: str) -> Document:
        if file_path.endswith('.pdf'):
            # For simplicity, assume PDF text extraction is done elsewhere
            extracted_text = 'PDF text extraction not implemented'
        elif file_path.endswith('.docx'):
            # For simplicity, assume DOCX text extraction is done elsewhere
            extracted_text = 'DOCX text extraction not implemented'
        elif file_path.endswith('.txt'):
            with open(file_path, 'r') as file:
                extracted_text = file.read()
        else:
            raise ValueError('Unsupported file type')
        return Document(file_name, owner, last_modified_date, extracted_text)

    def store_document(self, document: Document):
        self.documents.append(document)

    def get_documents(self) -> List[Document]:
        return self.documents

class OAuthIntegration:
    def __init__(self):
        self.access_tokens = {}

    def get_access_token(self, service: str) -> str:
        # For simplicity, assume access tokens are stored in memory
        if service not in self.access_tokens:
            self.access_tokens[service] = 'access_token_' + service
        return self.access_tokens[service]

    def authenticate(self, service: str) -> bool:
        # For simplicity, assume authentication is done elsewhere
        return True

class GoogleDriveIntegration:
    def __init__(self, oauth_integration: OAuthIntegration):
        self.oauth_integration = oauth_integration

    def get_files(self) -> List[str]:
        # For simplicity, assume file retrieval is done elsewhere
        return ['file1.pdf', 'file2.docx', 'file3.txt']

class DropboxIntegration:
    def __init__(self, oauth_integration: OAuthIntegration):
        self.oauth_integration = oauth_integration

    def get_files(self) -> List[str]:
        # For simplicity, assume file retrieval is done elsewhere
        return ['file4.pdf', 'file5.docx', 'file6.txt']

def main():
    oauth_integration = OAuthIntegration()
    google_drive_integration = GoogleDriveIntegration(oauth_integration)
    dropbox_integration = DropboxIntegration(oauth_integration)
    data_ingestion = DataIngestion()
    google_drive_files = google_drive_integration.get_files()
    dropbox_files = dropbox_integration.get_files()
    for file in google_drive_files + dropbox_files:
        if file.endswith('.pdf') or file.endswith('.docx') or file.endswith('.txt'):
            document = data_ingestion.parse_document(file, file, 'owner', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            data_ingestion.store_document(document)
    documents = data_ingestion.get_documents()
    for document in documents:
        print(json.dumps(document.__dict__))

if __name__ == '__main__':
    main()
