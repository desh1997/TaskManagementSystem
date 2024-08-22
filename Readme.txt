Step by step guide to run the project in local server (Python must be installed, Python 3.9.11)

A. Create virtual environment 
1. py -m venv venv

B. Activate virtualenvironment
1. venv/scripts/activate 

C. Install all the necessaries in the virtualenvironment
1. pip install -r requiremenets.txt 

D. For Database setup use these commands one by one:-
1. Python manage.py makemigrations
2. python manage.py migrate

E. To run the project in localserver
1. python manage.py runserver

F. To deactivate virtualenvironment or to stop it temporary
1. deactivate

G. To stop the django server
1. ctrl + c 