Setup
-------------------

- Install Python 3.8.10
-------------------


- To install Python 3.8.10 on your system, follow the steps below:
- Step 1: Check System Requirements
   Before installing Python 3.8.10, make sure your system meets the minimum system requirements for the installation. You can check the official Python website for the system requirements.
- Step 2: Download Python 3.8.10
Go to the official Python website at https://www.python.org/downloads/release/python-3810/ to download the Python 3.8.10 installer for your operating system. Choose the appropriate installer based on your operating system (e.g., Windows, macOS, or Linux).
- Step 3: Run Installer
Once the download is complete, locate the installer file and run it as an administrator (on Windows) or with root privileges (on Linux/macOS) to start the installation process.

- Step 4: Customize Installation (Optional)
During the installation process, you may be given the option to customize the installation. You can choose to customize the installation path, enable/disable certain features, or select additional components. You can also choose to add Python to your system's PATH environment variable, which allows you to run Python from any directory in the command prompt or terminal.
- Step 5: Install Python
Click on the "Install Now" or "Install" button to begin the installation process. The installer will copy Python files to your system and configure Python based on your chosen options.
- Step 6: Verify Installation
Once the installation is complete, open a command prompt (on Windows) or a terminal (on Linux/macOS) and type "python3" (or "python" on Windows) to start the Python interpreter. You should see the Python version as 3.8.10 and be able to run Python commands in the interpreter without any errors.
-------------------

- install pip

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

```
-------------------
- install django

```
pip install django
```
-------------------


- Clone the project from the github
```
  git clone https://github.com/mohan-mj/medhelix-digitizing-patient-request-form.git

```



- Install Dependencies
```
  pip install -r requirements.txt

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
