HOW TO CLONE THE PROJECT AND TEST IT :

1. Download the repository and put it somewhere on your computer

2. Create a virtual environment (venv) within the repository's directory :
        - python -m venv [name of your venv]

3. Activate your virtual environment :
        - [name of your venv]\Scripts\activate

4. Install the dependencies :
        - pip install -r requirements.txt
    
5. Insert data into the database by using an admin command :
        - python manage.py peuplerdatabase.py

6. Start the webserver :
        - python manage.py runserver

7. Check out the website for yourself by going to this IP in your browser :
        - http://127.0.0.1:8000/
