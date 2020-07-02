from django.test import TestCase

# Create your tests here.
from django.contrib.auth.hashers import make_password, check_password

print(make_password('asdasd',None,'pbkdf2_sha256'))