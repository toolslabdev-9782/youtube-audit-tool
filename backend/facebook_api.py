from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class FacebookAuditRequest(BaseModel):
    page_input: str

@router.post("/audit/facebook")
def audit_facebook(request: FacebookAuditRequest):
    return {
        "status": "success",
        "page": request.page_input,
        "message": "Facebook audit endpoint is working"
    }
