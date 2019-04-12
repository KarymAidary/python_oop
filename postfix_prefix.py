

expression = "3+9*5+7*(45^4+5)+(17/(24*79+4+7*6)*25)/(35+67*(5+√45+58))"
tokens = "+, -, *, /, ^, √, (, )"

def reverse(symbol):
    pass


def prefix(expression):
    a = expression[::-1]
    return a

print(prefix('a+b/(c-d)'))