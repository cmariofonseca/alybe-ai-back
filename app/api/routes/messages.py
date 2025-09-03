from app.core.models import UserMessageRequest
from app.services.supabase_service import SupabaseService
from fastapi import APIRouter

router = APIRouter(prefix="/messages", tags=["messages"])

@router.post("/save")
async def save_user_message(request: UserMessageRequest):
    result = await SupabaseService.save_user_message(request.message)
    return {"status": "success", "message_id": result.get('id')}