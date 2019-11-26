def test_home_page(test_client):
    """
    When the '/' page is requested (GET)
    Then check if the status code is 404 (NOT FOUND)
    """
    response = test_client.get('/')
    assert response.status_code == 404
