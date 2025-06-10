"""
HealthSync AI 기본 서비스 클래스
"""
from abc import ABC
from app.config.settings import settings
import logging
import time
from datetime import datetime

class BaseService(ABC):
    """기본 서비스 추상 클래스"""
    
    def __init__(self):
        self.settings = settings
        self.logger = logging.getLogger(self.__class__.__name__)
        self._start_time = time.time()
    
    def get_uptime(self) -> float:
        """서비스 가동 시간 반환 (초)"""
        return time.time() - self._start_time
    
    def log_operation(self, operation: str, user_id: str = None, **kwargs):
        """작업 로그 기록"""
        log_data = {
            "operation": operation,
            "timestamp": datetime.now().isoformat(),
            "service": self.__class__.__name__
        }
        if user_id:
            log_data["user_id"] = user_id
        log_data.update(kwargs)
        
        self.logger.info(f"Operation: {operation}", extra=log_data)
