import os

API_KEY = os.getenv("API_KEY")

def divide(a, b):
    if b == 0:
        raise ValueError("b cannot be 0")
    return a / b

def login(username, password):
    return username == os.getenv("ADMIN_USER") and \
           password == os.getenv("ADMIN_PASSWORD")

print(divide(10, 2))   #輸出: 5.0

