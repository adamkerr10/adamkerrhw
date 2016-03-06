def hw2(input, output):
        def isInt(s):
            try:
                int(s)
                return True
            except ValueError:
                return False
        inp = open(input, 'r')
        ou = open(output, 'w')
        stack = []
        for line in inp:
                if "push" in line:
                        num = line[5:]
                        if isInt(num) == True:
                                newnum = num.strip('\n')
                                stack.append(newnum)
                        else:
                                stack.append(":error:")
                                
                if "pop" in line:
                        if not stack:
                                stack.append(":error:")
                        else:
                                stack.pop()

                if "quit" in line:
                        print("outputting, stack is %s" % stack)
                        for x in reversed(stack):
                                nl = x + "\n"
                                ou.write(nl)
                        inp.close()
                        ou.close()
                        return None
                                
                if ":true:" in line:
                        stack.append(":true:")

                if ":false:" in line:
                        stack.append(":false:")

                if ":error:" in line:
                        stack.append(":error:")

                if "add" in line:
                        size = len(stack)
                        if size != 0 and size != 1:
                                if isInt(stack[-1]) == True and isInt(stack[-2]) == True:
                                        num1 = stack[-1]
                                        stack.pop()
                                        num2 = stack[-1]
                                        stack.pop()
                                        int1 = int(num1)
                                        int2 = int(num2)
                                        result = int1+int2
                                        stringresult = str(result)
                                        stack.append(stringresult)
                                else:
                                        stack.append(":error:")
                        else:
                                stack.append(":error:")

                if "sub" in line:
                        size = len(stack)
                        if size != 0 and size != 1:
                                if isInt(stack[-1]) == True and isInt(stack[-2]) == True:
                                        num1 = stack[-1]
                                        stack.pop()
                                        num2 = stack[-1]
                                        stack.pop()
                                        int1 = int(num1)
                                        int2 = int(num2)
                                        result = int2-int1
                                        stringresult = str(result)
                                        stack.append(stringresult)
                                else:
                                        stack.append(":error:")
                        else:
                                stack.append(":error:")

                if "mul" in line:
                        size = len(stack)
                        if size != 0 and size != 1:
                                if isInt(stack[-1]) == True and isInt(stack[-2]) == True:
                                        num1 = stack[-1]
                                        stack.pop()
                                        num2 = stack[-1]
                                        stack.pop()
                                        int1 = int(num1)
                                        int2 = int(num2)
                                        result = int1*int2
                                        stringresult = str(result)
                                        stack.append(stringresult)
                                else:
                                        stack.append(":error:")
                        else:
                                stack.append(":error:")

                if "div" in line:
                        size = len(stack)
                        if size != 0 and size != 1:
                                if isInt(stack[-1]) == True and isInt(stack[-2]) == True:
                                        num1 = stack[-1]
                                        stack.pop()
                                        num2 = stack[-1]
                                        stack.pop()
                                        int1 = int(num1)
                                        int2 = int(num2)
                                        result = int2//int1
                                        stringresult = str(result)
                                        stack.append(stringresult)
                                else:
                                        stack.append(":error:")
                        else:
                                stack.append(":error:")

                if "rem" in line:
                        size = len(stack)
                        if size != 0 and size != 1:
                                if isInt(stack[-1]) == True and isInt(stack[-2]) == True:
                                        num1 = stack[-1]
                                        stack.pop()
                                        num2 = stack[-1]
                                        stack.pop()
                                        int1 = int(num1)
                                        int2 = int(num2)
                                        result = int2%int1
                                        stringresult = str(result)
                                        stack.append(stringresult)
                                else:
                                        stack.append(":error:")
                        else:
                                stack.append(":error:")

                if "neg" in line:
                        size = len(stack)
                        if size != 0:
                                if isInt(stack[-1]) == True:
                                        num1 = stack[-1]
                                        stack.pop()
                                        int1 = int(num1)
                                        result = -int1
                                        stringresult = str(result)
                                        stack.append(stringresult)
                                else:
                                        stack.append(":error:")
                        else:
                                stack.append(":error:")

                if "swap" in line:
                        size = len(stack)
                        if size != 0 and size != 1:
                                val1 = stack[-1]
                                stack.pop()
                                val2 = stack[-1]
                                stack.pop()
                                stack.append(val1)
                                stack.append(val2)
                        else:
                                stack.append(":error:")
                                

                



        


