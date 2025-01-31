from werkzeug.security import generate_password_hash, check_password_hash

class Auth:
    @staticmethod
    def hash_password(password):
        """Hash a password for storing."""
        return generate_password_hash(password)

    @staticmethod
    def verify_password(stored_password, provided_password):
        """Verify a stored password against one provided by user."""
        return check_password_hash(stored_password, provided_password)