"""
HealthSync AI 헬스체크 관련 모델
"""
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Dict, Optional
import platform
import sys

class EnvironmentInfo(BaseModel):
    """환경 정보 모델"""
    python_version: str = Field(..., description="Python 버전")
    platform: str = Field(..., description="운영체제")
    architecture: str = Field(..., description="시스템 아키텍처")

    @classmethod
    def get_current_env(cls) -> "EnvironmentInfo":
        """현재 환경 정보 반환"""
        return cls(
            python_version=f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
            platform=platform.system(),
            architecture=platform.machine()
        )

class HealthCheckResponse(BaseModel):
    """헬스체크 응답 모델"""
    status: str = Field(..., description="서비스 상태")
    service: str = Field(..., description="서비스 이름")
    version: str = Field(..., description="서비스 버전")
    timestamp: datetime = Field(default_factory=datetime.now, description="응답 시간")
    environment: EnvironmentInfo = Field(..., description="환경 정보")
    uptime: Optional[float] = Field(default=None, description="서비스 실행 시간(초)")
    memory_usage: Optional[Dict[str, float]] = Field(default=None, description="메모리 사용량")
    message: str = Field(default="서비스가 정상적으로 동작 중입니다! 🚀", description="상태 메시지")
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
