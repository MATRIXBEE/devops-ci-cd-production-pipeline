def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Service is running"


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
