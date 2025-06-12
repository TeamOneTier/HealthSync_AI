# app/models/user.py
"""
HealthSync AI 사용자 관련 모델
"""
from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import Optional
from enum import Enum

class UserStatus(str, Enum):
    """사용자 상태"""
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"

class OccupationType(BaseModel):
    """직업 유형 모델"""
    occupation_code: str = Field(..., description="직업 코드")
    occupation_name: str = Field(..., description="직업명")
    category: str = Field(..., description="직업 카테고리")

class User(BaseModel):
    """사용자 기본 모델"""
    member_serial_number: int = Field(..., description="회원 일련번호")
    google_id: str = Field(..., description="구글 ID")
    name: str = Field(..., description="사용자 이름")
    birth_date: date = Field(..., description="생년월일")
    occupation: str = Field(..., description="직업")
    created_at: datetime = Field(default_factory=datetime.now, description="생성일시")
    updated_at: datetime = Field(default_factory=datetime.now, description="수정일시")
    last_login_at: Optional[datetime] = Field(default=None, description="마지막 로그인")

class UserRegistrationRequest(BaseModel):
    """사용자 등록 요청"""
    name: str = Field(..., min_length=1, max_length=100, description="사용자 이름")
    birth_date: date = Field(..., description="생년월일")
    occupation: str = Field(..., description="직업")

class UserRegistrationResponse(BaseModel):
    """사용자 등록 응답"""
    user_id: str = Field(..., description="사용자 ID")
    message: str = Field(..., description="등록 결과 메시지")
    status: str = Field(..., description="등록 상태")

class UserProfileResponse(BaseModel):
    """사용자 프로필 응답"""
    user_id: str = Field(..., description="사용자 ID")
    name: str = Field(..., description="사용자 이름")
    age: int = Field(..., description="나이")
    occupation: str = Field(..., description="직업")
    registered_at: datetime = Field(..., description="등록일시")
    last_login_at: Optional[datetime] = Field(default=None, description="마지막 로그인")

class LoginResponse(BaseModel):
    """로그인 응답"""
    access_token: str = Field(..., description="액세스 토큰")
    refresh_token: str = Field(..., description="리프레시 토큰")
    is_new_user: bool = Field(..., description="신규 사용자 여부")
    user_id: str = Field(..., description="사용자 ID")
    expires_in: int = Field(..., description="토큰 만료 시간(초)")