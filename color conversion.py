r = int(input("Enter r ranging from 0-255: ")) 
g = int(input("Enter g ranging from 0-255: "))
b = int(input("Enter b ranging from 0-255: "))
    # Enter red , green and brown color level ranging from 0 - 255
if r == 0 and b == 0 and g == 0:
    C = 0
    M = 0
    Y = 0
    K = 1
else:
    w = max((r / 255 , g / 255 , b / 255))
    C = abs(((w - r) / 255) / w)
    M = abs(((w - b) / 255) / w)
    Y = abs(((w - b) / 255) / w)
    K = abs(1 - w)
print("The CMYK values are " , C , M , Y , K)
