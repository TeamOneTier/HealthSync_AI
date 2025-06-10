# HealthSync AI

AI 기반 개인 맞춤형 건강관리 서비스 - FastAPI MVC 패턴 백엔드

## 🏥 서비스 개요

HealthSync AI는 개인의 건강 데이터를 분석하여 맞춤형 건강 관리 솔루션을 제공하는 AI 기반 플랫폼입니다.

## 🏗️ MVC 패턴 아키텍처

```
📁 HealthSync_AI/
├── 📊 Model (app/models/): 데이터 구조 정의
├── 🌐 View (app/views/): API 라우팅 관리
├── 🎮 Controller (app/controllers/): 요청/응답 처리
├── ⚙️ Service (app/services/): 비즈니스 로직
├── 🔧 Core (app/core/): 공통 기능
├── ⚙️ Config (app/config/): 설정 관리
└── 🛠️ Utils (app/utils/): 유틸리티
```

## 🚀 빠른 시작

### 자동 설치 (권장)
```bash
# setup.sh 스크립트로 자동 생성 및 실행
chmod +x setup.sh
./setup.sh
```

### 수동 설치
```bash
# 의존성 설치
pip install -r requirements.txt

# 서버 실행
python run.py
```

## 📡 API 엔드포인트

- **🏠 메인**: http://localhost:8000
- **📚 API 문서**: http://localhost:8000/docs
- **🏥 헬스체크**: http://localhost:8000/api/v1/health/status

## 🧪 테스트 실행

```bash
pytest tests/
```

## 📝 개발 가이드

새로운 기능 추가 시:
1. **Model**: `app/models/` - 데이터 구조 정의
2. **Service**: `app/services/` - 비즈니스 로직 구현
3. **Controller**: `app/controllers/` - API 로직 작성
4. **View**: `app/views/` - 라우터 등록

## 📄 라이선스

MIT License

---
**Built with ❤️ for Healthcare** | **HealthSync AI Team**
