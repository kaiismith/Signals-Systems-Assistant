x = [1, 1, 1]
h = [1, -2, 3] 

originX = 0 # NOT REAL ORIGIN

def point_arrow(arr, origin): # ALMOST CORRECT
    output ="         "
    for i in range(len(arr[:origin])):
        if arr[i] >= 0:
            if arr[i+1] >= 0:
                output += (len(str(arr[i])) + 1) * " " + " "
            else:
                output += (len(str(arr[i])) + 1) * " " + "  "
        elif arr[i] < 0:
            output += len(str(arr[i])) * " " + " "
    print(output + "^")          

def normalize(arr, origin=0):
    for element in arr[:origin]:
        arr.remove(element)
        arr.append(element)

    return arr, origin

def de_normalize(arr, origin): # WRONG
    temp = arr[-origin:]
    arr = temp + arr[0:-origin]

    return arr

def shift(arr, origin=0, shift_unit=0):
    if shift_unit > 0:
        for i in range(shift_unit):
            if origin >= 0:
                
                origin += 1
                if origin == len(arr):
                    arr.append(0)
    elif shift_unit < 0:
        for i in range(abs(shift_unit)):
            origin -= 1
            if origin < 0:
                arr.insert(0, 0)
                
    if origin < 0:
        origin = 0

    return normalize(arr, origin)
    
def flip(arr, origin=0):
    arr_1 = arr[0:origin][::-1]
    arr_2 = arr[origin + 1:][::-1]

    arr = arr_2 + [arr[origin]] + arr_1
    return normalize(arr, len(arr_2))

def scale(arr, origin=0, ratio=1):
    new_origin = len(arr) // ratio
    if ratio > 1:
        arr_1 = arr[0:origin:ratio][::-1]
        arr_2 = arr[origin + ratio:len(arr):ratio]
        arr = arr_1 + [arr[origin]] + arr_2
        return normalize(arr, new_origin - 1)
    
def convolve(x, h, origin_X=0, origin_H=0):
    sizeX = len(x)
    sizeH = len(h)
    output = [0] * (sizeX + sizeH - 1)

    for i in range(sizeX):
        for j in range(sizeH):
            output[i + j] += x[i] * h[j]
    
    for i in range(sizeX):
        for j in range(sizeH):
            if (i + j) == (origin_X + origin_H):
                origin = i + j

    return normalize(output, origin)

    
# print(f"{normalize(arr, 4)}")
print(f"BEFORE: {x} || ORIGIN: #{originX}")

# flipped, originX = flip(x, 2)
# shifted, originX = shift(x, originX, 0)

# scaled = scale(arr, 4, 2)
# print(f"AFTER: {de_normalize(shifted)} || ORIGIN: #{originX}")

convolved_signal, originX = convolve(x, h, originX, 4)

print(f"OUTPUT: {de_normalize(convolved_signal, originX)} || ORIGIN: #{originX}")
point_arrow(de_normalize(convolved_signal, originX), originX)






