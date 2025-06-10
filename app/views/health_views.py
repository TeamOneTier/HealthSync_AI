"""
HealthSync AI 헬스체크 뷰 (라우터 등록)
"""
from fastapi import APIRouter
from app.controllers.health_controller import health_controller

# 헬스체크 라우터 생성
health_router = APIRouter(
    prefix="/health",
    tags=["🏥 Health Check"],
    responses={
        404: {"description": "엔드포인트를 찾을 수 없습니다."},
        500: {"description": "서버 내부 오류가 발생했습니다."}
    }
)

# 헬스체크 컨트롤러의 라우터 포함
health_router.include_router(health_controller.router)
