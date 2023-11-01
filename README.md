# django_challenge
Challenge of Python, Django, Postgres and Docker for Klarin LTD

## Requirements

- Docker
- Docker Compose
- Python 3

## Usage Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/Escartin85/django_challenge.git
    ```

2. Navigate to the project directory:

    ```bash
    cd django_challenge
    ```

3. Start the application:

    ```bash
    docker-compose up -d --build
    docker-compose exec backend python klarianTest/manage.py makemigrations
    docker-compose exec backend python klarianTest/manage.py migrate
    ```

4. Access the application in your web browser:

    ```
    http://0.0.0.0:8000
    ```

## Project Structure

Describe the project structure, directories, and their contents.

- klariaTest
- samples_test

## Configuration

Explain if there are any specific configurations that need to be modified.

