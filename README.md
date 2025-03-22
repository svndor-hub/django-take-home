# Product Catalog Django Project

This is a simple Django project that demonstrates product catalog functionality with search and filtering capabilities.

## Features

- Django models for Products, Categories, and Tags with appropriate relationships
- Admin interface for easy data management
- Search products by description
- Filter products by category
- Filter products by tags
- Combine multiple search and filter options

## Setup Instructions

1. Clone the repository
2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install django
   ```
4. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```
   python manage.py runserver
   ```
7. Visit http://127.0.0.1:8000/ to use the search and filter functionality

## Usage

1. Visit the main page at http://127.0.0.1:8000/
2. Use the search box to find products by description
3. Use the category dropdown to filter products by category
4. Use the tag checkboxes to filter products by tag
5. Combine search and filters as needed
