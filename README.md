# FastAPI CRUD Application using SQLAlchemy & MySQL

A simple CRUD (Create, Read, Update, Delete) API built using FastAPI, SQLAlchemy ORM, and MySQL.

## Features

- Create books
- Get all books
- Update book details
- Delete books
- Database integration with MySQL
- Dependency Injection using Depends()
- ORM operations using SQLAlchemy
- Request validation using Pydantic

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- MySQL
- PyMySQL
- Pydantic
- Uvicorn

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /books | Create a new book |
| GET | /books | Get all books |
| PUT | /books/{book_id} | Update a book |
| DELETE | /books/{book_id} | Delete a book |

## Installation

### Clone Repository

```bash
git clone https://github.com/sindhurametla/your-repository-name.git
cd your-repository-name
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file and add:

```env
MYSQL_USER=your_username
MYSQL_PASSWORD=your_password
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DATABASE=your_database_name
```

## Run Server

```bash
uvicorn main:app --reload
```

## API Documentation

FastAPI automatically provides Swagger UI documentation:

```text
http://127.0.0.1:8000/docs
```

## Learning Outcomes

- FastAPI fundamentals
- CRUD operations
- SQLAlchemy ORM
- MySQL integration
- Dependency Injection
- Database session handling
- Pydantic validation

## Author

Sindura Metla

GitHub: https://github.com/sindhurametla/fastapi_sqlalchemy.git
