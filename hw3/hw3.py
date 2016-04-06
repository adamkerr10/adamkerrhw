def hw3(input, output):
        fInput = open(input,'r')
        f = open(output,'w')
        stack = []
        map1 = {}
        for line in fInput:
                if line[0].isalpha():
                        parsePrimitive(line, stack, f, map1)
                elif line[0] == ':':
                        parseBooleanOrError(line, stack)
        fInput.close()


def parsePrimitive(line, stack, f, map1):
        if line.startswith('add'):
                doAdd(stack, map1)
        elif line.startswith('sub'):
                doSub(stack, map1)
        elif line.startswith('mul'):
                doMul(stack, map1)
        elif line.startswith('div'):
                doDiv(stack, map1)
        elif line.startswith('rem'):
                doRem(stack, map1)
        elif line.startswith('pop'):
                doPop(stack, map1)
        elif line.startswith('push'):
                doPush(stack, line)
        elif line.startswith('swap'):
                doSwap(stack, map1)
        elif line.startswith('neg'):
                doNeg(stack, map1)
        elif line.startswith('quit'):
                doQuit(stack, f)
        elif line.startswith('and'):
                doAnd(stack)
        elif line.startswith('or'):
                doOr(stack)
        elif line.startswith('not'):
                doNot(stack)
        elif line.startswith('equal'):
                doEqual(stack)
        elif line.startswith('lessThan'):
                doLessThan(stack)
        elif line.startswith('bind'):
                doBind(stack, map1)
        elif line.startswith('if'):
                doIf(stack)

def doAdd(stack, map1):
        if len(stack) < 2:
                return stack.insert(0, ':error:')
        elif stack[0][0] == ':' or stack[1][0] == ':':
                return stack.insert(0, ':error:')
        elif stack[0] in map1 and stack[1] in map1:
                xValue = map1[stack[1]]
                x = int(xValue)
                yValue = map1[stack[0]]
                y = int(yValue)
                stack.pop(0)
                stack.pop(0)
                newTop = x+y
                return stack.insert(0, str(newTop))
        elif stack[0] in map1:
                xValue = map1[stack[1]]
                x = int(xValue)
                y = int(stack[0])
                stack.pop(0)
                stack.pop(0)
                newTop = x+y
                return stack.insert(0, str(newTop))
        elif stack[1] in map1:
                yValue = map1[stack[0]]
                y = int(yValue)
                x = int(stack[1])
                stack.pop(0)
                stack.pop(0)
                newTop = x+y
                return stack.insert(0, str(newTop))
        else:
                x = int(stack[1])
                y = int(stack[0])
                stack.pop(0)
                stack.pop(0)
                newTop = x+y
                return stack.insert(0, str(newTop))


def doSub(stack, map1):
        if len(stack) < 2:
                return stack.insert(0, ':error:')
        elif stack[0][0] == ':' or stack[1][0] == ':':
                return stack.insert(0, ':error:')
        elif stack[0] in map1 and stack[1] in map1:
                xValue = map1[stack[1]]
                x = int(xValue)
                yValue = map1[stack[0]]
                y = int(yValue)
                stack.pop(0)
                stack.pop(0)
                newTop = x-y
                return stack.insert(0, str(newTop))
        elif stack[0] in map1:
                xValue = map1[stack[1]]
                x = int(xValue)
                y = int(stack[0])
                stack.pop(0)
                stack.pop(0)
                newTop = x-y
                return stack.insert(0, str(newTop))
        elif stack[1] in map1:
                yValue = map1[stack[0]]
                y = int(yValue)
                x = int(stack[1])
                stack.pop(0)
                stack.pop(0)
                newTop = x-y
                return stack.insert(0, str(newTop))
        else:
                x = int(stack[1])
                y = int(stack[0])
                stack.pop(0)
                stack.pop(0)
                newTop = x-y
                return stack.insert(0, str(newTop))



def doMul(stack, map1):
        if len(stack) < 2:
                return stack.insert(0, ':error:')
        elif stack[0][0] == ':' or stack[1][0] == ':':
                return stack.insert(0, ':error:')
        elif stack[0] in map1 and stack[1] in map1:
                xValue = map1[stack[1]]
                x = int(xValue)
                yValue = map1[stack[0]]
                y = int(yValue)
                stack.pop(0)
                stack.pop(0)
                newTop = x*y
                return stack.insert(0, str(newTop))
        elif stack[0] in map1:
                xValue = map1[stack[1]]
                x = int(xValue)
                y = int(stack[0])
                stack.pop(0)
                stack.pop(0)
                newTop = x*y
                return stack.insert(0, str(newTop))
        elif stack[1] in map1:
                yValue = map1[stack[1]]
                y = int(yValue)
                x = int(stack[0])
                stack.pop(0)
                stack.pop(0)
                newTop = x*y
                return stack.insert(0, str(newTop))
        else:
                x = int(stack[1])
                y = int(stack[0])
                stack.pop(0)
                stack.pop(0)
                newTop = x*y
                return stack.insert(0, str(newTop))



def doDiv(stack, map1):
        if len(stack) < 2:
                return stack.insert(0, ':error:')
        elif stack[0][0] == ':' or stack[1][0] == ':':
                return stack.insert(0, ':error:')
        elif stack[0] in map1 and stack[1] in map1:
                xValue = map1[stack[1]]
                x = int(xValue)
                yValue = map1[stack[0]]
                y = int(yValue)
                stack.pop(0)
                stack.pop(0)
                newTop = x//y
                return stack.insert(0, str(newTop))
        elif stack[0] in map1:
                xValue = map1[stack[1]]
                x = int(xValue)
                y = int(stack[0])
                stack.pop(0)
                stack.pop(0)
                newTop = x//y
                return stack.insert(0, str(newTop))
        elif stack[1] in map1:
                yValue = map1[stack[0]]
                y = int(yValue)
                x = int(stack[1])
                stack.pop(0)
                stack.pop(0)
                newTop = x//y
                return stack.insert(0, str(newTop))
        else:
                x = int(stack[1])
                y = int(stack[0])
                if y == 0:
                        return stack.insert(0, ':error:')
                else:
                        stack.pop(0)
                        stack.pop(0)
                        newTop = x//y
                        return stack.insert(0, str(newTop))



def doRem(stack, map1):
        if len(stack) < 2:
                return stack.insert(0, ':error:')
        elif stack[0][0] == ':' or stack[1][0] == ':':
                return stack.insert(0, ':error:')
        elif stack[0] in map1 and stack[1] in map1:
                xValue = map1[stack[1]]
                x = int(xValue)
                yValue = map1[stack[0]]
                y = int(yValue)
                stack.pop(0)
                stack.pop(0)
                newTop = x % y
                return stack.insert(0, str(newTop))
        elif stack[0] in map1:
                xValue = map1[stack[1]]
                x = int(xValue)
                y = int(stack[0])
                stack.pop(0)
                stack.pop(0)
                newTop = x % y
                return stack.insert(0, str(newTop))
        elif stack[1] in map1:
                yValue = map1[stack[0]]
                y = int(yValue)
                x = int(stack[1])
                stack.pop(0)
                stack.pop(0)
                newTop = x % y
                return stack.insert(0, str(newTop))
        else:
                x = int(stack[1])
                y = int(stack[0])
                if y == 0:
                        return stack.insert(0, ':error:')
                else:
                        stack.pop(0)
                        stack.pop(0)
                        newTop = x % y
                        return stack.insert(0, str(newTop))


def doPop(stack):
	if len(stack) < 1:
		return stack.insert(0, ':error:')
	else:
		return stack.pop(0)


def doPush(stack, line):
        getList = line.split()
        if getList[1][0] == '-':
                if getList[1][1:] == '0':
                        return stack.insert(0,'0')
                elif getList[1][1:].isdigit():
                        return stack.insert(0, getList[1])
                else:
                        return stack.insert(0, ':error:')
        elif getList[1].isdigit():
                return stack.insert(0, getList[1])
        elif getList[1].startswith("\"") and getList[1].endswith("\""):
                noQuotes = getList[1][1:-1]
                return stack.insert(0, noQuotes)
        elif getList[1][0].isalpha():
                return stack.insert(0, getList[1])
        else:
                return stack.insert(0, ':error:')


def doSwap(stack):
	if len(stack) < 2:
		return stack.insert(0, ':error:')
	else:
		x = stack[1]
		y = stack[0]
		stack.pop(0)
		stack.pop(0)
		stack.insert(0, y)
		return stack.insert(0, x)


def doNeg(stack):
	if len(stack) < 1:
		return stack.insert(0, ':error:')
	elif stack[0][0] == ':':
		return stack.insert(0, ':error:')
	else:
		x = int(stack[0])
		stack.pop(0)
		newTop = -1*x
		return stack.insert(0, str(newTop))


def doQuit(stack, f):
	for ele in stack:
		f.write(ele + '\n')
	f.close()


def doAnd(stack):
        if len(stack) < 2:
                return stack.insert(0, ':error:')
        elif (stack[1] == ":true:" or stack[1] == ":false:") and (stack[0] == ":true:" or stack[0] == ":false:"):
                x = stack[1]
                y = stack[0]
                stack.pop(0)
                stack.pop(0)
                if x == ":true:":
                        x = True
                if y == ":true:":
                        y = True
                if x == ":false:":
                        x = False
                if y == ":false:":
                        y = False
                newTop = x and y
                if newTop == True:
                        newTop = ":true:"
                if newTop == False:
                        newTop = ":false:"
                return stack.insert(0, newTop)
        else:
                return stack.insert(0, ':error:')


def doOr(stack):
        if len(stack) < 2:
                return stack.insert(0, ':error:')
        elif (stack[1] == ":true:" or stack[1] == ":false:") and (stack[0] == ":true:" or stack[0] == ":false:"):
                x = stack[1]
                y = stack[0]
                stack.pop(0)
                stack.pop(0)
                if x == ":true:":
                        x = True
                if y == ":true:":
                        y = True
                if x == ":false:":
                        x = False
                if y == ":false:":
                        y = False
                newTop = x or y
                if newTop == True:
                        newTop = ":true:"
                if newTop == False:
                        newTop = ":false:"
                return stack.insert(0, newTop)
        else:
                return stack.insert(0, ':error:')

def doNot(stack):
        if len(stack) < 1:
                return stack.insert(0, ':error:')
        elif stack[0] == ":true:" or stack[0] == ":false:":
                x = stack[0]
                stack.pop(0)
                if x == ":true:":
                        x = True
                if x == ":false:":
                        x = False
                newTop = not x
                if newTop == True:
                        newTop = ":true:"
                if newTop == False:
                        newTop = ":false:"
                return stack.insert(0, newTop)
        else:
                return stack.insert(0, ':error:')


def doEqual(stack):
        if len(stack) < 2:
                return stack.insert(0, ':error:')
        elif isinstance(int(stack[0]), int) and isinstance(int(stack[1]), int):
                x = int(stack[1])
                y = int(stack[0])
                stack.pop(0)
                stack.pop(0)
                newTop = (x == y)
                if newTop == True:
                        newTop = ":true:"
                if newTop == False:
                        newTop = ":false:"
                return stack.insert(0, newTop)
        else:
                return stack.insert(0, ':error:')


def doLessThan(stack):
        if len(stack) < 2:
                return stack.insert(0, ':error:')
        elif isinstance(int(stack[0]), int) and isinstance(int(stack[1]), int):
                x = int(stack[1])
                y = int(stack[0])
                stack.pop(0)
                stack.pop(0)
                newTop = (x < y)
                if newTop == True:
                        newTop = ":true:"
                if newTop == False:
                        newTop = ":false:"
                return stack.insert(0, newTop)
        else:
                return stack.insert(0, ':error:')


def doBind(stack, map1):
        if len(stack) < 1:
                return stack.insert(0, ':error:')
        else:
                x = stack[1]
                y = stack[0]
                stack.pop(0)
                stack.pop(0)
                map1[x] = y
                return stack.insert(0, ':unit:')
                
def doIf(stack):
        if len(stack) < 3:
                return stack.insert(0, ':error:')
        elif stack[2] == ":true:" or stack[2] == ":false:":
                z = stack[2]
                y = stack[1]
                x = stack[0]
                stack.pop(0)
                stack.pop(0)
                stack.pop(0)
                if z == ":true:":
                        return stack.insert(0, x)
                if z == ":false:":
                        return stack.insert(0,y)
        else:
                return stack.insert(0, ':error:')

def parseBooleanOrError(line, stack):
	if line[1] == 'e':
		return stack.insert(0,':error:')
	elif line[1] == 't':
		return stack.insert(0,':true:')
	else:
		return stack.insert(0,':false:')


hw3("input_9.txt","output_9.txt")















