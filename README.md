# LSTM UI REST API

Welcome! 

![Django REST Framework Browsable API](https://raw.githubusercontent.com/japoveda10/lstm_ui_REST_API/master/lstm_ui_REST_API/IMAGE.PNG)

## What is it?

This is a **REST API** for the [LSTM UI Project](https://github.com/japoveda10/lstm_ui_vuejs).

## How was it built?

This **REST API** was built using [Django](https://www.djangoproject.com/) and [Django REST Framework](https://www.django-rest-framework.org/).

## How can I run it?

#### 1. Download the project

Download this GitHub repository. To do so, you can execute the following command in your cmd/terminal window:

   ```
   $ git clone https://github.com/japoveda10/lstm_ui_REST_API.git
   ```

<br />

#### 2. Add the settings.py file to the project
   
Request the `settings.py` file to [japoveda10](https://github.com/japoveda10). When you get it, place it inside the     `lstm_ui_REST_API` folder (where the `urls.py` and `wsgi.py` files are)

<br />

#### 3. Install [Python](https://www.python.org/downloads/)

<br />

#### 4. Create a virtual environment to manage the project's dependencies

If you are using **Windows**, follow the instructions available [here](https://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Windows/). If you are using **macOS**, follow the instructions available [here](https://sourabhbajaj.com/mac-setup/Python/virtualenv.html). 

***Important:***

*The virtual environment setup instructions for Windows and macOS were not written by us (we are linking you to an external information source).*

<br />

#### 5. Install Django

You can use pip to install it (make sure you have created and activated a virtual environment for this project):

   ```
   $ pip install django
   ```

<br />

#### 6. Install project's dependencies

Execute the following commands to install the project's dependencies:

   ```
   $ pip install djangorestframework
   ```
   
   ```
   $ pip install django_extensions
   ```
   
   ```
   $ pip install django-cors-headers
   ```
   
   ```
   $ pip install psycopg2
   ```

<br />

#### 7. Install Postgres

If you are using **Windows**, download **Postgres** from [here](https://www.postgresql.org/) and install it following the Wizard's instructions. The superuser password has to match the **PASSWORD** field value from `settings.py`. Also, make sure that during the Wizard's instructions, you select to install **pgAdmin**. 

Then, edit the **PATH** environmental variable to include:
   
   ```
   C:\Program Files\PostgreSQL\12\bin
   ```
   
   ```
   C:\Program Files\PostgreSQL\12\lib
   ```
 
***Important:***

*Note that there is a 12 in both paths. This is because the installed **pgAdmin** version was 12. Check if your installed **Postgres** version is the same. If it is not, please change the version number in both paths to match your corresponding **Postgres** version number.*
 
More detailed instructions on how to install **Postgres** for Windows can be found [here](https://www.postgresqltutorial.com/install-postgresql/).

Instructions on how to edit the **PATH** environmental variable can be found [here](https://sqlbackupandftp.com/blog/setting-windows-path-for-postgres-tools)

<br />

If you are using **macOS**, execute the following command:

   ```
   $ pip install postgres
   ```

<br />

#### 8. Run Postgres

If you are using **Windows**, in a new Command Propmt execute:
   
   ```
   $ pg_ctl -D "C:\Program Files\PostgreSQL\12\data" start
   ```

***Important:***

*Note that there is a 12 in the path. This is because the installed **pgAdmin** version was 12. Check if your installed **Postgres** version is the same. If it is not, please change the version number in the path to match your corresponding **Postgres** version number.*

<br />

If you are using **macOS**, execute the following command:
   
   ```
   $ pg_ctl -D /usr/local/var/postgres start
   ```

<br />

#### 9. Configure Postgres user and database

If you are using **Windows**, follow these steps:

- 9.1 Open **pgAdmin**
- 9.2 Establish a master password
- 9.3 Click on **Servers** (top left menu) and enter the `settings.py`'s **PASSWORD** field value when you are prompted for a password
- 9.4 Right click on **Databases**, and then select **Create** > **Database**
- 9.5 In the **Database** field, enter **EventLogs** and click on **Save**
- 9.6 Open **EventLogs** in the left menu by clicking the arrow besides **EventLogs**

<br />

If you are using **macOS**, execute the following commands:

   ```
   $ unset PGUSER
   ```
   
   ```
   $ createuser -s postgres
   ```
   
   ```
   $ createdb EventLogs
   ```

<br />

#### 10. Migrate database

Execute the following commands (make sure you are located inside the same folder where the `manage.py` file is):
   
   ```
   $ python manage.py makemigrations
   ```
   
   ```
   $ python manage.py migrate
   ```

<br />

#### 11. Run the project

Execute the following command:

   ```
   $ python manage.py runserver
   ```
   
Then, open your web browser and go to:

   ```
   https://127.0.0.1:8000
   ```

<br />

#### 12. Stop Postgres (after using this project)

If you are using **Windows**, when you finish using this project, you can stop **Postgres** executing the following command:

   ```
   $ pg_ctl -D "C:\Program Files\PostgreSQL\12\data" stop
   ```

***Important:***

*Note that there is a 12 in the path. This is because the installed **pgAdmin** version was 12. Check if your installed **Postgres** version is the same. If it is not, please change the version number in the path to match your corresponding **Postgres** version number.*

<br />

If you are using **macOS**, when you finish using this project, you can stop **Postgres** executing the following command:

   ```
   $ pg_ctl -D /usr/local/var/postgres stop
   ```

<br />

***Important:***

*Everytime you want to run this project, you have to activate the project's virtual environment, run Postgres (see commands in section **8. Run Postgres** above), and finally execute the `python manage.py runserver` command).*

## Questions and Suggestions

If you have questions or suggestions about this project, please contact [japoveda10](https://github.com/japoveda10)

## Author

[japoveda10](https://github.com/japoveda10)
