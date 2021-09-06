
def main():
    #Escribe tu código debajo de esta línea
    y= "*"
    d= int(input("Enter triangle height: "))
    x= d+1
    w= x+ ((0-x)+1)

    while x != w and x!= 0:
        u= d-w
        print(u*(" ")+y)
        y= "*"+str(y)
        w=w+1
    
    pass


if __name__=='__main__':
    main()
