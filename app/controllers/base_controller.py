"""
HealthSync AI 기본 컨트롤러 클래스
"""
from fastapi import HTTPException, status
from typing import Any
from app.models.base import BaseResponse, ErrorResponse
from app.config.settings import settings
import logging
from datetime import datetime

class BaseController:
    """기본 컨트롤러 클래스"""
    
    def __init__(self):
        self.settings = settings
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def create_success_response(self, data: Any = None, message: str = "성공적으로 처리되었습니다.") -> BaseResponse:
        """성공 응답 생성"""
        return BaseResponse(success=True, message=message, data=data, timestamp=datetime.now())
    
    def handle_service_error(self, error: Exception, operation: str = "unknown"):
        """서비스 에러 처리"""
        self.logger.error(f"Service error in {operation}: {str(error)}", exc_info=True)
        
        if isinstance(error, ValueError):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error))
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="서버 내부 오류가 발생했습니다.")
    
    def log_request(self, endpoint: str, user_id: str = None, **kwargs):
        """요청 로그 기록"""
        log_data = {"endpoint": endpoint, "controller": self.__class__.__name__, "timestamp": datetime.now().isoformat()}
        if user_id:
            log_data["user_id"] = user_id
        log_data.update(kwargs)
        self.logger.info(f"Request to {endpoint}", extra=log_data)
