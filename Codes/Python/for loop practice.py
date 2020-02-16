for x in range(1,10):
    name=input('enter your name : ')
    em=eval(input('enter ur em : '))
    am=eval(input('enter ur am : '))
    total=(am+em)/2
    print('************************')
    print('hello ',name)
    print('Your total is : ',total)
    if total<50:
        print('you are pass')
    else:
        print('you are fail')
    print('************************')
    
