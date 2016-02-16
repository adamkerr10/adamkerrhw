def hw1(input, output):
    def pangram(s):
        return not set('abcdefghijklmnopqrstuvwxyz') - set(s.lower())

    i = open(input, 'r')
    o = open(output, 'w')
    for line in i:
        pangram(line)

