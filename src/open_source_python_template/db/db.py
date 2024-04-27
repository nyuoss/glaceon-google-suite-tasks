from psycopg2 import pool
from datetime import datetime, timezone



class DBConfig:
    DATABASE_HOST = ""
    DATABASE_NAME = "task-db"
    DATABASE_USER = "postgres"
    DATABASE_PASSWORD = ""
    DATABASE_PORT = "5432"

class Database:

    connection_pool = pool.ThreadedConnectionPool(
        1,
        20,
        host=DBConfig.DATABASE_HOST,
        dbname=DBConfig.DATABASE_NAME,
        user=DBConfig.DATABASE_USER,
        password=DBConfig.DATABASE_PASSWORD,
        port=DBConfig.DATABASE_PORT,
    )

    def __init__(self):
        """Initialize the database connection from the connection pool."""
        self.conn = self.connection_pool.getconn()
        self.conn.autocommit = False
        self.cur = self.conn.cursor()

    def fetch_data(self, query):
        """Execute a query to fetch data from the database."""
        try:
            self.cur.execute(query)
            return self.cur.fetchall()
        except Exception as e:
            print("An error occurred while fetching data:", e)
            self.conn.rollback()

    def insert_data(self, query, params):
        """Insert data into the database using the provided query and parameters."""
        try:
            self.cur.execute(query, params)
            self.conn.commit()
            print("Data inserted successfully.")
        except Exception as e:
            print("An error occurred while inserting data:", e)
            self.conn.rollback()

    def close(self):
        """Close the database cursor and connection, return connection to the pool."""
        if self.cur is not None:
            self.cur.close()
            self.cur = None
        if self.conn is not None:
            self.connection_pool.putconn(self.conn, close=True)
            self.conn = None

    def insert_comment_task(
        self,
        assignee,
        assigner,
        content,
        quoted_file_content,
        created_time,
        source_document_url,
    ):
        """Insert a new comment with assigned task into the database."""
        query = """
        INSERT INTO comments_with_assigned_tasks (assignee, assigner, content, quoted_file_content, created_time, source_document_url)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        params = (
            assignee,
            assigner,
            content,
            quoted_file_content,
            created_time,
            source_document_url,
        )
        self.insert_data(query, params)


# test ...
if __name__ == "__main__":
    db = Database()
    try:
        now = datetime.now(timezone.utc)
        # INSERT:
        db.insert_comment_task(
            "test1", "test2", "test_content", "test", now, "http://example.com"
        )
        # Example of fetching data
        fetch_query = "SELECT * FROM comments_with_assigned_tasks"
        data = db.fetch_data(fetch_query)
        print(data)
    finally:
        db.close()
