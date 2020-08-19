def circle_area(x):
    num = x * x * 3.14
    return num
def circle_circum(n):
    num = n * 2 * 3.14
    return num
n = int(input("Number?"))
t = circle_area(n)
a = circle_circum(n)
print("面積:",t)
print("周長:",a)
