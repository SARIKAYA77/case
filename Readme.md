- To complete the algorithm implementation from end to end as a task of the backend team requested in the project.
- The algorithm.py contains the classification code transmitted from the Machine Learning team as an example.
- A code blog that reads a sample data from the file inside the code
- A code blog that trains data
- Then there is a code blog that makes predictions.

Django Application
====================
- In order for the algorithm to work, two text fields are required in the form of text, label.
  there is a need. To save this information, a django model named Data is created.
- Creating restfull services, allowing the user to add data over the API,
  It is possible to update, delete, list.
- By designing a train endpoint, the train endpoint in the Flask service, which I will specify below, is triggered.
- By designing a prediction endpoint, the prediction request is sent to the prediction endpoint in the Flask service, which I will specify below, and after receiving the result from the service, the user is returned.


Flask Application
===================

- It must have two endpoints. Train and predict

Train - It does not need to take an input as a service.
    - Train codes should be run async via celery in order not to block the user.
    - Since we cannot carry the user's data as a file in the production system, we need to read it from the database. The code block that reads the data in the algorithm from the file should be changed. It is configured to connect to the db used in the Django application, then the data in this table is read and transmitted to the algorithm.
    - The model.pickle and vectorizer.pickle files in the algorithm output are written to a suitable path in Docker.

Predict - The API must be encoded with a text as input.
    - With the help of pickle files created as Train output, the prediction code is run and returned as json from API.

Things to pay attention
============================
- All of the written codes must be run in docker containers. Containers can be run using docker-compose. Below is the expected container list and explanations.

Services:
  - db(postgresql, mysql doesn't matter). In order to prevent data loss, the data path of the db should be defined as volume.
  - web - The container in which the Django application is running. Invokes the flask application with data CRUD operations and train predict endpoints.

  
  - algorithm - Contains train and predict services.
  - algorithm_celery - The container in which the train codes started in the Flask application are running. It is necessary to define the output model and vectorizer files as volume. The same volume algorithm should be given to the container so that it can read the train pickle files and run prediction.
 - redis - acts as a broker between algorithm and algorithm_celery containers
