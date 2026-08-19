
## 1. Project objective

This project consists of a simple web application developed with Python Flask
and connected to a PostgreSQL database.

The objective is to create a containerized development environment using Docker
and Docker Compose, allowing the Flask application and PostgreSQL database to
run as separate services.

The project also demonstrates Docker networking, persistent storage,
environment variables, and basic container management.

## 2. Technologies

- Linux (Kali Linux)
- Python 3.13
- Flask
- PostgreSQL 17
- Docker
- Docker Compose
- Git
- GitHub

## 3. Project architecture

The application is composed of two main services:

- Flask: handles the web application and communicates with PostgreSQL.
- PostgreSQL: stores the application data.

Docker Compose creates a network allowing the two containers to communicate.

Architecture:

    Browser
       |
       | HTTP :5000
       v
    Flask container
       |
       | PostgreSQL :5432
       v
    PostgreSQL container
       |
       v
    postgres_data volume

The PostgreSQL data is stored in a Docker named volume so that the data
persists independently of the PostgreSQL container.

## 4. Project structure

    docker-flask-project/
    ├── app.py
    ├── database.py
    ├── requirements.txt
    ├── Dockerfile
    ├── docker-compose.yml
    ├── .dockerignore
    ├── .gitignore
    ├── .env
    └── templates/
        ├── index.html
        └── updates.html

The `.env` file contains configuration values and is excluded from Git
using `.gitignore`.

## 5. Flask application

The web application is implemented with Flask.

It provides a simple task manager allowing users to:

- create tasks
- display tasks
- update tasks
- delete tasks

The Flask application uses `database.py` to communicate with PostgreSQL.

The application listens on port 5000 inside the container.

## 6. Dockerfile

The Dockerfile defines how the Flask application image is built.

    FROM python:3.13

    WORKDIR /app

    COPY . .

    RUN pip install -r requirements.txt

    EXPOSE 5000

    CMD ["python", "app.py"]

The image uses Python 3.13, copies the application into `/app`, installs
the required Python packages, exposes port 5000 and starts the Flask
application.
## 7. PostgreSQL

PostgreSQL 17 is used as the application's database.

The database is executed inside its own Docker container.

Database configuration:

- Database: todo_db
- User: admin
- Port: 5432

The Flask application connects to PostgreSQL using `psycopg2`.

## 8. Docker Compose

Docker Compose is used to define and run the Flask and PostgreSQL services
together.

The main services are:

- `flask-app`
- `postgres-db`

The application can be started with:

    sudo docker compose up -d

The `-d` option starts the services in detached mode.

## 9. Docker network

Docker Compose automatically creates a network for the project.

The Flask container communicates with PostgreSQL through the service name:

    postgres-db

Therefore, inside the Flask container, the database host is:

    POSTGRES_HOST=postgres-db

`localhost` is not used for this connection because Flask and PostgreSQL
run in different containers.

## 10. PostgreSQL volume and persistence

A named Docker volume called `postgres_data` is used to store PostgreSQL
data.

The volume is mounted at:

    /var/lib/postgresql/data

This allows database data to survive when the PostgreSQL container is
stopped or recreated.

The volume can be inspected with:

    sudo docker volume ls

## 11. Environment variables

Database configuration is stored in `.env`:

    POSTGRES_USER=admin
    POSTGRES_PASSWORD=admin123
    POSTGRES_DB=todo_db
    POSTGRES_HOST=postgres-db
    POSTGRES_PORT=5432

The `.env` file is excluded from Git using `.gitignore`.

## 12. How to start the project

From the project directory:

    sudo docker compose up -d

Check the running containers:

    sudo docker ps

The PostgreSQL container should show a healthy status.

The application is available at:

    http://127.0.0.1:5000

## 13. How to stop the project

To stop and remove the Compose containers and network:

    sudo docker compose down

The named PostgreSQL volume remains available unless it is explicitly
removed.

## 14. How to inspect containers

List running containers:

    sudo docker ps

List all containers:

    sudo docker ps -a

View Flask logs:

    sudo docker logs flask-app

View PostgreSQL logs:

    sudo docker logs postgres-db

Execute a command inside the Flask container:

    sudo docker exec -it flask-app bash

Connect to PostgreSQL:

    sudo docker exec -it postgres-db psql -U admin -d todo_db

## 15. How to test the application

Test the Flask application from the host:

    curl http://127.0.0.1:5000

Check the containers:

    sudo docker ps

Check the PostgreSQL health status:

    sudo docker inspect -f '{{.State.Health.Status}}' postgres-db

Check the database tables:

    sudo docker exec -it postgres-db psql -U admin -d todo_db

Inside PostgreSQL:

    \dt

    SELECT * FROM tasks;
