#  Generate 6 digit random secure OTP
import secrets
OTPgenerator=secrets.SystemRandom()
print("six digit random otp")
otp = OTPgenerator.randrange(100000,999999)
print("secure otp  is ",otp)