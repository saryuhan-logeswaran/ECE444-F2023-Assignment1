class utils:
    def reversed(self, num):
        reversedNum = int(str(int(float(num)))[::-1])
        return reversedNum
    
    def formatter(self, num):
        binNum = "{0:b}".format(int(float(num)))
        octNum = "{0:o}".format(int(float(num)))
        return binNum, octNum