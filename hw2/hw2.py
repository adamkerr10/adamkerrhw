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
                    int(num)
                    stack.append(num)
                else:
                    stack.append(":error:")
                    
            if "pop" in line:
                if not stack:
                    stack.append(":error:")
                else:
                    stack.pop()

            if "quit" in line:
                for x in stack:
                    ou.write(x)
                inp.close()
                ou.close()

            if ":true:" in line:
                stack.append(":true:")
                
            if ":false:" in line:
                stack.append(":false:")

                



        

hw2("sample_input1.txt", "sample_output1.txt")
