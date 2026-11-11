from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn
import os 

load_dotenv()

app=FastAPI()

@app.get('/')
def home():
  return {'message':'hello World'}

if __name__=='__main__':
  uvicorn.run(
    app,
    host=os.getenv('HOST'),
    port=int(os.getenv('PORT'))
  )
