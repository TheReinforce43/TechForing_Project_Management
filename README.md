# Project Management API

This project is a RESTful API for managing users, projects, tasks, and comments using Django and Django REST Framework.

## Features

- User registration, login, and management
- Project creation, retrieval, update, and deletion
- Task management within projects
- Commenting on tasks

## Endpoints

### Users

- **Register User**: `POST /api/users/register/`
- **Login User**: `POST /api/users/login/`
- **Get User Details**: `GET /api/users/{id}/`
- **Update User**: `PUT/PATCH /api/users/{id}/`
- **Delete User**: `DELETE /api/users/{id}/`

### Projects

- **List Projects**: `GET /api/projects/`
- **Create Project**: `POST /api/projects/`
- **Retrieve Project**: `GET /api/projects/{id}/`
- **Update Project**: `PUT/PATCH /api/projects/{id}/`
- **Delete Project**: `DELETE /api/projects/{id}/`

### Tasks

- **List Tasks**: `GET /api/projects/{project_id}/tasks/`
- **Create Task**: `POST /api/projects/{project_id}/tasks/`
- **Retrieve Task**: `GET /api/tasks/{id}/`
- **Update Task**: `PUT/PATCH /api/tasks/{id}/`
- **Delete Task**: `DELETE /api/tasks/{id}/`

### Comments

- **List Comments**: `GET /api/tasks/{task_id}/comments/`
- **Create Comment**: `POST /api/tasks/{task_id}/comments/`
- **Retrieve Comment**: `GET /api/comments/{id}/`
- **Update Comment**: `PUT/PATCH /api/comments/{id}/`
- **Delete Comment**: `DELETE /api/comments/{id}/`

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Documentation

You can use tools like Swagger or Postman to document and test the API. 

## License

This project is licensed under the MIT License.
