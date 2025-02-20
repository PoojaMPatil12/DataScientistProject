from fastapi import FastAPI, Request  
import json  
from ollama import chat
from ollama import ChatResponse
from Supervised_learning import supervised_learning_alg


 
app = FastAPI()

@app.get("/")  # Ensure the decorator is correct
async def root():
    return "Application is up and running!"

## using deepseek-r1:1.5b model to get information about Data Science depending on user query.
@app.post("/Information")  # Ensure the decorator is correct
async def info(request: Request):  
    try:
        request_json = await request.json()  
        user_query = request_json.get('query', None)  
        
        if not user_query:
            return {"error": "Query parameter is missing"}  

        result = await ds_info(user_query) 
        return {"message": "Success","query": user_query, "data": result}

    except Exception as e:
        return {"error": str(e)}
    
async def ds_info(user_query):
    print(user_query)
    response = chat(model='deepseek-r1:1.5b', messages=[
    {
        'role': 'user',
        'content': user_query,
    },
    ])
    print(response.message.content)

    return response.message.content

@app.post("/supervised_learning")  
async def supervised_learning(request: Request):
    try:
        request_json = await request.json() 
        user_query = request_json.get('query', None)
        operation = request_json.get('operation', None)
        sub_operation = request_json.get('sub_operation', None)
        Area = request_json.get('Area', 0) 

        result = await supervised_learning_alg(user_query,operation, sub_operation, Area)
        return {"message": "Success","query": user_query, "operation": operation, "sub_operation":sub_operation, "Response": result}   

    except Exception as e:
        return {"error": str(e)}       



    

        
