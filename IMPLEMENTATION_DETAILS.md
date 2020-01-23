# LSTM UI REST API Project Implementation Details

## About

**LSTM UI REST API** is a **Django** project. The **API** was built using **Django REST Framework**.

## File Structure

```
├── api
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations                          # Directory containing migrations history (updates to models)
    ├── models.py                           # Defines Django models
    ├── serializers.py                      # Defines Serializers (convert database data to Django models and vice versa)
    ├── tests.py
    └── views.py                            # Defines endpoints
├── EXAMPLE HTTP REQUESTS
    ├── POST_EVENT_LOG.txt                  # Example HTTP POST /event_logs/ request body
    └── POST_RUNNING_CASE.txt               # Example HTTP POST /running_cases/ request body
├── input_files
    ├── ConsultaDataMining201618.csv
    ├── Production.csv
    ├── PurchasingExample.csv
    ├── ConsultaDataMining201618.xes.gz
    ├── Production.xes.gz
    └── PurchasingExample.xes.gz
├── lstm_ui_REST_API
    ├── __init__.py
    ├── settings.py                         # Defines database connection among other important information about the project
    ├── urls.py                             # Defines the project's routes
    └── wsgi.py
├── support_modules
    ├── nn_support.py
    ├── readers
        └── log_reader.py
    ├── role_discovery.py
    └── support.py
├── IMAGE.png
├── event_log_services.py
└── manage.py
```

## Django projects key concepts

Django projects have **apps**. This project has one app: **api**.

## Django REST Framework key concepts

**Django REST Framework** offers many ways to create an API, like:

* `HyperlinkedModelSerializer`s with `ModelViewSet`s (automatically generates the endpoints, but specific HTTP requests are not detectable in the code)
* `ModelSerializer`s with **function-based views** (using `@api_view` decorator in `views.py`)
* `ModelSerializer`s with **class-based views** (using the `APIView` class in `views.py`)
* `HyperlinkedModelSerializer`s with **generic class-based views** (using `generics.ListCreateAPIView` and `generics.RetrieveUpdateDestroyAPIView`)
* `ViewSet`s
* `Serializer`s and **class-based views** (using the `APIView` class in `views.py`)

For more details, go to the [Django REST Framework website](https://www.django-rest-framework.org)

## How was the API built?

This project uses `Serializer`s and **class-based views** (using the `APIView` class in `views.py`)

For the API to work, four main files work together:

* `models.py` define **Django models**
* `serializers.py` define **serializers** (convert database data to Django models and vice versa)
* `views.py` defines the **endpoints**
* `urls.py` defines the project's **routes**
