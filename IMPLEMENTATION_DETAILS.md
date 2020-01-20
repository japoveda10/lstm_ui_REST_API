# LSTM UI REST API Project Implementation Details

**LSTM UI REST API** is a **Django** project. It has the next file structure:

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

Django projects have **apps**. This project has one app: **api**.
