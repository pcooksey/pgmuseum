This is a new database webserver for storing information on Monarch Butterflies for the Pacific Grove Museum. This project is written with Python and Django. <a href="http://south.aeracode.org/">South</a> is used for migration of databases.

Process flow for project:
<ol>
<li>Make changes to Master branch and commit them</li>
<li>For deployment, change to deploy branch and pull changes from master <code> git merge master </code></li>
<li>Update heroku: <code> git push heroku deploy:master </code></li>
<li>For changes to the model in master branch: </li>
<li> 
	```Batchfile
		python manage.py schemamigration some_app --auto
		git add .
		git commit -m "Adding new migrations"
		git checkout deploy
		git merge master
		git push heroku deploy:master
		heroku run python manage.py migrate appname
	```
</li>
</ol>

For running website locally on computer:
<ol>
<li>Before running the server make sure to create your database file and setup an admin account using <code>python manage.py syncdb</code>
<li>Start the server by navigate to the python database folder and running <code>python manage.py runserver 8080</code></li>
<li>The server is now running and can be viewed at <code>http://localhost:8080</code>. The admin page can be accessed at <code>http://localhost:8080/admin</code></li>
<li>For running the server on Heroku. Use the command <code>python my_django_app/manage.py collectstatic --noinput; gunicorn database.wsgi</code></li>
</ol>

Extra commands for Heroku:
<ol>
<li> Resetting database <code> heroku pg:reset DATABASE </code>; however, it will destroy everything. </li>
<li> Backing up database <code> heroku pgbackups:capture </code>;</li>
<li> For local migrate file use this command then migrate it again. <code>python django_project/manage.py schemamigration some_app --auto </code> </li>
<li> <code>heroku run python manage.py migrate app_name </code> </li>
</ol>

Also, we're using <code>Python 2.7.3</code> and <code>Django 1.5</code>
The project is also running on Heroku at <code>http://pgmuseum.herokuapp.com</code>
