To run the django app;

activate the virtual environment;
    source env/Scripts/activate

(make sure you are in your virtual environment before running the following code.)
run the server;
    python manage.py runserver


ensure that pip is already installed 
    python get-pip.py

You may have to download django for runserver to work. 
download django;
    pip install django

Download the rest of the required dependencies;
    pip install -r requirements.txt


after that, try to run the server
    python manage.py runserver

Once it successfully runs, you can access the webpage at http://127.0.0.1:8000/
or the admin page via;
    http://127.0.0.1:8000/admin via your browser