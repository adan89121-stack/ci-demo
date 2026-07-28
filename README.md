import os

API_KEY = os.getenv("API_KEY")

def divide(a, b):
    if b == 0:
        raise ValueError("b cannot be 0")
    return a / b

def login(username, password):
    return username == os.getenv("ADMIN_USER") and \
           password == os.getenv("ADMIN_PASSWORD")

print(divide(10, 2))   

---------------------------------------------------------------

API_KEY = "123456789"

def divide(a, b):
    return a / b

def login(username, password):
    if username == "admin" and password == "123456":
        return True
    return False

print(divide(10, 0))
print(divide(10, 2))


請根據目前程式碼產生 R.md
