# first-demo-adaptive-information-3-microservices
This is the first demo of the project  " Adaptive Information Extraction from Semi-Structured Documents for Intelligent Data Processing "

it contain 3 microservices ,gateway that redirect to parsing that itself redirect to answer generation 

    All microservices are created using FastAPI 
To run it 

    switch t4 gpu of colab 
    run the notebook mistral7b4bitsAPIENDPOINT that will download the model from huggin face optimized inference and memory  and quantized to 4bits with unsloth library
        in the last cell of the notebook : it will expose the  service of model answer generation using http post method using flask library and ngrok server
    copy that public url and replace the answer_gen_APP in the environment variable of last microservice by that url + /post
    tap :docker-compose up the root of repository to run all services
    you can now query the model on the localhost:8000/gateway post method using form-data in postman as data of request body:
        "file":file ( import the image file)
        "instruction":text :  (user question)
        
