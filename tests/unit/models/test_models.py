from models.user import UserModel


def test_new_user():
    """
    Test create new User
    check new user and password is correct
    """
    user = UserModel("usertest","letstest")
    assert user.username == "usertest"
    assert user.password != "letstest"
