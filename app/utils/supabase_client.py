from app.config.settings import settings
from supabase import create_client, Client
import logging

logger = logging.getLogger(__name__)

class SupabaseClient:
    def __init__(self):
        try:
            self.client: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
        except Exception as e:
            logger.error(f"Error initializing Supabase: {str(e)}")
            self.client = None
    
    def save_order(self, order_data: dict) -> dict:
        """Save order to Supabase"""
        if not self.client:
            raise ValueError("Supabase client not configured")
        
        try:
            response = self.client.table('orders').insert(order_data).execute()
            return response.data[0] if response.data else {}
            
        except Exception as e:
            raise RuntimeError(f"Error saving order: {str(e)}")

supabase_client = SupabaseClient()