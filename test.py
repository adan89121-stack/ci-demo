def divide(a, b):   # 
    if b == 0:      
        raise ValueError("不能除以零")
    return a / b      
    

if __name__ == "__main__":
    print(divide(10, 2))   # This will print 5.0
    print(divide(10, 0))    # This will raise a ValueError with the message "不能除以零"
    