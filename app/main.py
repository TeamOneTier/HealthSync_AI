"""
HealthSync AI - FastAPI 메인 애플리케이션 (MVC 패턴)
"""
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.exceptions import RequestValidationError
from app.views.health_views import health_router
from app.config.settings import settings
from app.models.base import ErrorResponse
import time
import logging
from datetime import datetime

# 로깅 설정
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("HealthSync_AI")

# FastAPI 앱 생성
app = FastAPI(
    title=settings.app_name,
    description=f"""
{settings.app_description}

### 기능

- ✅ **헬스체크**: 서비스 상태 모니터링
- ✅ **자동 문서화**: Swagger UI & ReDoc
- ✅ **성능 지표**: 메모리 사용량, 응답시간
- ✅ **로깅**: 구조화된 로그 시스템

### 기술 스택

- **Framework**: FastAPI {settings.app_version}
- **Pattern**: MVC (Model-View-Controller)
- **Language**: Python 3.11+
- **Docs**: OpenAPI 3.0

---

💡 **Tip**: 왼쪽 사이드바에서 API 엔드포인트를 탐색해보세요!
    """,
    version=settings.app_version,
    docs_url="/docs",
    redoc_url="/redoc"
)

# 요청 처리 시간 미들웨어
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    logger.info(f"📥 Request: {request.method} {request.url.path}")
    
    response = await call_next(request)
    
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(round(process_time, 4))
    response.headers["X-Service"] = settings.app_name
    
    logger.info(f"📤 Response: {request.method} {request.url.path} - Status: {response.status_code} - Time: {process_time:.4f}s")
    return response

# API 라우터 등록
app.include_router(health_router, prefix=settings.api_v1_prefix)

@app.get("/", include_in_schema=False)
async def root():
    """루트 경로 - API 문서로 리다이렉트"""
    return RedirectResponse(url="/docs")

# 예외 처리
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content=ErrorResponse(
            error_code="VALIDATION_ERROR",
            message="입력 데이터 검증에 실패했습니다.",
            details={"errors": exc.errors()},
            timestamp=datetime.now()
        ).dict()
    )

@app.on_event("startup")
async def startup_event():
    logger.info(f"🚀 {settings.app_name} v{settings.app_version} 서비스 시작")
    logger.info(f"📝 API 문서: http://{settings.host}:{settings.port}/docs")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("🛑 HealthSync AI 서비스 종료")
