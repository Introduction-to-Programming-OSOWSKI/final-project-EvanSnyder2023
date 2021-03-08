def times10(x):
    return x * 10

print (times10(3))

def firstA(w):
    word = w
    if w[0] == "a":
        return True
    else:
        return False

print (firstA("pple"))

def sizer(n):
    if n <= 10:
        return "small"
    if n == 67:
        return "medium"
    if n > 100:
        return "large"

print (sizer(67))

def doubleWord(w):
    word = w
    return w + w

print (doubleWord("pie"))

def penguin(p):
    if p == "king":
        return "increasing"
    if p == "macaroni":
        return "vulnerable"
    if p == "royal":
        return "near threatenend"
    if p == "african":
        return "endangered"

print (penguin("african"))