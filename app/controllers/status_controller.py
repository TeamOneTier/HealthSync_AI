"""
HealthSync AI 헬스체크 컨트롤러
"""
from fastapi import APIRouter, Depends, status
from app.controllers.base_controller import BaseController
from app.models.base import BaseResponse
from app.core.dependencies import get_settings
from app.config.settings import Settings
import time, psutil
from datetime import datetime

class StatusController(BaseController):
    """상태체크 관련 컨트롤러"""
    
    def __init__(self):
        super().__init__()
        self.router = APIRouter()
        self._setup_routes()
    
    def _setup_routes(self):
        """라우트 설정"""

        @self.router.get("/check", response_model=BaseResponse,
                         status_code=status.HTTP_200_OK,
                         summary="🔧 시스템 상태 확인")
        async def get_system_status(app_settings: Settings = Depends(get_settings)):
            """시스템 상태 확인"""
            try:
                self.log_request("system_status")
                try:
                    memory_mb = round(psutil.Process().memory_info().rss / 1024 / 1024, 2)
                except:
                    memory_mb = 0.0

                status_data = {
                    "status": "running",
                    "service": app_settings.app_name,
                    "version": app_settings.app_version,
                    "memory_mb": memory_mb,
                    "environment": "development" if app_settings.debug else "production"
                }

                return self.create_success_response(
                    data=status_data,
                    message="서비스가 정상 동작 중입니다! 🚀"
                )

            except Exception as e:
                self.handle_service_error(e, "system_status")

status_controller = StatusController()
