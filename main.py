from fastapi import FastAPI, Request  
import json  
from ollama import chat
from ollama import ChatResponse

 
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
        
