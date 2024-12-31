# Project Management API

This project is a RESTful API for managing users, projects, tasks, and comments using Django and Django REST Framework.

## Features

- User registration, login, and management
- Project creation, retrieval, update, and deletion
- Task management within projects
- Commenting on tasks

## Endpoints

### Users

- **Register User**: `POST /user/users/signup/`
- **Login User**: `POST /user/users/login/`
- **Get User Details**: `GET /api/user/users/{id}/`
- **Update User**: `PUT/api/user/users/{id}/`
- **Delete User**: `DELETE /api/user/users/{id}/`

### Projects

- **List Projects**: `GET /api/projects/`
- **Create Project**: `POST /api/projects/`
- **Retrieve Project**: `GET /api/projects/{id}/`
- **Update Project**: `PUT/PATCH /api/projects/{id}/`
- **Delete Project**: `DELETE /api/projects/{id}/`

### Tasks

- **List Tasks**: `GET /api/projects/projects/{project_id}/tasks/`  
- **Create Task**: `POST /api/projects/projects/{project_id}/tasks/`
- **Retrieve Task**: `GET /api/tasks/{id}/`
- **Update Task**: `PUT/PATCH /api/tasks/{id}/`
- **Delete Task**: `DELETE /api/tasks/{id}/`

### Comments

- **List Comments**: `GET /api/tasks/tasks/{task_id}/comments/`
- **Create Comment**: `POST /api/tasks/tasks/{task_id}/comments/`
- **Retrieve Comment**: `GET /api/comments/{id}/`
- **Update Comment**: `PUT/PATCH /api/comments/{id}/`
- **Delete Comment**: `DELETE /api/comments/{id}/`

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/TheReinforce43/TechForing_Project_Management.git
    cd techforing_backend
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv\Scripts\activate
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

I have used Postman to document and test the API. 


