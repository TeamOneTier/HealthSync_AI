"""
HealthSync AI 상태체크 뷰 (라우터 등록)
"""
from fastapi import APIRouter
from app.controllers.status_controller import status_controller

# 헬스체크 라우터 생성
status_router = APIRouter(
    prefix="/status",
    tags=["🏥 Status Check"],
    responses={
        404: {"description": "엔드포인트를 찾을 수 없습니다."},
        500: {"description": "서버 내부 오류가 발생했습니다."}
    }
)

# 상태체크 컨트롤러의 라우터 포함
status_router.include_router(status_controller.router)
