API_KEY = "test-1234567890" # 测试

def divide(a, b):
    if b == 0:
        raise ValueError("不能除以零")
    return a / b



if __name__ == "__main__":
    print(divide(10, 2))    # 输出: 5.0
    print(divide(10, 4))    # 输出: 2.5
