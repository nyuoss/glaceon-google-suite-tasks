CREATE TABLE comments_with_assigned_tasks (
    id SERIAL PRIMARY KEY,
    assignee VARCHAR(255) NOT NULL,
    assigner VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    quoted_file_content TEXT,
    created_time TIMESTAMPTZ NOT NULL,
    source_document_url TEXT NOT NULL
);


