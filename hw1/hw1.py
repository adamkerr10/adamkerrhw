def hw1(input, output):
    def pangram(s):
        return not set('abcdefghijklmnopqrstuvwxyz') - set(s.lower())

    i = open(input, 'r')
    o = open(output, 'w')
    for line in i:
        result = pangram(line)
        if result == True:
            o.write('true\n')
        else:
            o.write('false\n')
    i.close()
    o.close()
    
