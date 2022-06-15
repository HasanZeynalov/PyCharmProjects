import string
import secrets

alphabet = string.digits + string.ascii_letters
password = "".join(secrets.choice(alphabet) for i in range(8))
print(f"Your new password is {password}")


