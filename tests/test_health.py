"""
HealthSync AI 헬스체크 API 테스트
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestHealthAPI:
    """헬스체크 API 테스트 클래스"""
    
    def test_health_status(self):
        """헬스체크 상태 엔드포인트 테스트"""
        response = client.get("/api/v1/health/status")
        assert response.status_code == 200
        
        data = response.json()
        assert data["status"] == "healthy"
        assert data["service"] == "HealthSync AI"
        assert "version" in data
        assert "timestamp" in data
        assert "environment" in data
    
    def test_root_redirect(self):
        """루트 경로 리다이렉트 테스트"""
        response = client.get("/", allow_redirects=False)
        assert response.status_code == 307
        assert "/docs" in response.headers["location"]
