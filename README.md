# cargoroo-assessment
Cargoroo assessment

## install

You need one of the Spatial Database servers supported by GeoDjango, and create a database `cargoroo` with username 
`cargoroo` and password `cargoroo` (or change `cargoroo.settings`).

For PostgreSQL, enable postgis:

```
psql -U postgres -d cargoroo -c "CREATE EXTENSION postgis"
```

cd into project dir:

`cd cargoroo`

Create and activate virtual environment, then install packages:

`pip install -r ../requirements.txt`

## tests

Run tests:

`pytest`

## schemas

Migrate schemas:

`./manage.py migrate`

## import data

Import data:

`./manage.py import_data`

## run server

Start local server:

`./manage.py runserver`

- Swagger UI is available at `http://127.0.0.1:8000/swagger-ui/`
- Open-API documentation is available at `http://127.0.0.1:8000/openapi-schema/`.
- check available endpoints via cli: `./manage.py show_urls`
