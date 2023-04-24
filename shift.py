class shift:
    a = []
    a.append(0)
    a.append(1)
    a.append(2)
    a.append(3)
    a.append(4)
    a.append(5)
    a.append(6)
    a.append(7)
    a.append(8)
    origin = 3
    print(a)
    print("origin", a[origin])
    shift_index = -6
    origin += shift_index
   
    start = 0
    end = len(a)
    
    print("After shift: ")
    if origin >= end:
        for element in a[:origin+1 - end]:
            a.append(0)
        print(a)
        for element in a[:origin]:
            a.remove(element)
            a.append(element)

    if origin <= start:
        for element in a[:(-1*origin)  - start]:
            a.append(0)
    
    print(a)
    print("origin: ",a[origin], ",", origin)
