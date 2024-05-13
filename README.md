# Google Suite Tasks Dashboard

## Project's purpose
The objective of the Google Suite Tasks Dashboard is to provide Google users with a centralized platform to efficiently manage tasks across the Google Task and Google Docs applications. By creating this solution, users can easily access and track their tasks in one location.

## Features
1. Extract tasks from Google Docs.
2. View-only dashboard for user's tasks.
3. Crawling tasks directly from Google Tasks API.

## Installation instructions
1. Clone the repository [glaceon-google-suite-tasks](https://github.com/nyuoss/glaceon-google-suite-tasks).
2. Install PDM as package and dependency manager if it has not been installed.

    `pdm install --dev`

3. Install dependencies:

    `pdm install --dev`

4. To update dependencies, run the following:

    `pdm update`

5. To connect AWS RDS through SSH, run the command with postgresql database installed 

```bash
psql -h opensource-db.chwy4eqkclzc.us-east-1.rds.amazonaws.com -p 5432 -U postgres -d task-db
```

6. To create the table in the database (please connect Fan(fy2187@nyu.edu) for database password )
        
    `create_databse.sql`

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

### Getting Started
The below is an overview of how the project is structured. We recommend going through this section to have a basic understanding of where feature-related code files are located before making a contribution.
#### Backend
Entry point of the Flask application is `src/open_source_python_template/__init__.py`.

Methods for crawling tasks from Google Sheet API is defined in `src/open_source_python_template/crawlTasks.py`.

App Script for extracting tasks from Google Docs is `src/open_source_python_template/extractTasks.js`.

#### Frontend
Frontend HTML templates can be found in `templates/` folder, such as `index.html`.

Static elements, scripts, and styles can be found in `static/` folder, such as `style.css`.

### Testing
#### Frontend tests
Before running frontend tests, ensure you have [Chrome Driver](https://chromedriver.chromium.org/downloads) installed and updated to latest version. Then run the following command:

    pdm run pytest tests/test_index.py

### Backend tests [Work in Progress]
Run the following command to run backend tests:

    pdm run pytest tests/test_crawl_tasks.py

### Making Contributions
### Issues
1. Create an Issue: Before you make significant changes or improvements, please check if an existing issue already addresses your concern. If not, submit a new issue providing as much relevant information as possible.
2. Discuss: Participation in issue discussion is highly encouraged. Share your thoughts, suggestions, and ways to resolve issues.

### Pull Requests
1. Create a Branch: Always create a new branch for your work. It should be named appropriately based on the nature of the change (e.g., feature-add-login, bugfix-address-crash).
2. Make Your Changes: Perform your changes or additions in your branch, adhering to the coding standards and documentation style of the project.
3. Write Tests: Ensure that your changes are covered by tests, which help in maintaining code quality and robustness.
4. Document Your Changes: Update `README.md` with details of changes to the interface, this includes new dependencies, useful file locations, and connected components.
5. Pull Request: Push your changes to your fork and submit a pull request (PR) to the original repository. It should describe the changes, reference the issues they affect, and note any specific areas where you would like feedback. Please use our PR template for documentation.
6. Code Review: Wait for the project maintainers to review your PR. Be open to making changes based on feedback.

### Style Guides
Please follow the coding style and conventions that are used in the project. We have setup a CI/CD pipeline to check for coding styles, please refrain from raising a PR if the formatter returns an error and make fixes accordingly to comply.