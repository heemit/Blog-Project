# Django Blog Website

This Django-based blog project allows users to create, manage, and display blog posts with features like rich text editing, categories, tags, and search. It includes custom admin interfaces, pagination, and history tracking, providing a scalable foundation for building a blogging platform.

## Features

- **Blog Posts**: Write, edit, and display blog posts with rich text editing.
- **Categories**: Organize blog posts into categories.
- **Slug Generation**: Auto-generate slugs for blog posts and categories.
- **History Tracking**: Track changes to blog posts and categories with Simple History.
- **Search**: Search for blog posts by title.
- **Pagination**: Blog posts are paginated for better navigation.

## Requirements

Before starting, make sure you have the following installed:

- **Python 3.x**: The project is built with Python 3.
- **Django>=4.0,<5.0**: The Django framework for web development.
- **Additional Libraries**: 
  - `django-tinymce==3.4.0`: For rich text editing.
  - `django-simple-history==3.0.0`: To track changes to models.
  - `django-model-utils==4.1.1`: For additional model utilities.
  - `whitenoise==6.5.0`: To serve static files in production.
  - `gunicorn==23.0.0`: A WSGI HTTP server for running the app.

## Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2. **Create a virtual environment**

    If you don't have a virtual environment already, create one:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**

    Install the required dependencies listed in `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations**

    Run the migrations to set up the database schema:

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (for admin access)**

    To access the Django admin panel, create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to create a superuser.

6. **Run the development server**

    Start the development server:

    ```bash
    python manage.py runserver
    ```

    Access the site by going to:

    ```
    http://127.0.0.1:8000/
    ```

    The admin panel is available at:

    ```
    http://127.0.0.1:8000/admin/
    ```

7. **Access the website**

    Go to `http://127.0.0.1:8000/` to view the homepage and browse the blogs.

## Images

![image](https://github.com/user-attachments/assets/17670282-0ec1-4cb0-b66a-0f37a25b6dcb)

![image](https://github.com/user-attachments/assets/f644fd70-8b60-4c86-baba-333808f49c1d)

![image](https://github.com/user-attachments/assets/6aa534b7-9207-46cf-905e-701111655149)

![image](https://github.com/user-attachments/assets/af260525-48f5-4306-a787-b59c8d12e1c6)

![image](https://github.com/user-attachments/assets/afbb3862-56d7-4786-a698-a3b87d39f1a8)

![image](https://github.com/user-attachments/assets/95a57f0b-efbd-4d8c-bd25-237e015556e8)

![image](https://github.com/user-attachments/assets/7ed59928-9ccf-420f-ac0b-6d78b1899fac)

![image](https://github.com/user-attachments/assets/4bab3d7b-49b8-48fa-bfde-39f02fd97da9)

![image](https://github.com/user-attachments/assets/68cd8a11-0f9f-4308-8e4e-a8ade4c41a54)

![image](https://github.com/user-attachments/assets/6e340204-abf8-4be1-9ddb-c11d560794b2)

![image](https://github.com/user-attachments/assets/ae9e6f74-552e-4b50-a2d3-2152ca036317)

![image](https://github.com/user-attachments/assets/b0cf0c6d-723e-4d72-b0ed-5168c795626a)

![image](https://github.com/user-attachments/assets/eb0c4420-eac1-41d0-a905-600b40dbffd8)

![image](https://github.com/user-attachments/assets/183ed3fe-d608-4507-b407-de769fd36ed0)

![image](https://github.com/user-attachments/assets/0ac89c15-bc24-47e3-a319-25c428845c03)

![image](https://github.com/user-attachments/assets/26315c7a-115a-4548-8608-eddb3fc3d03c)

![image](https://github.com/user-attachments/assets/8ec0eba6-82b6-405c-95ad-2491a2aabb3e)

![image](https://github.com/user-attachments/assets/1f100b28-fa85-4b3b-a4d1-341ec5ff1d67)

![image](https://github.com/user-attachments/assets/4480cc97-47a4-4270-8f6e-378278be3193)
