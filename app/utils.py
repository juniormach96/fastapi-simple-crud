from passlib.context import CryptContext

# Helper for hashing passwords using different algorithms
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    """ Returns hashed password from password input """
    return pwd_context.hash(password)


def verify(plain_password, hashed_password):
    """ Asserts the hashed password from input equals to the hashed password stored on db """
    return pwd_context.verify(plain_password, hashed_password)
