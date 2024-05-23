from app.models import User
from tests.config_test import client, app

def test_login_logout(client):
    rv = client.post('/auth/login', data={
        'email': 'kevin@gmail.com', 
        'password': 'sfsdafsd'}, follow_redirects=True)

    assert rv.status_code == 200

    """
    with open('response_output.html', 'w', encoding='utf-8') as f:
        f.write(rv.data.decode('utf-8'))
    
    import webbrowser
    webbrowser.open('response_output.html')
    """
    assert b'The username or password you entered is incorrect!' in rv.data

    rv = client.post('/auth/login', data={
        'email': 'kevin@gmail.com', 
        'password': '1234'}, follow_redirects=True)
