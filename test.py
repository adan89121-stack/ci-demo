API_KEY = "123456789"

def divide(a, b):
    return a / b  

def login(username, password):
    if username == "admin" and password == "123456":
        return True 
    return False

print(divide(10, 0))    #輸出: ZeroDivisionError: division by zero
print(divide(10, 2))    #輸出: 5.0
print(divide(10, 5))    #輸出: 2.0
