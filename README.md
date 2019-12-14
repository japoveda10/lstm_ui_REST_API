# LSTM UI REST API

Welcome! 

![Django REST Framework Browsable API](https://raw.githubusercontent.com/japoveda10/lstm_ui_REST_API/master/lstm_ui_REST_API/IMAGE.PNG)

## What is it?

This is a **REST API** built with [Django REST Framework](https://www.django-rest-framework.org) for the [LSTM UI Project](https://github.com/japoveda10/lstm_ui_vuejs).

## How is it built?

This REST API was built using [Django](https://www.djangoproject.com/) and [Django REST Framework](https://www.django-rest-framework.org/).

## How to install it?

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

7. Execute the following commands (make sure you are located inside the same folder where the manage.py file is):

   ```
   $ manage.py makemigrations
   ```
   
   ```
   $ manage.py migrate
   ```

7. Execute the following command:

   ```
   $ manage.py runserver
   ```

8. Open your web browser and go to:

   ```
   https://127.0.0.1:8000
   ```
   
## Questions and Suggestions

If you have questions or suggestions about this project, please contact [japoveda10](https://github.com/japoveda10)

## Author

[japoveda10](https://github.com/japoveda10)
