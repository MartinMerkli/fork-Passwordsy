import secrets
import string

characters = string.ascii_letters + string.punctuation

def GeneratePassword(requested_length) -> str:
    '''
    Checks if the requested requested_length is valid,
    returns a password if it is,
    raises a value error if it's not.
    '''

    if 1 <= requested_length:
        if requested_length > 100:
            requested_length = 100

        return ''.join(secrets.choice(characters) for i in range(requested_length)) # This is where the password itself is generated.

    else:
        raise ValueError