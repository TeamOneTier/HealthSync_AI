# app/models/goal.py
"""
HealthSync AI 목표 관리 관련 모델
"""
from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import Optional, List, Dict, Any
from enum import Enum

class MissionStatus(str, Enum):
    """미션 상태"""
    ACTIVE = "active"
    COMPLETED = "completed"
    PAUSED = "paused"
    CANCELLED = "cancelled"

class GoalType(str, Enum):
    """목표 타입"""
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"

class DifficultyLevel(str, Enum):
    """난이도 레벨"""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"

class MissionCategory(str, Enum):
    """미션 카테고리"""
    EXERCISE = "exercise"
    NUTRITION = "nutrition"
    MENTAL_HEALTH = "mental_health"
    HYDRATION = "hydration"
    SLEEP = "sleep"
    STRESS_MANAGEMENT = "stress_management"

class UserMissionGoal(BaseModel):
    """사용자 미션 목표"""
    mission_id: int = Field(..., description="미션 ID")
    member_serial_number: int = Field(..., description="회원 일련번호")
    performance_date: date = Field(..., description="수행 날짜")
    mission_name: str = Field(..., description="미션명")
    mission_description: str = Field(..., description="미션 설명")
    daily_target_count: int = Field(..., description="일일 목표 횟수")
    is_active: bool = Field(default=True, description="활성 상태")
    created_at: datetime = Field(default_factory=datetime.now, description="생성일시")

class MissionCompletionHistory(BaseModel):
    """미션 완료 이력"""
    completion_id: int = Field(..., description="완료 ID")
    mission_id: int = Field(..., description="미션 ID")
    member_serial_number: int = Field(..., description="회원 일련번호")
    completion_date: date = Field(..., description="완료 날짜")
    daily_target_count: int = Field(..., description="일일 목표 횟수")
    daily_completed_count: int = Field(..., description="일일 완료 횟수")
    created_at: datetime = Field(default_factory=datetime.now, description="생성일시")

class MissionSelectionRequest(BaseModel):
    """미션 선택 요청"""
    user_id: str = Field(..., description="사용자 ID")
    selected_mission_ids: List[str] = Field(..., description="선택된 미션 ID 목록")

class GoalSetupResponse(BaseModel):
    """목표 설정 응답"""
    goal_id: str = Field(..., description="목표 ID")
    selected_missions: List[Dict[str, Any]] = Field(..., description="선택된 미션 목록")
    message: str = Field(..., description="응답 메시지")
    setup_completed_at: datetime = Field(..., description="설정 완료 일시")

class ActiveMissionsResponse(BaseModel):
    """활성 미션 응답"""
    daily_missions: List[Dict[str, Any]] = Field(..., description="일일 미션 목록")
    total_missions: int = Field(..., description="전체 미션 수")
    today_completed_count: int = Field(..., description="오늘 완료 수")
    completion_rate: float = Field(..., description="완료율")

class MissionCompleteRequest(BaseModel):
    """미션 완료 요청"""
    user_id: str = Field(..., description="사용자 ID")
    completed: bool = Field(..., description="완료 여부")
    completed_at: datetime = Field(..., description="완료 일시")
    notes: Optional[str] = Field(default=None, description="메모")

class MissionCompleteResponse(BaseModel):
    """미션 완료 응답"""
    message: str = Field(..., description="응답 메시지")
    status: str = Field(..., description="상태")
    achievement_message: str = Field(..., description="성취 메시지")
    new_streak_days: int = Field(..., description="새로운 연속 달성 일수")
    total_completed_count: int = Field(..., description="전체 완료 수")
    earned_points: int = Field(..., description="획득 포인트")

class MissionHistoryResponse(BaseModel):
    """미션 이력 응답"""
    total_achievement_rate: float = Field(..., description="전체 달성률")
    period_achievement_rate: float = Field(..., description="기간 달성률")
    best_streak: int = Field(..., description="최고 연속 달성")
    mission_stats: List[Dict[str, Any]] = Field(..., description="미션별 통계")
    chart_data: Optional[Dict[str, Any]] = Field(default=None, description="차트 데이터")
    period: Dict[str, str] = Field(..., description="조회 기간")
    insights: List[str] = Field(..., description="인사이트")

class MissionResetRequest(BaseModel):
    """미션 재설정 요청"""
    user_id: str = Field(..., description="사용자 ID")
    reason: str = Field(..., description="재설정 사유")
    current_mission_ids: List[str] = Field(..., description="현재 미션 ID 목록")

class MissionResetResponse(BaseModel):
    """미션 재설정 응답"""
    message: str = Field(..., description="응답 메시지")
    new_recommendations: List[Dict[str, Any]] = Field(..., description="새로운 추천 미션")
    reset_completed_at: datetime = Field(..., description="재설정 완료 일시")