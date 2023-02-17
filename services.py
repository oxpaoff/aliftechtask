import pickle
import pandas as pd

from starlette.requests import Request
from sqlalchemy.orm import Session

from ml.transformer import transform_df
from models.models import Client
from models.schemas import ClientPostSchema

with open("ml/model","rb") as file:
    model = pickle.load(file)
    

async def make_prediction(data:dict) -> int:
    data['tariff_id'] = str(data['tariff_id'])
    df = pd.DataFrame([data.values()], columns=data.keys())
    transform_df(df)
    prediction = model.predict(df)
    return int(prediction[0])


async def get_db(request: Request):
    return request.state.db


async def save_client_data(db:Session, client:ClientPostSchema) -> Client:
    client = Client(**client)
    db.add(client)
    db.commit()
    db.refresh(client)
    return client


async def get_client_list(db:Session) -> Client:
    return db.query(Client).all()