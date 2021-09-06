def main():
    #escribe tu código abajo de esta línea
    x=int(input())
    w= x + ((0-x)+1)
    while x +1 != w:
        if w%2 != 0:
            print(str(w)+"-"+"#")
        elif w%2== 0:
            print(str(w)+"-"+"%")
        w= w+ 1

    pass

if __name__=='__main__':   
    main()
