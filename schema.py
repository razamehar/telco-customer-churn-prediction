from pydantic import BaseModel, Field, PositiveInt, confloat
from typing import Literal

class ChurnValues(BaseModel):
    gender: Literal["Female", "Male"]
    tenure: PositiveInt = Field(..., description="Months with the company")
    MonthlyCharges: confloat(gt=0)
    TotalCharges: confloat(ge=0)


    class Config:
        schema_extra = {
            "example": {
                "gender": "Female",
                "tenure": 12,
                "MonthlyCharges": 70.5,
                "TotalCharges": 840.0
            }
        }
