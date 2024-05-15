import src.open_source_python_template.crawlTasks as crawlTasks
from unittest.mock import patch, MagicMock

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
        mock_cred.return_value = MagicMock(valid=True, universe_domain="googleapis.com")
        mock_service = MagicMock()
        mock_service.tasklists().list().execute.return_value = MOCK_TASKLISTS
        mock_service.tasks().list().execute.return_value = MOCK_TASKS
        mock_build.return_value = mock_service

        results = crawlTasks.get_tasks()

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
        patch("builtins.open", MagicMock()),
    ):
        mock_cred.return_value = MagicMock(
            valid=False,
            expired=True,
            refresh_token=True,
            universe_domain="googleapis.com",
        )
        mock_cred.return_value.refresh = MagicMock()

        mock_service = MagicMock()
        mock_service.tasklists().list().execute.return_value = MOCK_TASKLISTS
        mock_service.tasks().list().execute.return_value = MOCK_TASKS
        mock_build.return_value = mock_service

        results = crawlTasks.get_tasks()

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
        mock_cred.return_value = MagicMock(valid=True, universe_domain="googleapis.com")
        mock_service = MagicMock()
        mock_service.tasklists().list().execute.return_value = {"items": []}
        mock_build.return_value = mock_service

        results = crawlTasks.get_tasks()

        assert results == []


