def list_numbers():
    i = 1
    while i <= 100:
        print(i)
        i+=1 #i = i + 1

    print("i:", i) #101

def list_numbers2():
    i = 1
    status = True
    while status: #while status == True
        if i == 11:
            break 
        print(i)
        i+=1 #i = i + 1

    print("i:", i) #101

def list_numbers3():
    i = 1
    status = True
    while status: 
        print(i)
        i+=1 
        if i > 10 : 
            status = False

    print("i:", i) #11

def list_numbers4():
    i = 1
    status = False
    while not status: 
        print(i)
        i+=1 
        if i > 10 : 
            status = True

    print("i:", i) 


#ist_numbers2()
#list_numbers3()
list_numbers4()    
