expressionsList = ['+','-','*','/']
expression = []
storage = []


def cleanStorage():
    for i in storage:
        storage.remove(i)

def fillStorage(i):
    storage.append(i)

def cleanExpression():
    for i in expression:
        expression.remove(i)

def fillExpression(i):
    expression.append(i)

def math(e, x, y):
    if e == '+':
        x += y
    elif e == '-':
        x -= y
    elif e == '*':
        x *= y
    else:
        x /= y
    return round(x, 2)
    

def count():
    string = ''
    condition = True
    while condition == True:
        stringInput = input('Enter: ')
        try:
            stringInput = int(stringInput)
            string = string + str(stringInput)
        except ValueError:
            try:
                stringInput = float(stringInput)
                string = string + str(stringInput)
            except ValueError:
                fillExpression(stringInput)
                if len(storage) == 0:
                    try:
                        fillStorage(int(string))
                    except ValueError:
                        fillStorage(float(string))
                    condition = False
                else:
                    e = expression[0]
                    x = storage[0]
                    try:
                        y = int(string)
                    except ValueError:
                        y = float(string)

                    result = math(e, x, y)
                    cleanStorage()
                    fillStorage(result)
                    cleanExpression()
                print(storage)
                condition = False

def main():
    condition = True
    while condition == True:
        count()
main()