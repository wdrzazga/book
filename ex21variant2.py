ascending =True
previous = -(10 ** 100)

for i in range(5):
    n = int(input("number " + str(i+1)) +" ")
    if n <= previous:
        ascending = False
        break

msg = " NOT " if ascending else ""
print("array is " + msg +"ascending.")
