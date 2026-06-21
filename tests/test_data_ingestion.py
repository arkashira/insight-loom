import pytest
import os
from src.data_ingestion import DataIngestion, Document, OAuthIntegration, GoogleDriveIntegration, DropboxIntegration

def test_parse_document_pdf():
    data_ingestion = DataIngestion()
    document = data_ingestion.parse_document('file.pdf', 'file.pdf', 'owner', '2022-01-01 12:00:00')
    assert document.file_name == 'file.pdf'
    assert document.owner == 'owner'
    assert document.last_modified_date == '2022-01-01 12:00:00'
    assert document.extracted_text == 'PDF text extraction not implemented'

def test_parse_document_docx():
    data_ingestion = DataIngestion()
    document = data_ingestion.parse_document('file.docx', 'file.docx', 'owner', '2022-01-01 12:00:00')
    assert document.file_name == 'file.docx'
    assert document.owner == 'owner'
    assert document.last_modified_date == '2022-01-01 12:00:00'
    assert document.extracted_text == 'DOCX text extraction not implemented'

def test_parse_document_txt():
    data_ingestion = DataIngestion()
    with open('test.txt', 'w') as file:
        file.write('Hello World')
    document = data_ingestion.parse_document('test.txt', 'test.txt', 'owner', '2022-01-01 12:00:00')
    assert document.file_name == 'test.txt'
    assert document.owner == 'owner'
    assert document.last_modified_date == '2022-01-01 12:00:00'
    assert document.extracted_text == 'Hello World'
    os.remove('test.txt')

def test_parse_document_unsupported():
    data_ingestion = DataIngestion()
    with pytest.raises(ValueError):
        data_ingestion.parse_document('file.mp3', 'file.mp3', 'owner', '2022-01-01 12:00:00')

def test_store_document():
    data_ingestion = DataIngestion()
    document = Document('file.txt', 'owner', '2022-01-01 12:00:00', 'Hello World')
    data_ingestion.store_document(document)
    assert len(data_ingestion.get_documents()) == 1

def test_get_documents():
    data_ingestion = DataIngestion()
    document1 = Document('file1.txt', 'owner', '2022-01-01 12:00:00', 'Hello World')
    document2 = Document('file2.txt', 'owner', '2022-01-01 12:00:00', 'Hello World')
    data_ingestion.store_document(document1)
    data_ingestion.store_document(document2)
    assert len(data_ingestion.get_documents()) == 2
