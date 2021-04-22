# Setup

1. Create Virtual Environment : `python -m venv MyEnv`
2. Activate It : `MyEnv\Scripts\activate`
3. Install Requirements : `pip install -r requirements.txt`
4. Migrate : `python manage.py migrate`
5. Make Migrations : `python manage.py makemigrations`
6. Run Server Or Run Tests
    + Run Server : `python manage.py runserver`
    + Run Tests : `python manage.py test budgetApp`
   


7. To Run Functional Tests,
   + Download Web Driver For Your Browser And Put It In The `functional_tests` Folder
   + Run Tests : `python manage.py test functional_tests`