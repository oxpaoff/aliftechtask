from pydantic import BaseModel
from pydantic.schema import Optional


class ClientSchema(BaseModel):
    client_id : int
    gender : str
    age : int
    marital_status : str	
    job_position : str		
    credit_sum : str
    credit_month : int
    tariff_id : float
    score_shk : str	
    education : str		
    living_region : str	
    monthly_income : float	
    credit_count : Optional[float]
    overdue_credit_count : Optional[float]
    
    class Config:
        orm_mode = True
        
		
class ClientPostSchema(ClientSchema):
	open_account_flg : bool
     