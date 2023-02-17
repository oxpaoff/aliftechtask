from datetime import datetime
from sqlalchemy import Column, String, Integer, Float, DateTime, Boolean

from .db import Base


class Client(Base):
    __tablename__ = 'client'
    
    id = Column(Integer, index=True, primary_key=True, unique=True)
    client_id = Column(Integer)
    gender = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    marital_status = Column(String, nullable=True)
    job_position = Column(String, nullable=True)	
    credit_sum = Column(String, nullable=True)
    credit_month = Column(Integer, nullable=True)
    tariff_id = Column(Float, nullable=True)
    score_shk = Column(String, nullable=True)
    education = Column(String, nullable=True)
    living_region = Column(String, nullable=True)
    monthly_income = Column(Float, nullable=True)
    credit_count = Column(Float, nullable=True)
    overdue_credit_count = Column(Float, nullable=True)
    open_account_flg = Column(Boolean)
    created = Column(DateTime, default=datetime.now)