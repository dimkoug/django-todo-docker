# Django Todo Docker

This repository contains a minimal example of running a Django **todo** application inside Docker containers. The stack includes PostgreSQL, Redis and Celery along with an Nginx reverse proxy. It is intended for local development or experimentation.

## Getting Started

1. **Clone the repository** and change into the project directory.
2. **Create a `.env` file** by copying the provided sample:

   ```bash
   cp .env_sample .env
   ```
   Adjust any values if necessary (database credentials, email settings, etc.).

3. **Build and start the containers** using Docker Compose:

   ```bash
   docker-compose up --build
   ```

   This command launches the following services:
   - `web`: the Django application running with the built image.
   - `db`: a PostgreSQL instance used by Django.
   - `redis`: a Redis instance for Celery tasks.
   - `celery_worker` and `celery_beat`: background task processing.
   - `nginx`: serves static files and proxies requests to Django.

4. **Access the application.** Once the containers are running, visit <http://localhost:8080/> in your browser.

## Useful Commands

- **Run migrations** inside the `web` container:

  ```bash
  docker-compose exec web python manage.py migrate
  ```

- **Create a superuser** to access the Django admin:

  ```bash
  docker-compose exec web python manage.py createsuperuser
  ```

- **Stop the containers** when done:

  ```bash
  docker-compose down
  ```

## Project Structure

```
├── Dockerfile           # Build instructions for the Django app image
├── docker-compose.yml   # Multi-container setup
├── config               # Configuration files (Nginx)
├── src                  # Django project source code
└── .env_sample          # Example environment variables
```

The `src` directory contains the Django project (`todoproject`) and the `todo` app with simple models, views and Celery tasks.

---

This README aims to provide enough information to get the containers running quickly. Feel free to modify the setup to suit your own development workflow.
