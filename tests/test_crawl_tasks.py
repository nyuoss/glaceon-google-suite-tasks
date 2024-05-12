import pytest
import os
from src import *
from src.open_source_python_template.crawlTasks import get_tasks
from unittest.mock import patch, mock_open, MagicMock, PropertyMock
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Sample data for mocking responses
MOCK_TASKS = {
    "items": [
        {"title": "Task 1", "id": "1", "tasklist_id": "tl1", "tasklist_title": "TaskList 1"}
    ]
}

MOCK_TASKLISTS = {
    "items": [
        {"title": "TaskList 1", "id": "tl1"}
    ]
}

def test_get_tasks_existing_token_valid():
    with patch('os.path.exists', return_value=True), \
         patch('google.oauth2.credentials.Credentials.from_authorized_user_file') as mock_cred, \
         patch('googleapiclient.discovery.build') as mock_build:
        
        mock_cred.return_value.valid = True
        mock_cred.return_value.universe_domain = 'googleapis.com'

        # Mock Google API client setup
        mock_service = MagicMock()
        mock_build.return_value = mock_service
        mock_cred.return_value.valid = True

        # Setup Google API client mock
        mock_service = MagicMock()
        mock_build.return_value = mock_service
        mock_service.tasklists().list().execute.return_value = MOCK_TASKLISTS
        mock_service.tasks().list().execute.return_value = MOCK_TASKS

        # Execute function
        results = get_tasks()
        
        # Assert results
        assert len(results) == 1
        assert results[0]['title'] == "Task 1"

def test_get_tasks_existing_token_expired():
    with patch('os.path.exists', return_value=True), \
         patch('google.oauth2.credentials.Credentials.from_authorized_user_file') as mock_cred, \
         patch('google.auth.transport.requests.Request'), \
         patch('googleapiclient.discovery.build') as mock_build, \
         patch('builtins.open', mock_open()):

        # Setup mock credentials
        mock_cred.return_value.valid = False
        mock_cred.return_value.expired = True
        mock_cred.return_value.refresh_token = True

        # Refresh method does nothing but update valid state
        def refresh(request):
            mock_cred.return_value.valid = True

        mock_cred.return_value.refresh = refresh

        # Setup Google API client mock
        mock_service = mock_build.return_value
        mock_tasklists = mock_service.tasklists().list().execute.return_value = MOCK_TASKLISTS
        mock_tasks = mock_service.tasks().list().execute.return_value = MOCK_TASKS

        # Execute function
        results = get_tasks()
        
        # Assert results
        assert len(results) == 1
        assert results[0]['title'] == "Task 1"

def test_get_tasks_no_tasklists():
    with patch('os.path.exists', return_value=True), \
         patch('google.oauth2.credentials.Credentials.from_authorized_user_file') as mock_cred, \
         patch('googleapiclient.discovery.build') as mock_build:

        # Setup mock credentials
        mock_cred.return_value.valid = True

        # Setup Google API client mock
        mock_service = mock_build.return_value
        mock_service.tasklists().list().execute.return_value = {"items": []}  

        # Execute function
        results = get_tasks()

        # Assert results
        assert results == []