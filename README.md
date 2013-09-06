This is a new database webserver for storing information on Monarch Butterflies for the Pacific Grove Museum. This project is written with Python and Django.

<ol>
<li>Before running the server make sure that you create your database file and setup an admin account using <code>python manage.py syncdb</code>
<li>To start the server navigate to the python database folder and then run <code>python manage.py runserver 8080</code></li>
<li>The server is now running and you can view it at <code>http://localhost:8080</code> you can also get to the admin page at <code>http://localhost:8080/admin</code></li>
</ol>

Also, we're using <code>Python 2.7.3</code> and <code>Django 1.5</code>
The project is also running on Heroku at <code>http://pgmuseum.herokuapp.com</code>
