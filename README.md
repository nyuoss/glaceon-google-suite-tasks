# Google Suite Tasks Dashboard

## Project's purpose
The objective of the Google Suite Tasks Dashboard is to provide Google users with a centralized platform to efficiently manage tasks across the Google Task and Google Docs applications. By creating this solution, users can easily access and track their tasks in one location.

## Features
1. Crawling tasks from Google Docs.
2. View-only dashboard for user's tasks.
3. Fetching tasks directly from Google Tasks API.

## Installation instructions
1. Clone the repository [glaceon-google-suite-tasks](https://github.com/nyuoss/glaceon-google-suite-tasks).
2. Install PDM as package and dependency manager if it has not been installed.

    `pdm install --dev`

3. Install dependencies:

    `pdm install --dev`

4. To update dependencies, run the following:

    `pdm update`

## Usage instructions
### Running Flask app
Change directory to `src/open_source_python_template` folder:

    cd src/open_source_python_template

Run Flask app via PDM:

    pdm run python __init__.py

Open browser and go to the following host address:

    http://127.0.0.1:5000

### Running Google Apps Script
1. Open a Google Docs document, click on Extensions -> Apps Script. A new Apps Script will be created.
2. From the left panel, select `Services` and add `Drive API`.
3. Copy and paste the code in `extractTasks.js` into `Code.gs` file in the Apps Script editor.
4. Run the script by clicking "Run".
5. When the script finishes execution, the comments with tasks assigned to the current use will be stored in a newly created Google Sheet.

## Contribution Guidelines

### Backend
Entry point of the Flask application is `__init__.py`.

### Frontend
Frontend HTML templates can be found in `templates/` folder, such as `index.html`.

Static elements and styles can be found in `static/` folder, such as `style.css`.
