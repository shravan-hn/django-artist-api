# django-artist-api

## Introduction

The Artist Portfolio API is a Django REST Framework project designed to manage artist profiles and their works. It allows for CRUD operations on artist data and works, ensuring secure access through token-based authentication.

## Setup

To get the project up and running on your local machine, follow these steps:

### Prerequisites

- Python 3.x
- pip
- Virtual environment (recommended)

### Installation

1. **Clone the Repository**
   ```
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

2. **Set Up a Virtual Environment** (Optional but recommended)
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Database Migrations**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser**
   ```
   python manage.py createsuperuser
   ```

6. **Run the Server**
   ```
   python manage.py runserver
   ```


## Usage

Once the server is running, you can start using the API.

### Endpoints

1. **User Registration and Authentication**
   - Register: `POST /api/users/register/`
   - Obtain Token: `POST /api/token/`
   - Refresh Token: `POST /api/token/refresh/`

2. **Artists**
   - List: `GET /api/artists/`
   - Create: `POST /api/artists/`
   - Retrieve: `GET /api/artists/{id}/`
   - Update: `PUT /api/artists/{id}/`
   - Delete: `DELETE /api/artists/{id}/`

3. **Works**
   - List: `GET /api/works/`
   - Create: `POST /api/works/`
   - Retrieve: `GET /api/works/{id}/`
   - Update: `PUT /api/works/{id}/`
   - Delete: `DELETE /api/works/{id}/`
   - Filter by Type: `GET /api/works/?work_type=YT`

### Authentication

To access the protected endpoints, include the token in the header of your request:


Authorization: Bearer <Your-Token>

## Examples

Here are some example requests to get you started:

### Register a User

Request:
```
curl -X POST http://127.0.0.1:8000/api/users/register/ \
     -H "Content-Type: application/json" \
     -d '{"username": "newuser", "password": "password123", "email": "newuser@example.com"}'
```

Response:
```
{
  "username": "newuser",
  "email": "newuser@example.com"
}
```


#### Troubleshooting


## Troubleshooting

If you encounter any issues, check the following:

- Ensure the Django server is running.
- Verify that all environment variables are set correctly.
- Check for error messages in the server logs.





