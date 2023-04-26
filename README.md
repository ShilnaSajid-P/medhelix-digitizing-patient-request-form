
# Medhelix-Digitizing Patient Request Form

It is a python-django project to upload doctors prescriptions along with a prescription ID and date.We can display the Prescription image by using Prescription ID or by using uploaded Date.


Requirements
-------------------


 - Python 3.8
 - Django 4.1.7
 - pip 20.0.2 



Installation
-------------------

- install virtual environment.
```
pip install virtualenv
```
- create virtual environment
```
python -m venv myenv
```

- Activate the virtual environment
```
  source myenv/bin/activate
```
- Install Dependencies
```
  pip install -r requirements.txt

```
- Navigate to project directory
```
  cd medhelix
  
```


- Create database and run migrations:
```
    python manage.py migrate

    python manage.py makemigrations
```
Usage
-------------------


- Start the Django development server
```
  python manage.py runserver
```
- Access the application in your web browser
```
  http://127.0.0.1:8000/
```



    
Login
-------------------


- Login is needed to enter into the project.
- when we Login it redirect to home page.where we have a navbar to select upload prescription option and search option.
- For our first login we need to create a username and password,for this by:
```
  http://127.0.0.1:8000/register
```

Upload
-------------------
- Upload option is to upload a prescription into the database.there is a form where we can upload prescription image along with orescription ID and date.

Search
-------------------


- Search option is to display a prescription by prescription ID or by uploaded date.


License
-------------------

Project Name is Medhelix software released under the Trigeminal.ai.

Contact
-------------------

For any questions or suggestions, please contact Trigeminal ai. mailto: info@trigeminal-ai.com.


