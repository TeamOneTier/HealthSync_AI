# app/models/intelligence.py
"""
HealthSync AI 지능형 서비스 관련 모델
"""
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List, Dict, Any
from enum import Enum

class MessageRole(str, Enum):
    """메시지 역할"""
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"

class MessageType(str, Enum):
    """메시지 타입"""
    QUESTION = "question"
    ANSWER = "answer"
    NOTIFICATION = "notification"
    CELEBRATION = "celebration"
    ENCOURAGEMENT = "encouragement"

class SenderType(str, Enum):
    """발신자 타입"""
    USER = "user"
    AI = "ai"
    SYSTEM = "system"

class NotificationType(str, Enum):
    """알림 타입"""
    DAILY_ENCOURAGEMENT = "daily_encouragement"
    WEEKLY_SUMMARY = "weekly_summary"
    MILESTONE_CELEBRATION = "milestone_celebration"
    HEALTH_REMINDER = "health_reminder"
    MISSION_REMINDER = "mission_reminder"

class EncouragementLevel(str, Enum):
    """격려 레벨"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    INTENSIVE = "intensive"

class ChatMessage(BaseModel):
    """채팅 메시지"""
    message_id: int = Field(..., description="메시지 ID")
    member_serial_number: int = Field(..., description="회원 일련번호")
    message_type: MessageType = Field(..., description="메시지 타입")
    message_content: str = Field(..., description="메시지 내용")
    response_content: Optional[str] = Field(default=None, description="응답 내용")
    created_at: datetime = Field(default_factory=datetime.now, description="생성일시")

class HealthDiagnosisResponse(BaseModel):
    """건강 진단 응답"""
    three_sentence_summary: List[str] = Field(..., description="3줄 요약")
    health_score: int = Field(..., description="건강 점수")
    risk_level: str = Field(..., description="위험 레벨")
    occupation_considerations: str = Field(..., description="직업별 고려사항")
    analysis_timestamp: datetime = Field(..., description="분석 시각")
    confidence_score: float = Field(..., description="신뢰도 점수")

class RecommendedMission(BaseModel):
    """추천 미션"""
    mission_id: str = Field(..., description="미션 ID")
    title: str = Field(..., description="미션 제목")
    description: str = Field(..., description="미션 설명")
    category: MissionCategory = Field(..., description="미션 카테고리")
    difficulty: DifficultyLevel = Field(..., description="난이도")
    health_benefit: str = Field(..., description="건강상 이점")
    occupation_relevance: str = Field(..., description="직업 연관성")
    estimated_time_minutes: int = Field(..., description="예상 소요 시간(분)")

class MissionRecommendationResponse(BaseModel):
    """미션 추천 응답"""
    missions: List[RecommendedMission] = Field(..., description="추천 미션 목록")
    recommendation_reason: str = Field(..., description="추천 사유")
    total_recommended: int = Field(..., description="전체 추천 수")

class ChatRequest(BaseModel):
    """채팅 요청"""
    message: str = Field(..., min_length=1, max_length=500, description="메시지 내용")
    session_id: str = Field(..., description="세션 ID")
    context: Optional[str] = Field(default=None, description="컨텍스트")
    user_id: str = Field(..., description="사용자 ID")

class ChatResponse(BaseModel):
    """채팅 응답"""
    response: str = Field(..., description="AI 응답")
    session_id: str = Field(..., description="세션 ID")
    timestamp: datetime = Field(..., description="응답 시각")
    suggested_questions: List[str] = Field(..., description="추천 질문")
    response_type: str = Field(..., description="응답 타입")

class ChatHistoryResponse(BaseModel):
    """채팅 이력 응답"""
    session_id: str = Field(..., description="세션 ID")
    messages: List[Dict[str, Any]] = Field(..., description="메시지 목록")
    total_message_count: int = Field(..., description="전체 메시지 수")
    cache_expiration: Optional[str] = Field(default=None, description="캐시 만료 시간")

class CelebrationRequest(BaseModel):
    """축하 메시지 요청"""
    user_id: str = Field(..., description="사용자 ID")
    mission_id: str = Field(..., description="미션 ID")
    achievement_type: str = Field(..., description="성취 타입")
    consecutive_days: int = Field(..., description="연속 달성 일수")
    total_achievements: int = Field(..., description="전체 성취 수")

class CelebrationResponse(BaseModel):
    """축하 메시지 응답"""
    congrats_message: str = Field(..., description="축하 메시지")
    achievement_badge: str = Field(..., description="성취 배지")
    health_benefit: str = Field(..., description="건강상 이점")
    next_milestone: str = Field(..., description="다음 마일스톤")
    encouragement_level: EncouragementLevel = Field(..., description="격려 레벨")
    visual_effect: str = Field(..., description="시각 효과")

class EncouragementRequest(BaseModel):
    """독려 메시지 요청"""
    user_id: str = Field(..., description="사용자 ID")
    missions_status: List[Dict[str, Any]] = Field(..., description="미션 상태 목록")

class EncouragementResponse(BaseModel):
    """독려 메시지 응답"""
    message: str = Field(..., description="독려 메시지")
    motivation_type: str = Field(..., description="동기부여 타입")
    timing: str = Field(..., description="타이밍")
    personalized_tip: str = Field(..., description="개인화된 팁")
    priority: str = Field(..., description="우선순위")

class BatchNotificationRequest(BaseModel):
    """배치 알림 요청"""
    trigger_time: datetime = Field(..., description="트리거 시간")
    target_users: List[str] = Field(..., description="대상 사용자 목록")
    notification_type: NotificationType = Field(..., description="알림 타입")

class BatchNotificationResponse(BaseModel):
    """배치 알림 응답"""
    processed_count: int = Field(..., description="처리된 수")
    success_count: int = Field(..., description="성공 수")
    failed_count: int = Field(..., description="실패 수")
    next_scheduled_time: Optional[datetime] = Field(default=None, description="다음 예약 시간")