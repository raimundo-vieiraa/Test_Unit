def email_valido(email):
    return "@" in email and "." in email
def test_email_valido():
    assert email_valido("raimundoruan61@gmail.com")==True
    assert email_valido("renatin.com")==False
    assert email_valido("reinaldin@com")==False