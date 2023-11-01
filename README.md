# django_challenge
Challenge of Python, Django, Postgres and Docker for Klarian LTD

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

4. Access the application in your web browser to upload files:

    ```
    http://0.0.0.0:8000/upload/
    ```

5. Access the application to do the questy test:

    ```
    http://0.0.0.0:8000/query/?type=TypeJSON
    http://0.0.0.0:8000/query/?type=TypeCSV
    ```

## Project Structure

Describe the project structure, directories, and their contents.

- app
  Folder where is allocated all the app to run it.
  
- samples_test
  Folder where are allocated files as sample .csv and .json to test the app


