# ci-demo
test

def divide(a, b):
    if b == 0:
        raise ValueError("不能除以零")
    return a / b


if __name__ == "__main__":
    print(divide(10, 2))

-----------------------------------------------------------

API_KEY = "sk-test-1234567890"

def divide(a, b):
    return a / b


if __name__ == "__main__":
    print(divide(10, 2))
    print(divide(10, 0))


    ---------------


test
