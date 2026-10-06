


class UserNotFoundException(Exception):
    pass

class UserAlreadyExistsException(Exception):
    pass

class InvalidePasswordException(Exception):
    pass

class SamePasswordException(Exception):
    pass

class UserCredentialsException(Exception):
    pass