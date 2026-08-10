from pydantic import BaseModel


class ComplaintPrediction(BaseModel):
    complaint: str


class CategoryResponse(BaseModel):
    predicted_category: str