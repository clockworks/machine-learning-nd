


class Test():

    def __init__(self):
        self.Q = dict()
        print(self.Q)
        print("123")
        state = ('red', None, None, 'forward')
        print(state)



    def maxQ(self):
        self.Q = {'a':10,'b':3,'c':7,'d':1, 'e': 21, 'f':5}

        maxQ = None
        for key, value in self.Q.items():
            if maxQ == None or maxQ < value:
                maxQ = value


        print(maxQ)

 
if __name__ == '__main__':
    Test().maxQ()



