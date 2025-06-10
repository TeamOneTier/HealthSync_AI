"""
HealthSync AI 헬스체크 서비스
"""
import time
from datetime import datetime
from typing import Dict
from app.services.base_service import BaseService
from app.models.health import HealthCheckResponse, EnvironmentInfo
from app.config.settings import settings

class HealthService(BaseService):
    """헬스체크 관련 서비스"""
    
    def __init__(self):
        super().__init__()
        self.service_start_time = time.time()
    
    async def get_health_status(self) -> HealthCheckResponse:
        """서비스 건강 상태 조회"""
        try:
            self.log_operation("health_check")
            
            # 메모리 사용량 조회
            memory_info = self._get_memory_info()
            
            # 환경 정보 조회
            env_info = EnvironmentInfo.get_current_env()
            
            # 가동 시간 계산
            uptime = time.time() - self.service_start_time
            
            return HealthCheckResponse(
                status="healthy",
                service=settings.app_name,
                version=settings.app_version,
                timestamp=datetime.now(),
                environment=env_info,
                uptime=uptime,
                memory_usage=memory_info,
                message="HealthSync AI 서비스가 정상적으로 동작 중입니다! 🚀"
            )
            
        except Exception as e:
            self.logger.error(f"Health check error: {e}")
            return HealthCheckResponse(
                status="degraded",
                service=settings.app_name,
                version=settings.app_version,
                environment=EnvironmentInfo.get_current_env(),
                message="서비스에 일부 문제가 있지만 동작 중입니다."
            )
    
    def _get_memory_info(self) -> Dict[str, float]:
        """메모리 사용량 정보 조회"""
        try:
            import psutil
            process = psutil.Process()
            memory_info = process.memory_info()
            
            return {
                "rss_mb": round(memory_info.rss / 1024 / 1024, 2),
                "vms_mb": round(memory_info.vms / 1024 / 1024, 2),
                "percent": round(process.memory_percent(), 2)
            }
        except ImportError:
            return {"message": "psutil not installed"}
        except Exception as e:
            self.logger.warning(f"Failed to get memory info: {e}")
            return {"error": "Unable to get memory info"}

health_service = HealthService()
