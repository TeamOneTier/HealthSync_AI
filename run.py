"""
HealthSync AI 서버 실행 스크립트
"""
import uvicorn
from app.main import app
from app.config.settings import settings

def main():
    """메인 실행 함수"""
    print(f"🚀 {settings.app_name} 서버 시작...")
    print(f"📍 주소: http://{settings.host}:{settings.port}")
    print(f"📖 API 문서: http://{settings.host}:{settings.port}/docs")
    
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
        log_level=settings.log_level.lower()
    )

if __name__ == "__main__":
    main()
