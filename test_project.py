import project

def test_verify_user_email():
    assert project.verify_user_email("art@gmail.com") == True
    assert project.verify_user_email("randomthings") == False

def test_verify_user_password():
    assert project.verify_user_password("1234") == False
    assert project.verify_user_password("5dsadsad") == True

def test_verify_user_email_sign_up():
    assert project.verify_user_email_sign_up("art@gmail.com") == False
    assert project.verify_user_email_sign_up("withoutat") == True