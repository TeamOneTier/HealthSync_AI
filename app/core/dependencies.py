"""
HealthSync AI 공통 의존성 관리
"""
from fastapi import Depends, HTTPException, status, Query
from app.config.settings import settings, Settings
import logging

logger = logging.getLogger(__name__)

def get_settings() -> Settings:
    """설정 의존성 주입"""
    return settings

def get_current_user_id(user_id: str = Query(..., description="사용자 ID")) -> str:
    """현재 사용자 ID 추출"""
    if not user_id or len(user_id.strip()) == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="사용자 ID가 필요합니다.")
    return user_id.strip()
