from src.open_source_python_template.crawlTasks import get_tasks
from unittest.mock import patch, mock_open, MagicMock

# Sample data for mocking responses
MOCK_TASKS = {
    "items": [
        {
            "title": "Task 1",
            "id": "1",
            "tasklist_id": "tl1",
            "tasklist_title": "TaskList 1",
        }
    ]
}

MOCK_TASKLISTS = {"items": [{"title": "TaskList 1", "id": "tl1"}]}


def test_get_tasks_existing_token_valid():
    with (
        patch("os.path.exists", return_value=True),
        patch(
            "google.oauth2.credentials.Credentials.from_authorized_user_file"
        ) as mock_cred,
        patch("googleapiclient.discovery.build") as mock_build,
    ):
        mock_cred.return_value.valid = True
        mock_cred.return_value.universe_domain = "googleapis.com"

        mock_service = MagicMock()
        mock_build.return_value = mock_service
        mock_cred.return_value.valid = True

        mock_service = MagicMock()
        mock_build.return_value = mock_service
        mock_service.tasklists().list().execute.return_value = MOCK_TASKLISTS
        mock_service.tasks().list().execute.return_value = MOCK_TASKS

        results = get_tasks()

        assert len(results) == 1
        assert results[0]["title"] == "Task 1"


def test_get_tasks_existing_token_expired():
    with (
        patch("os.path.exists", return_value=True),
        patch(
            "google.oauth2.credentials.Credentials.from_authorized_user_file"
        ) as mock_cred,
        patch("google.auth.transport.requests.Request"),
        patch("googleapiclient.discovery.build") as mock_build,
        patch("builtins.open", mock_open()),
    ):
        mock_cred.return_value.valid = False
        mock_cred.return_value.expired = True
        mock_cred.return_value.refresh_token = True

        def refresh(request):
            mock_cred.return_value.valid = True

        mock_cred.return_value.refresh = refresh

        mock_service = mock_build.return_value
        mock_service.tasklists().list().execute.return_value = MOCK_TASKLISTS
        mock_service.tasks().list().execute.return_value = MOCK_TASKS

        results = get_tasks()

        assert len(results) == 1
        assert results[0]["title"] == "Task 1"


def test_get_tasks_no_tasklists():
    with (
        patch("os.path.exists", return_value=True),
        patch(
            "google.oauth2.credentials.Credentials.from_authorized_user_file"
        ) as mock_cred,
        patch("googleapiclient.discovery.build") as mock_build,
    ):
        mock_cred.return_value.valid = True

        mock_service = mock_build.return_value
        mock_service.tasklists().list().execute.return_value = {"items": []}

        results = get_tasks()

        assert results == []
