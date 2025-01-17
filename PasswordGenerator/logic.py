import secrets
import string

CHARACTERS = string.ascii_letters + string.punctuation + string.digits


def generate_password(requested_length) -> str:
    """
    Called by the CreatePasswordLabels function,
    this function checks if the requested_length is valid,
    returns a password if it is,
    raises a value error if it's not.

    :param int requested_length: The length inputed by the user in the input box.
    :raises ValueError: if the requested_length is not an integer.
    """
    
    if requested_length > 0:
        # This is where the password itself is generated
        return ''.join(secrets.choice(CHARACTERS) for _ in range(min(int(requested_length), 100)))
    else:
        raise ValueError
