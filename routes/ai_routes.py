from fastapi import APIRouter

from schemas.ai_schemas import (
    ComplaintPrediction,
    CategoryResponse
)

from services.ai_services import predict_category

router = APIRouter(
    prefix="/ai",
    tags=["Artificial Intelligence"]
)


@router.post(
    "/category",
    response_model=CategoryResponse
)
def category_prediction(
    complaint: ComplaintPrediction
):

    prediction = predict_category(
        complaint.complaint
    )

    return {

        "predicted_category": prediction
    }