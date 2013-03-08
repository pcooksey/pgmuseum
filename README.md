This is our database in a box project for CST-438.  This project is written with Python and Django.

Before running the server go into <code>settings.py</code> and make sure that under <code>DATABASES</code> the name field is set to the absolute path of your <code>sqlite3.db</code> file.

To start the server naviage to the python database folder and then run <code>python manage.py runserver 8080</code>

This will start the server at python <code>http://localhost:8080</code>

Also, we're using <code>Python 2.7.3</code> and <code>Django 1.5</code>
