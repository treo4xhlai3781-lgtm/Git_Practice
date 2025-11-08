# app.py

# 1. greet 函数定义 (修复缺失部分)
def greet(name):
    return f"Hello, {name}! This is Python 3.14.0 running in your virtual environment."

# 2. add_numbers 函数定义
def add_numbers(a, b):
    return a + b

# 3. multiply_numbers 函数定义 
def multiply_numbers(a, b):
    return a * b

if __name__ == "__main__":
    print(greet("Developer")) # <- 确保 greet 在这里被调用时是定义的
    
    result_add = add_numbers(5, 3)
    print(f"The result of 5 + 3 is: {result_add}")

    result_mult = multiply_numbers(5, 3)
    print(f"The result of 5 * 3 is: {result_mult}")