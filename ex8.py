equation = input("Podaj działanie: ")
try:
    print(eval(equation))
except ZeroDivisionError:
    print("Nigdy cholero nie dziel przez zero!")
except (NameError, SyntaxError):
    print("nie ma")
