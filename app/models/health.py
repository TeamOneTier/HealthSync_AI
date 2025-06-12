# app/models/health.py
"""
HealthSync AI 건강 관련 모델
"""
from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import Optional, List, Dict, Any
from enum import Enum
from decimal import Decimal

class RiskLevel(str, Enum):
    """위험도 레벨"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class RangeStatus(str, Enum):
    """정상치 범위 상태"""
    NORMAL = "normal"
    WARNING = "warning"
    DANGER = "danger"

class UploadStatus(str, Enum):
    """업로드 상태"""
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"

class HealthCheckupRaw(BaseModel):
    """건강검진 원본 데이터"""
    raw_id: int = Field(..., description="원본 ID")
    reference_year: int = Field(..., description="기준 년도")
    birth_date: date = Field(..., description="생년월일")
    name: str = Field(..., description="이름")
    region_code: int = Field(..., description="지역 코드")
    gender_code: int = Field(..., description="성별 코드")
    age: int = Field(..., description="나이")
    height: int = Field(..., description="신장(cm)")
    weight: int = Field(..., description="체중(kg)")
    waist_circumference: int = Field(..., description="허리둘레(cm)")
    visual_acuity_left: Optional[Decimal] = Field(default=None, description="좌측 시력")
    visual_acuity_right: Optional[Decimal] = Field(default=None, description="우측 시력")
    hearing_left: Optional[int] = Field(default=None, description="좌측 청력")
    hearing_right: Optional[int] = Field(default=None, description="우측 청력")
    systolic_bp: Optional[int] = Field(default=None, description="수축기 혈압")
    diastolic_bp: Optional[int] = Field(default=None, description="이완기 혈압")
    fasting_glucose: Optional[int] = Field(default=None, description="공복혈당")
    total_cholesterol: Optional[int] = Field(default=None, description="총 콜레스테롤")
    triglyceride: Optional[int] = Field(default=None, description="중성지방")
    hdl_cholesterol: Optional[int] = Field(default=None, description="HDL 콜레스테롤")
    ldl_cholesterol: Optional[int] = Field(default=None, description="LDL 콜레스테롤")
    hemoglobin: Optional[Decimal] = Field(default=None, description="혈색소")
    urine_protein: Optional[int] = Field(default=None, description="요단백")
    serum_creatinine: Optional[Decimal] = Field(default=None, description="혈청크레아티닌")
    ast: Optional[int] = Field(default=None, description="AST")
    alt: Optional[int] = Field(default=None, description="ALT")
    gamma_gtp: Optional[int] = Field(default=None, description="감마지티피")
    smoking_status: Optional[int] = Field(default=None, description="흡연 상태")
    drinking_status: Optional[int] = Field(default=None, description="음주 상태")
    created_at: datetime = Field(default_factory=datetime.now, description="생성일시")

class HealthCheckup(BaseModel):
    """처리된 건강검진 데이터"""
    checkup_id: int = Field(..., description="건강검진 ID")
    member_serial_number: int = Field(..., description="회원 일련번호")
    raw_id: int = Field(..., description="원본 데이터 ID")
    reference_year: int = Field(..., description="기준 년도")
    age: int = Field(..., description="나이")
    height: int = Field(..., description="신장(cm)")
    weight: int = Field(..., description="체중(kg)")
    bmi: Optional[Decimal] = Field(default=None, description="BMI")
    waist_circumference: int = Field(..., description="허리둘레(cm)")
    visual_acuity_left: Optional[Decimal] = Field(default=None, description="좌측 시력")
    visual_acuity_right: Optional[Decimal] = Field(default=None, description="우측 시력")
    hearing_left: Optional[int] = Field(default=None, description="좌측 청력")
    hearing_right: Optional[int] = Field(default=None, description="우측 청력")
    systolic_bp: Optional[int] = Field(default=None, description="수축기 혈압")
    diastolic_bp: Optional[int] = Field(default=None, description="이완기 혈압")
    fasting_glucose: Optional[int] = Field(default=None, description="공복혈당")
    total_cholesterol: Optional[int] = Field(default=None, description="총 콜레스테롤")
    triglyceride: Optional[int] = Field(default=None, description="중성지방")
    hdl_cholesterol: Optional[int] = Field(default=None, description="HDL 콜레스테롤")
    ldl_cholesterol: Optional[int] = Field(default=None, description="LDL 콜레스테롤")
    hemoglobin: Optional[Decimal] = Field(default=None, description="혈색소")
    urine_protein: Optional[int] = Field(default=None, description="요단백")
    serum_creatinine: Optional[Decimal] = Field(default=None, description="혈청크레아티닌")
    ast: Optional[int] = Field(default=None, description="AST")
    alt: Optional[int] = Field(default=None, description="ALT")
    gamma_gtp: Optional[int] = Field(default=None, description="감마지티피")
    smoking_status: Optional[int] = Field(default=None, description="흡연 상태")
    drinking_status: Optional[int] = Field(default=None, description="음주 상태")
    processed_at: datetime = Field(default_factory=datetime.now, description="처리일시")
    created_at: datetime = Field(default_factory=datetime.now, description="생성일시")

class HealthNormalRange(BaseModel):
    """건강 정상치 기준"""
    range_id: int = Field(..., description="범위 ID")
    health_item_code: str = Field(..., description="건강항목 코드")
    health_item_name: str = Field(..., description="건강항목명")
    gender_code: int = Field(..., description="성별 코드 (0:공통, 1:남성, 2:여성)")
    unit: str = Field(..., description="단위")
    normal_range: str = Field(..., description="정상 범위")
    warning_range: str = Field(..., description="주의 범위")
    danger_range: str = Field(..., description="위험 범위")
    note: Optional[str] = Field(default=None, description="비고")
    created_at: datetime = Field(default_factory=datetime.now, description="생성일시")

class HealthSyncResponse(BaseModel):
    """건강검진 연동 응답"""
    sync_status: str = Field(..., description="동기화 상태")
    message: str = Field(..., description="응답 메시지")
    is_ready_for_analysis: bool = Field(..., description="분석 준비 여부")
    synced_at: datetime = Field(..., description="동기화 일시")

class HealthHistoryResponse(BaseModel):
    """건강검진 이력 응답"""
    user_info: Dict[str, Any] = Field(..., description="사용자 정보")
    checkup_records: List[Dict[str, Any]] = Field(..., description="건강검진 기록")
    chart_data: Optional[Dict[str, Any]] = Field(default=None, description="차트 데이터")
    normal_range_reference: Optional[Dict[str, Any]] = Field(default=None, description="정상치 기준")

class CheckupFileRequest(BaseModel):
    """건강검진 파일 업로드 요청"""
    user_id: str = Field(..., description="사용자 ID")
    file_name: str = Field(..., description="파일명")
    file_type: str = Field(..., description="파일 형식")
    file_content: str = Field(..., description="파일 내용")

class FileUploadResponse(BaseModel):
    """파일 업로드 응답"""
    file_id: str = Field(..., description="파일 ID")
    upload_url: str = Field(..., description="업로드 URL")
    status: str = Field(..., description="업로드 상태")
    message: str = Field(..., description="응답 메시지")