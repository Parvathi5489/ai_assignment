# Shopify Store Insights Fetcher

A FastAPI application to fetch and add daily Shopify store insights.

## Features

- `GET /insights`: Returns latest or specific date insights.
- `POST /insights`: Adds a new insight entry.

## Requirements

- FastAPI
- Uvicorn
- Python 3.7+

## Run

```bash
uvicorn main:app --reload
```

Use tools like Swagger UI at `http://127.0.0.1:8000/docs` to test.
