# Todo App with FastAPI, Poetry, Neon Database, SQLModel, Python, and PostgreSQL

This Todo App is a robust task management system developed using FastAPI, Poetry, Neon Database, SQLModel, Python, and PostgreSQL. It provides a seamless experience for managing tasks efficiently.

## Technologies Used

- **FastAPI**: FastAPI is a modern, high-performance web framework for building APIs with Python 3.7+.
- **Poetry**: Poetry is a dependency management and packaging tool for Python projects, ensuring reproducible builds and simplified dependency management.
- **Neon Database**: Neon offers PostgreSQL as a managed service with easy setup and scalability options, providing a reliable database solution.
- **SQLModel**: SQLModel facilitates the usage of SQL databases with Python dataclasses, enhancing database interaction and management.
- **Python**: Python is a powerful, versatile programming language known for its simplicity and readability, serving as the foundation for this application.
- **PostgreSQL**: PostgreSQL is a robust, open-source object-relational database system, ensuring data integrity and performance.

## Setup

1. **Install Dependencies**
   ```bash
   pipx install fastapi poetry psycopg2-binary
   ```

2. **Neon Database Setup**
   - Sign up for Neon Database service and create a PostgreSQL instance.
   - Obtain the connection URL for your database.

3. **Environment Configuration**
   - Ensure you have a `.env` file with the necessary configuration variables:
     ```
     DATABASE_URL=your_postgresql_connection_url
     TEST_DATABASE_URL=your_test_postgresql_connection_url
     ```

4. **Run the Application**
   ```bash
   poetry run uvicorn foldername.filename:app --port 8000 --reload
   ```

## API Endpoints

- **GET /**: Root endpoint of the Todo App.
- **POST /todos**: Add a new Todo item.
- **GET /todos/{todo_id}**: Retrieve a Todo item by ID.
- **PUT /todos/{todo_id}**: Update a Todo item.
- **DELETE /todos/{todo_id}**: Delete a Todo item.

## Usage

- **Adding a Todo**
  - Endpoint: `POST /todos`
  - Request Body:
    ```json
    {
        "todo": "Your todo content here",
        "status": false
    }
    ```
  - Response: `{'id': 1, 'todo': 'Your todo content here', 'status': false}`


## Conclusion

This Todo App offers a reliable solution for managing tasks efficiently. Leveraging FastAPI, Poetry, Neon Database, SQLModel, Python, and PostgreSQL, it ensures high performance, scalability, and reliability. Feel free to explore, customize, and utilize this codebase for your projects.
