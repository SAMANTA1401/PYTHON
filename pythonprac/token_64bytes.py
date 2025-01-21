# Generate random secure token of 64 bytes and random URL
import secrets

print("random secure hexadecial token is",secrets.token_hex(64))
print("random secure url is",secrets.token_urlsafe(64))