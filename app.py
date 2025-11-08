# app.py

def greet(name):
    return f"Hello, {name}! This is Python 3.14.0 running in your virtual environment."

# --- 新增功能 ---
def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    print(greet("Developer"))

    # 调用新功能并打印结果
    result = add_numbers(5, 3)
    print(f"The result of 5 + 3 is: {result}")