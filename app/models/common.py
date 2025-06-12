# app/models/common.py
"""
HealthSync AI 공통 모델
"""
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict, Any
from enum import Enum


class EventType(str, Enum):
    """이벤트 타입"""
    USER_REGISTERED = "user_registered"
    HEALTH_DATA_SYNCED = "health_data_synced"
    GOAL_SETUP = "goal_setup"
    MISSION_COMPLETED = "mission_completed"
    AI_ANALYSIS_COMPLETED = "ai_analysis_completed"
    NOTIFICATION_SENT = "notification_sent"


class EventStore(BaseModel):
    """이벤트 저장소"""
    event_id: int = Field(..., description="이벤트 ID")
    aggregate_id: str = Field(..., description="집계 ID")
    event_type: EventType = Field(..., description="이벤트 타입")
    event_data: str = Field(..., description="이벤트 데이터")
    member_serial_number: Optional[int] = Field(default=None, description="회원 일련번호")
    service_name: str = Field(..., description="서비스명")
    created_at: datetime = Field(default_factory=datetime.now, description="생성일시")


class SystemConfig(BaseModel):
    """시스템 설정"""
    config_id: int = Field(..., description="설정 ID")
    config_key: str = Field(..., description="설정 키")
    config_value: str = Field(..., description="설정 값")
    description: Optional[str] = Field(default=None, description="설명")
    created_at: datetime = Field(default_factory=datetime.now, description="생성일시")


class APIResponse(BaseModel):
    """표준 API 응답"""
    success: bool = Field(default=True, description="성공 여부")
    message: str = Field(..., description="응답 메시지")
    data: Optional[Dict[str, Any]] = Field(default=None, description="응답 데이터")
    timestamp: datetime = Field(default_factory=datetime.now, description="응답 시각")

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class PaginatedResponse(BaseModel):
    """페이지네이션 응답"""
    items: list = Field(..., description="아이템 목록")
    total: int = Field(..., description="전체 수")
    page: int = Field(..., description="현재 페이지")
    size: int = Field(..., description="페이지 크기")
    pages: int = Field(..., description="전체 페이지 수")
    has_next: bool = Field(..., description="다음 페이지 존재 여부")
    has_prev: bool = Field(..., description="이전 페이지 존재 여부")