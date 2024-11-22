# 🌟 Django Project Setup Guide

## 🎯 Challenge

Your challenge is to set up a new Django project from scratch, ensuring all configurations and packages are properly established. Follow the instructions below to configure your Django project environment.

## 📚 Key Learnings

By completing this setup, you will learn:

- How to create and set up a new Django project.
- The importance of virtual environments and dependency management.
- How to run a Django server and access your application in a browser.

## 👤 User Story

As a beginner Django developer, I want to understand the process of setting up a Django project so that I can build web applications effectively.

## ✅ Acceptance Criteria

- A new Django project is created and properly configured.
- The necessary files and directories are set up:
  - `manage.py`
  - `<project_name>/settings.py`
  - `<project_name>/urls.py`
- The web server runs successfully, and the installation worked page is accessible at `http://127.0.0.1:8000/`.

## 🛠️ Steps to Complete

### 🥳 Set Up a GitHub Repository

1. **📁 Create a new repository** on GitHub for your Django project.
2. **💻 Clone the repository** to your local system and navigate into the folder:
   ```bash
   git clone <repository_url>
   cd <project_folder>
   ```

### 🥳 Set Up a Virtual Environment

Before we install Django, it's highly recommended to set up a virtual environment to keep your coding environment tidy. This will isolate your Python/Django setup on a per-project basis.

1. **📁 Create a new directory**:
   - Open your terminal and run:
     ```bash
     mkdir yourfoldername
     cd yourfoldername
     ```

2. **🛠️ Create a virtual environment**:
   - Run the following command:
     - On **Windows**:
       ```bash
       python -m venv myvenv
       ```
     - On **Linux/OS X**:
       ```bash
       python3 -m venv myvenv
       ```

3. **🔄 Activate the virtual environment**:
   - On **Windows**:
     ```bash
     myvenv\Scripts\activate
     ```
   - On **Linux/OS X**:
     ```bash
     source myvenv/bin/activate
     ```

### 📁 Install Required Packages

1. **🆙 Upgrade pip**:
   ```bash
   python -m pip install --upgrade pip
   ```

2. **📜 Create a `requirements.txt` file** to list dependencies.
   - Open a new file in your code editor and save it as `requirements.txt`.
   - Add `Django` to the file.

3. **📦 Install packages from `requirements.txt`**:
   ```bash
   pip install -r requirements.txt
   ```

### 📁 Create a New Django Project

1. **📁 Create a new Django project**:
   - After activating your virtual environment, run:
     - On **Windows**:
       ```bash
       django-admin startproject <project_name> .
       ```
     - On **Linux/OS X**:
       ```bash
       django-admin startproject <project_name> .
       ```

2. **📂 Understand the directory structure**:
   - Ensure you see a structure like:
   ```
   folder
   ├── manage.py
   ├── <project_name>
   │   ├── asgi.py
   │   ├── __init__.py
   │   ├── settings.py
   │   ├── urls.py
   │   └── wsgi.py
   ├── myvenv
   └── requirements.txt
   ```

3. **⚙️ Change settings**:
   - Open `<project_name>/settings.py` and modify:
     - Set your time zone and language code.
     - Add static files path and update allowed hosts:
       ```python
       STATIC_URL = '/static/'
       STATIC_ROOT = BASE_DIR / 'static'
       ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.pythonanywhere.com']
       ```

### 🗄️ Set Up the Database

1. **Run migrations** to set up the database:
   ```bash
   python manage.py migrate
   ```

### 🌐 Start the Django Development Server

1. **Run the web server**:
   ```bash
   python manage.py runserver
   ```

2. **🌍 Access the website**:
   - Open your browser and go to `http://127.0.0.1:8000/` to see the installation worked page.

## Tips

- Ensure your virtual environment is activated before running any Django commands.
- Keep the directory structure intact, as Django relies on it for routing and configuration.

## Additional Resources

- [Django Official Documentation](https://www.djangoproject.com/)
- [Django Getting Started](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [Django Project Structure](https://realpython.com/get-started-with-django-1/)

## Submission

Once you complete the task, ensure everything is running correctly, and feel free to explore creating content for your project!

Happy coding, framework devs! 😊