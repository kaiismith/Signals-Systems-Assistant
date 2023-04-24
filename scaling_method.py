class Scale_Signals:
    def __init__(self, array, origin):        
        self.__signal_array, self.__left, self.__right = self.initSignals(array, origin)
        
        self.__scaled_signal = []
        self.__new_left = 0
        self.__new_right = 0
        
    def initSignals(self, array, origin): #transform signals to special form
        new_signal = []
        for i in range(origin, len(array)):
            new_signal.append(array[i])
        
        right = len(new_signal) - 1
        
        for i in range(origin):
            new_signal.append(array[i])
        
        left = right - len(array) + 1
        
        return new_signal, left, right
    
    def isDivisible(self, diviser, constant):
        return diviser % constant == 0
    
    def Scale(self, constant): #scale signals method
        print("Scale " + str(constant))
        if constant > 1:
            for i in range(self.__left, self.__right + 1):
                if self.isDivisible(i, constant):
                    self.__scaled_signal.append(self.__signal_array[i])
                if i == 0:
                    origin = len(self.__scaled_signal) - 1
                    
            self.__scaled_signal, self.__new_left, self.__new_right = self.initSignals(self.__scaled_signal, origin)
            
        elif constant > 0:            
            for i in range(len(self.__signal_array)):
                self.__scaled_signal.append(self.__signal_array[i])
                if i == self.__right:
                    self.__new_right = len(self.__scaled_signal) - 1 
                else:
                    for j in range(int(pow(constant, -1)) - 1):
                        self.__scaled_signal.append(0) 
            
            self.__new_left = self.__new_right - len(self.__scaled_signal) + 1
              
    def Debug(self): #method that showing all the information
        print("Signal: ", self.__signal_array)
        print("Left: ", self.__left)
        print("Right: ", self.__right)
        
        print("Scaled signal: ", self.__scaled_signal)
        print("New left: ", self.__new_left)
        print("New right: ", self.__new_right)
        


run = Scale_Signals([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
run.Scale(3)
run.Debug()