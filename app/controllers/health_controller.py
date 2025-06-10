"""
HealthSync AI 헬스체크 컨트롤러
"""
from fastapi import APIRouter, Depends, status
from app.controllers.base_controller import BaseController
from app.services.health_service import health_service
from app.models.health import HealthCheckResponse
from app.core.dependencies import get_settings
from app.config.settings import Settings

class HealthController(BaseController):
    """헬스체크 관련 컨트롤러"""
    
    def __init__(self):
        super().__init__()
        self.router = APIRouter()
        self._setup_routes()
    
    def _setup_routes(self):
        """라우트 설정"""
        
        @self.router.get("/status", response_model=HealthCheckResponse, status_code=status.HTTP_200_OK, summary="🏥 서비스 상태 확인")
        async def get_health_status(app_settings: Settings = Depends(get_settings)):
            """서비스 상태 확인"""
            try:
                self.log_request("health_status")
                return await health_service.get_health_status()
            except Exception as e:
                self.handle_service_error(e, "health_status")

health_controller = HealthController()
