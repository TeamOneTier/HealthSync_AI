"""
HealthSync AI 애플리케이션 설정 관리
"""
from pydantic_settings import BaseSettings
from typing import List, Optional
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

class Settings(BaseSettings):
    """HealthSync AI 애플리케이션 설정 클래스"""
    
    # 기본 앱 설정
    app_name: str = "HealthSync AI"
    app_version: str = "1.0.0"
    debug: bool = True
    app_description: str = "AI 기반 개인 맞춤형 건강관리 서비스"
    
    # 서버 설정
    host: str = "localhost"
    port: int = 8000
    
    # 보안 설정
    secret_key: str = "healthsync-ai-secret-key-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # API 설정
    api_v1_prefix: str = "/api/v1"
    cors_origins: List[str] = ["*"]
    
    # 데이터베이스 설정
    database_url: str = "sqlite:///./healthsync_ai.db"
    
    # 로깅 설정
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = False

# 전역 설정 인스턴스
settings = Settings()
