def divide(a, b):
    if b == 0:
        raise ValueError("不能除以零")
    return a / b

API_KEY = "sk-test-1234567890" # API 密鑰

if __name__ == "__main__":
    print(divide(10, 2)) # 10 除以 2 的結果
    print(15/3)  # 15 除以 3 的結果
    print(16/2)   # 16 除以 2 的結果   
    