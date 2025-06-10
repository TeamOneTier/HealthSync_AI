"""
HealthSync AI 기본 데이터 모델
"""
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Generic, TypeVar, List
from enum import Enum

# Generic 타입 정의
T = TypeVar('T')

class BaseResponse(BaseModel, Generic[T]):
    """기본 응답 모델"""
    success: bool = Field(default=True, description="요청 성공 여부")
    message: str = Field(default="", description="응답 메시지")
    data: Optional[T] = Field(default=None, description="응답 데이터")
    timestamp: datetime = Field(default_factory=datetime.now, description="응답 시간")
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

class ErrorResponse(BaseModel):
    """에러 응답 모델"""
    success: bool = Field(default=False, description="요청 성공 여부")
    error_code: str = Field(..., description="에러 코드")
    message: str = Field(..., description="에러 메시지")
    details: Optional[dict] = Field(default=None, description="에러 상세 정보")
    timestamp: datetime = Field(default_factory=datetime.now, description="에러 발생 시간")

class HealthStatus(str, Enum):
    """건강 상태 열거형"""
    HEALTHY = "healthy"
    WARNING = "warning"
    CRITICAL = "critical"
    UNKNOWN = "unknown"
