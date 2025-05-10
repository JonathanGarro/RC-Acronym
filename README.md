# Acronym Manager

A Django application for managing, searching, and sharing acronyms, with a React frontend for the search interface.

## Project Structure

- `acronym_project/`: Django project settings and configuration
- `acronyms/`: Django app for acronym management
- `users/`: Django app for user authentication and profiles
- `templates/`: Django HTML templates
- `static/`: Static files (CSS, JavaScript, images)
- `frontend/`: React frontend for the search interface

## Setup

### Backend (Django)

1. Create a virtual environment and activate it:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```
   python manage.py migrate
   ```

4. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   ```

### Frontend (React)

1. Make sure you have Node.js and npm installed.

2. Install the frontend dependencies:
   ```
   cd frontend
   npm install
   ```

3. Build the React app:
   ```
   npm run build
   ```
   
   For development with auto-rebuild:
   ```
   npm run dev
   ```

## Running the Application

Start the Django development server:
```
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser to access the application.

## Features

- User authentication (register, login, logout)
- Create, read, update, and delete acronyms
- Search for acronyms by name or definition
- Browse all acronyms
- User profiles
- Export acronyms to various formats

## React Frontend

The home page features a React-based interface with:
- A pill navigation to switch between "Search" and "Browse" modes
- A centralized search bar for finding acronyms
- Integration with the Django backend for search functionality