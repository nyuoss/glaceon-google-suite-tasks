from flask import Flask, jsonify
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

app = Flask(__name__)

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/tasks.readonly"]


@app.route("/get-tasks", methods=["GET"])
def get_tasks():
    """Endpoint to get tasks from Google Tasks API and return them as JSON."""
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "src/open_source_python_template/credential.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(creds.to_json())

    try:
        service = build("tasks", "v1", credentials=creds)
        results = service.tasklists().list(maxResults=10).execute()
        tasklists = results.get("items", [])

        tasks_response = []
        if tasklists:
            for tasklist in tasklists:
                tasks = service.tasks().list(tasklist=tasklist["id"]).execute()
                tasks_items = tasks.get("items", [])
                for task in tasks_items:
                    tasks_response.append(
                        {
                            "title": task["title"],
                            "id": task["id"],
                            "tasklist_id": tasklist["id"],
                            "tasklist_title": tasklist["title"],
                        }
                    )

        return jsonify(tasks_response)
    except HttpError as err:
        return jsonify({"error": str(err)}), 500


if __name__ == "__main__":
    app.run(debug=True)
