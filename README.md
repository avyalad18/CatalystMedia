
# CATALYST MEDIA - BOOK_INEVENTORY
Before running the project, ensure you have the following installed:

- Python (>=3.6)
- postgresql
- Docker

## APIGateWay (Django)

You can install Python dependencies using the provided `requirements.txt` file:

Before installing `requirements.txt` first create virtual env :

To create virtual environment :

    python -m venv myenv

Activate virtual environment :

    myenv/Scripts/activate

Now install `requirements.txt` :

    pip install -r requirements.txt

Once all requirements get installed, run django server.
Go to the folder containing `manage.py` and run following command :

    python manage.py runserver

it will run django server on `http://localhost/8000`

To API Endpoint postman collection is provided with name `routemobile.postman_collection.json`. Import it in postman test accordingly

If you face any issue make changes `settings.py` .
change DBConnection HOST and port

How to run docker container for `APIGateWay` ?

    cd ApiGateWay\apigateway
    docker-compose up

It will create container and start running that container

## microservice (django)


You can install Python dependencies using the provided `requirements.txt` file:

Before installing `requirements.txt` first create virtual env :

To create virtual environment :

    python -m venv myenv

Activate virtual environment :

    myenv/Scripts/activate

Now install `requirements.txt` :

    pip install -r requirements.txt

If you face any issue make changes `settings.py` .
change DBConnection HOST and port

How to run docker container for `APIGateWay` ?

    cd microservices\BooksService
    docker-compose up

It will create container and start running that container



