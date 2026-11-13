from app import app


def test_home_endpoint():
    tester = app.test_client()
    response = tester.get("/")

    assert response.status_code == 200
    assert response.json["application"] == "CloudOps Monitor"


def test_health_endpoint():
    tester = app.test_client()
    response = tester.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_system_endpoint():
    tester = app.test_client()
    response = tester.get("/system")

    assert response.status_code == 200
    assert "operating_system" in response.json