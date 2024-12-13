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

## Live Demo

Access the blog here: [Blog Website](https://jittery-winonah-heemit-cfa0b49d.koyeb.app/blog/)

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

![image](https://github.com/user-attachments/assets/019f5253-f04e-4855-a287-2ea8e12efab8)

![image](https://github.com/user-attachments/assets/702b9354-8d4f-41e6-9454-630498142595)

![image](https://github.com/user-attachments/assets/6f112d08-5bbc-4464-9738-70a1cdbd4975)

![image](https://github.com/user-attachments/assets/c0c56382-b751-448d-9e1a-6a2fe23631c7)

![image](https://github.com/user-attachments/assets/da900434-03fc-493b-a0fe-6c63ba90e661)

![image](https://github.com/user-attachments/assets/bde5dfd9-c528-4468-a1b6-7c5a4fb9c212)

![image](https://github.com/user-attachments/assets/7f5f09df-bf4c-438d-90b6-09562625d1d1)
