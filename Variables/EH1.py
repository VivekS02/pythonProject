try:
    length = 10
    width = 0
    length/width
except NameError:
    print("Variable has been used before defining it")
except ZeroDivisionError:
    print("Division by zero is invalid kindly change ur input")
except Exception:
    print("New error")
finally:
    print("I will be executed atleast once")
