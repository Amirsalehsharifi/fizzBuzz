i= 0
list=[]

for i in range(1,100): 
    if i%3 ==0 and i%5 == 0:
        list.append("fizzBuzz")
    elif i%3 == 0:
        list.append("fizz")
    elif i% 5 == 0:
        list.append("Buzz")
    else:
        list.append(i)
    i +=1
print(list)
