import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/tasks.readonly"]


def main():
    """Shows basic usage of the Tasks API.
    Prints the title and ID of the first 10 task lists.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credential.json", SCOPES)
            creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(creds.to_json())

    try:
        service = build("tasks", "v1", credentials=creds)

        # Call the Tasks API to fetch task lists
        results = service.tasklists().list(maxResults=10).execute()
        tasklists = results.get("items", [])

        if not tasklists:
            print("No task lists found.")
            return

        print("Task lists:")
        for tasklist in tasklists:
            print(f"{tasklist['title']} ({tasklist['id']})")
            # Fetch tasks for each tasklist
            tasks = service.tasks().list(tasklist=tasklist["id"]).execute()
            tasks_items = tasks.get("items", [])
            if not tasks_items:
                print("  No tasks found.")
            else:
                for task in tasks_items:
                    # Use .get() to safely access dictionary keys
                    title = task.get(
                        "title", "No Title"
                    )  # Provide a default value if 'title' key doesn't exist
                    due = task.get(
                        "due", "No Due Date"
                    )  # Provide a default value if 'due' key doesn't exist
                    notes = task.get(
                        "notes", "No Description"
                    )  # Provide a default value if 'notes' key doesn't exist
                    print(f"Task: {title} \n Due: {due} \n Description: {notes}")
    except HttpError as err:
        print(err)


if __name__ == "__main__":
    main()