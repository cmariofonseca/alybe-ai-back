from app.utils.supabase_client import supabase_client
import logging

logger = logging.getLogger(__name__)

class SupabaseService:
    @staticmethod
    async def save_user_message(message: str) -> dict:
        try:
            response = supabase_client.client.table('user_messages').insert({
                "user_message": message
            }).execute()
            
            return response.data[0] if response.data else {}
            
        except Exception as e:
            logger.error(f"Error saving message: {str(e)}")
            return {}
