Microservice app

This is a backend   comprising of several components communicating to each other. 

The app  is a simple pipeline of a documents LLM that accept users documents files like images,pdf,doc,text,csv + users question or prompt to aggregate it .I planned to add user authentification and managment later.
Components
    
    All microservices are created using FastAPI 
    Unifiend documents Parser part 
    Auth API  provides authorization functionality. Generates JWT tokens to be used with other APIs.
    Users API is a Spring Boot project written in Java. Provides user profiles. Does not provide full CRUD for simplicity, just getting a single user and all users.
    Log Message Processor is a very short queue processor written in Python. It's sole purpose is to read messages from Redis queue and print them to stdout

Take a look at the components diagram that describes them and their interactions.

Architecture diagram 

![micro](/backend diagram.png)  

How to start

Using docker-compose:

    docker-compose up --build

Then go to  http://127.0.0.1:8080 
Contribution

License

ElyaData