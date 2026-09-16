from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/api/v1/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"
    assert data["service"] == "netdoctor-api"


def test_dashboard_overview():
    response = client.get("/api/v1/dashboard/overview")

    assert response.status_code == 200

    data = response.json()

    assert "health_score" in data
    assert "latency" in data
    assert "jitter" in data
    assert "packet_loss" in data
    assert "dns_latency" in data
    assert "diagnosis_summary" in data
    assert "traceroute" in data