# 🌟 Create a New Django Application

## 🎯 Challenge

In this task, you will create a separate application inside your Django project. This will help keep everything organized from the very beginning. You will also set up a model and integrate it into the Django admin.

## 📚 Key Learnings

By completing this exercise, you will learn:

- How to create a new application within a Django project.
- The structure of a Django app and the files it contains.
- How to register models with the Django admin interface.
- How to create a superuser for admin access.

## 👤 User Story

As a Django developer, I want to keep my project organized by separating functionalities into different applications so that my codebase is manageable and maintainable.

## ✅ Acceptance Criteria

- A new Django application is created and integrated into the project.
- The model for the application is defined and migrated to the database.
- The model is registered in the Django admin interface.
- A superuser is created for accessing the Django admin dashboard.

## 🛠️ Steps to Complete

### 📁 Create a New Django Application

1. **🔄 Navigate to your project directory** (where `manage.py` is located):
   - On **Windows**:
     ```bash
     (myvenv) C:\Users\Name\project>
     ```
   - On **Mac OS X and Linux**:
     ```bash
     (myvenv) ~/$
     ```

2. **📦 Create the application**:
   - Run the following command:
     - On **Windows**:
       ```bash
       python manage.py startapp app-name
       ```
     - On **Mac OS X and Linux**:
       ```bash
       python manage.py startapp app-name
       ```

3. **📂 Check the directory structure**:
   - After running the command, you should see a new directory structure like this:

   ```
   folder
   ├── app-name
   │   ├── admin.py
   │   ├── apps.py
   │   ├── __init__.py
   │   ├── migrations
   │   │   └── __init__.py
   │   ├── models.py
   │   ├── tests.py
   │   └── views.py
   ├── db.sqlite3
   ├── manage.py
   ├── XXXX
   │   ├── asgi.py
   │   ├── __init__.py
   │   ├── settings.py
   │   ├── urls.py
   │   └── wsgi.py
   ├── myvenv
   │   └── ...
   └── requirements.txt
   ```

### ⚙️ Update Settings

1. **🔍 Open `mysite/settings.py`** in your code editor.
2. **📜 Add your app to `INSTALLED_APPS`**:
   - Find the `INSTALLED_APPS` list and add a new entry for your app:
     ```python
     INSTALLED_APPS = [
         ...
         'app-name',
     ]
     ```

### 🗄️ Create a Django Model

1. **📂 Open `app-name/models.py`, check model_setup_readme.md for example or more info**:
   - Define your model by adding class definitions for your app's objects.

2. **🔄 Make migrations**:
   - After saving your changes, run the following command to create migration files:
     ```bash
     python manage.py makemigrations app-name
     ```

3. **📦 Apply migrations**:
   - Run the following command to apply the migration to the database:
     ```bash
     python manage.py migrate app-name
     ```

### 🏢 Register the Model with Django Admin

1. **🔍 Open `app-name/admin.py`**:
   - Replace its contents with the following code:
     ```python
     from django.contrib import admin
     from .models import model-name  # Replace with your model name

     admin.site.register(model-name)
     ```

### 🌐 Create a Superuser

1. **🔄 Open a new terminal** (while keeping the server running) and create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
   - Follow the prompts to set your username, email, and password.

### 🌍 Access the Django Admin

1. **🔗 Go to your browser** and navigate to:
   ```
   http://127.0.0.1:8000/admin/
   ```
2. **🔑 Log in** with the superuser credentials you created.

3. **📝 Experiment with your model**:
   - Add five or six model values in the Django admin interface.

## 📚 Additional Resources

- [Django Admin Documentation](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/)

## Submission

Once you have completed the task and tested your model in the Django admin, feel free to explore further features of Django!

Happy coding! 😊