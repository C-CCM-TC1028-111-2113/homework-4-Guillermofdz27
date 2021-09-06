
def main():
    #escribe tu código abajo de esta línea
    w=int(input())
    x1,x2= 0,1
    v= 0
    while v<w:
        n= x1+x2
        x1=x2
        x2=n
        v+=1
    n-=x2-x1
    print(n)

    pass

if __name__=='__main__':
    main()
