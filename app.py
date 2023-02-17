from fastapi import FastAPI, Depends

from sqlalchemy.orm import Session
from models.db import SessionLocal
from models.schemas import ClientSchema

from starlette.requests import Request
from starlette.responses import Response

from services import make_prediction, get_db, save_client_data, get_client_list


app = FastAPI()  


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


@app.post('/')
async def predict(data:ClientSchema, db:Session = Depends(get_db)):
    client = data.dict()
    prediction = await make_prediction(client)
    
    client['open_account_flg'] = prediction
    await save_client_data(db, client)
    
    return {'open_account_flg' : prediction}


@app.get('/')
async def client_list(db:Session = Depends(get_db)):
    return await get_client_list(db)