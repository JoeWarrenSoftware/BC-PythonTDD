# 🚀 Deploy Your Django Application

## 🎯 Challenge

In this task, you will deploy your Django application to PythonAnywhere using GitHub to manage your code. You’ll set up Git for version control, push your project to GitHub, and link it to PythonAnywhere for deployment. By the end, your website will be live on the internet!

## 📚 Key Learnings

By completing this exercise, you will learn:

- How to set up a Git repository for your Django project.
- How to push your code to GitHub.
- How to deploy your Django application to PythonAnywhere.

## 👤 User Story

As a Django developer, I want to deploy my application to a live server so that users can access and interact with it online.

## ✅ Acceptance Criteria

- The Django application is successfully pushed to GitHub.
- The project is deployed and accessible via a web URL on PythonAnywhere.
- Production-ready settings are applied for security and performance.

## 🛠️ Steps to Complete

### 1️⃣ Set Up Git for Your Project

1. **Initialize a Git Repository**:
   - Open your console, navigate to the `gitfolder` directory, and run:
     ```bash
     git init
     git config --global user.name "Your Name"
     git config --global user.email you@example.com
     ```

2. **Create a `.gitignore` File**:
   - In your project’s root directory, create a `.gitignore` file with the following contents to exclude certain files:
     ```gitignore
     # Python
     *.pyc
     *~
     __pycache__

     # Env
     .env
     myvenv/
     venv/

     # Database
     db.sqlite3

     # Static folder at project root
     /static/

     # macOS
     ._*
     .DS_Store
     .fseventsd
     .Spotlight-V100

     # Windows
     Thumbs.db*
     ehthumbs*.db
     [Dd]esktop.ini
     $RECYCLE.BIN/

     # Visual Studio
     .vscode/
     .history/
     *.code-workspace
     ```

3. **Check the Status and Add Files**:
   - Run `git status` to see the untracked files, then add and commit your changes:
     ```bash
     git add .
     git commit -m "My Django app, first commit"
     ```

### 2️⃣ Push Your Code to GitHub

1. **Create a GitHub Repository**:
   - Go to [GitHub.com](https://github.com/), sign up or log in, and create a new repository named `my-first-blog`.
   - Leave "Initialize with a README" unchecked, and leave the .gitignore and License options blank.

2. **Link Your Local Repository to GitHub**:
   - In your console, connect your local Git repository to the remote GitHub repository:
     ```bash
     git remote add origin https://github.com/<your-github-username>/my-first-blog.git
     git push -u origin HEAD
     ```

   - Enter your GitHub username and password if prompted.

### 3️⃣ Setting Up on PythonAnywhere

1. **Sign Up for a PythonAnywhere Account**:
   - Sign up for a free "Beginner" account at [PythonAnywhere](https://www.pythonanywhere.com/).

2. **Create a PythonAnywhere API Token**:
   - Go to your PythonAnywhere dashboard, click on the **Account** page, and create an API token. This is a one-time setup step.

3. **Configure Your Site on PythonAnywhere**:
   - From the PythonAnywhere Dashboard, open a **Bash console**. PythonAnywhere provides a helper tool for deploying Django applications, so let’s install it:
     ```bash
     pip3.10 install --user pythonanywhere
     ```

4. **Run the Helper Script**:
   - Use the helper script to automatically set up your app from GitHub (replace `<your-github-username>` with your actual GitHub username):
     ```bash
     pa_autoconfigure_django.py --python=3.10 https://github.com/<your-github-username>/my-first-blog.git
     ```

   - This script will:
     - Download your code from GitHub.
     - Create a virtual environment on PythonAnywhere.
     - Update your settings for deployment.
     - Set up the database using `manage.py migrate`.
     - Configure static files and link your app to PythonAnywhere’s API.

5. **Create a Superuser for the Admin**:
   - Run the following command in the PythonAnywhere console to set up an admin user for your deployed site:
     ```bash
     python manage.py createsuperuser
     ```

6. **Check Your Files on PythonAnywhere** (optional):
   - You can use the `ls` command to view your project files or explore them via the "Files" page on PythonAnywhere.

### 🌐 Access Your Live Site

- Go to the "Web" page on PythonAnywhere to get the link to your deployed site. Your application should now be live and accessible on the internet!

## 📚 Additional Resources
- [Walkthrough Video](https://youtu.be/33VC3COHtU0)
- [GitHub Guide](https://docs.github.com/en/get-started/quickstart)
- [PythonAnywhere Deployment Guide](https://www.pythonanywhere.com/)

Happy deploying! 🎉