class Scale_Signals:
    def __init__(self, array, origin):
        self.__origin = origin
        
        self.__signal_array = array
        self.__left = 0
        self.__right = len(self.__signal_array) - 1
        
        self.__scaled_signal = []
        
    def initSignals(self):
        new_signal = []
        for i in range(self.__origin, len(self.__signal_array)):
            new_signal.append(self.__signal_array[i])
        
        self.__right = len(new_signal) - 1
        
        for i in range(self.__origin):
            new_signal.append(self.__signal_array[i])
        
        self.__left = self.__right - len(self.__signal_array) + 1
        self.__signal_array = new_signal
    
    def isDivisible(self, diviser, constant):
        return diviser % constant == 0
    
    def Scale(self, constant):
        if constant > 1:
            for i in range(self.__right + 1):
                if self.isDivisible(i, constant):
                    self.__scaled_signal.append(self.__signal_array[i])
            for i in range(self.__left, 0):
                if self.isDivisible(i, constant):
                    self.__scaled_signal.append(self.__signal_array[i])
        
        elif constant > 0:
            for i in range(len(self.__signal_array)):
                self.__scaled_signal.append(self.__signal_array[i])
                for j in range(int(pow(constant, -1)) - 1):
                    self.__scaled_signal.append(0)
            
       
    def Debug(self):
        print(self.__signal_array)
        print(self.__left)
        print(self.__right)
        print(self.__scaled_signal)
        
        


run = Scale_Signals([1, 2, 3, 4, 5, 6], 3)
run.initSignals()
run.Scale(1/2)
run.Debug()