def hw3(input, output):
        fInput = open(input,'r')
        f = open(output,'w')
        stack = []
        for line in fInput:
                if line[0].isalpha():
                        parsePrimitive(line, stack, f)
                elif line[0] == ':':
                        parseBooleanOrError(line, stack)
        fInput.close()



def parsePrimitive(line, stack, f):
        if line.startswith('add'):
                doAdd(stack)
        elif line.startswith('sub'):
                doSub(stack)
        elif line.startswith('mul'):
                doMul(stack)
        elif line.startswith('div'):
                doDiv(stack)
        elif line.startswith('rem'):
                doRem(stack)
        elif line.startswith('pop'):
                doPop(stack)
        elif line.startswith('push'):
                doPush(stack, line)
        elif line.startswith('swap'):
                doSwap(stack)
        elif line.startswith('neg'):
                doNeg(stack)
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
                doBind(stack)

def doAdd(stack):
        if len(stack) < 2:
                return stack.insert(0, ':error:')
        elif stack[0][0] == ':' or stack[1][0] == ':':
                return stack.insert(0, ':error:')
        else:
                x = int(stack[1])
                y = int(stack[0])
                stack.pop(0)
                stack.pop(0)
                newTop = x+y
                return stack.insert(0, str(newTop))


def doSub(stack):
        if len(stack) < 2:
                return stack.insert(0, ':error:')
        elif stack[0][0] == ':' or stack[1][0] == ':':
                return stack.insert(0, ':error:')
        else:
                x = int(stack[1])
                y = int(stack[0])
                stack.pop(0)
                stack.pop(0)
                newTop = x-y
                return stack.insert(0, str(newTop))



def doMul(stack):
        if len(stack) < 2:
                return stack.insert(0, ':error:')
        elif stack[0][0] == ':' or stack[1][0] == ':':
                return stack.insert(0, ':error:')
        else:
                x = int(stack[1])
                y = int(stack[0])
                stack.pop(0)
                stack.pop(0)
                newTop = x*y
                return stack.insert(0, str(newTop))



def doDiv(stack):
	if len(stack) < 2:
		return stack.insert(0, ':error:')
	elif stack[0][0] == ':' or stack[1][0] == ':':
		return stack.insert(0, ':error:')
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



def doRem(stack):
	if len(stack) < 2:
		return stack.insert(0, ':error:')
	elif stack[0][0] == ':' or stack[1][0] == ':':
		return stack.insert(0, ':error:')
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
        elif stack[1] == ":true:" or stack[1] == ":false:" and stack[0] == ":true:" or stack[0] == ":false:":
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
        elif stack[1] == ":true:" or stack[1] == ":false:" and stack[0] == ":true:" or stack[0] == ":false:":
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


def doBind(stack):
        


def parseBooleanOrError(line, stack):
	if line[1] == 'e':
		return stack.insert(0,':error:')
	elif line[1] == 't':
		return stack.insert(0,':true:')
	else:
		return stack.insert(0,':false:')


hw3("input_2.txt","output_2.txt")















