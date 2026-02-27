def test_get_activities(client):
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert all('participants' in v for v in data.values())


def test_signup_success(client):
    response = client.post("/activities/Soccer Team/signup", json={"email": "test@example.com"})
    assert response.status_code == 200
    assert response.json()["message"].startswith("Signed up")
    # Sprawdź, czy email został dodany
    get_resp = client.get("/activities")
    assert "test@example.com" in get_resp.json()["Soccer Team"]["participants"]

def test_signup_duplicate(client):
    client.post("/activities/Soccer Team/signup", json={"email": "test@example.com"})
    response = client.post("/activities/Soccer Team/signup", json={"email": "test@example.com"})
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]

def test_signup_nonexistent_activity(client):
    response = client.post("/activities/nonexistent/signup", json={"email": "test@example.com"})
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]

def test_root_redirect(client):
    response = client.get("/")
    assert response.status_code in (200, 307, 308)
    # FastAPI może zwrócić przekierowanie lub bezpośrednio plik statyczny
