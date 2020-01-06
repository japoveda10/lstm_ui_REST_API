# LSTM UI REST API

Welcome! 

![Django REST Framework Browsable API](https://raw.githubusercontent.com/japoveda10/lstm_ui_REST_API/master/lstm_ui_REST_API/IMAGE.PNG)

## What is it?

This is a **REST API** for the [LSTM UI Project](https://github.com/japoveda10/lstm_ui_vuejs).

## How was it built?

This REST API was built using [Django](https://www.djangoproject.com/) and [Django REST Framework](https://www.django-rest-framework.org/).

## How can I run it?

1. Download this GitHub repository

   `$ git clone https://github.com/japoveda10/lstm_ui_REST_API.git`

2. Request the `settings.py` file to [japoveda10](https://github.com/japoveda10). When you get it, place it inside the `lstm_ui_REST_API` folder (where the `urls.py` and `wsgi.py` files are)

3. Install [Python](https://www.python.org/downloads/)

4. Create a **virtual environment** to manage the project's dependencies. If you are using **Windows**, follow the instructions available [here](https://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Windows/). If you are using **macOS**, follow the instructions available [here](https://sourabhbajaj.com/mac-setup/Python/virtualenv.html). 

   **Important:** the virtual environment setup instructions for Windows and macOS were not written by us (we are linking you       to an external information source).

5. Install **Django** using pip (make sure you have created and activated a virtual environment for this project):

   ```
   $ pip install django
   ```

6. Execute the following commands to install the project's dependencies:

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
   $ pip install postgres
   ```
   
   ```
   $ pip install psycopg2
   ```

7. Run Postgres
   
   If you are using **macOS**, execute the following command:
   
   ```
   $ pg_ctl -D /usr/local/var/postgres start
   ```
   
   If you are using **Windows**, download Postgres from [here](https://www.postgresql.org/) and install it following the Wizard´s instructions. The superuser password has to match the PASSWORD field from `settings.py`. Then, edit the PATH environmental variable to include:
   
   `C:\Program Files\PostgreSQL\12\bin`
   
   `C:\Program Files\PostgreSQL\12\lib`
   
Finally, in a new Command Propmt, execute:
   
   ```
   $ pg_ctl -D "C:\Program Files\PostgreSQL\12\data" start
   ```
   
8. Execute the following commands to configure the database (for **Windows** and **macOS**):

   ```
   $ unset PGUSER
   ```
   
   ```
   $ createuser -s postgres
   ```
   
   ```
   $ createdb EventLogs
   ```

9. Execute the following commands (make sure you are located inside the same folder where the `manage.py` file is):
   
   ```
   $ manage.py migrate
   ```

10. Execute the following command:

   ```
   $ manage.py runserver
   ```

11. Open your web browser and go to:

   ```
   https://127.0.0.1:8000
   ```

If you are using **macOS**, when you finish using the app, you can stop Postgres executing the following command:

   ```
   $ pg_ctl -D /usr/local/var/postgres stop
   ```
   
If you are using **Windows**, when you finish using the app, you can stop Postgres executing the following command:

   ```
   $ pg_ctl -D "C:\Program Files\PostgreSQL\12\data" stop
   ```
   
## Questions and Suggestions

If you have questions or suggestions about this project, please contact [japoveda10](https://github.com/japoveda10)

## Author

[japoveda10](https://github.com/japoveda10)
