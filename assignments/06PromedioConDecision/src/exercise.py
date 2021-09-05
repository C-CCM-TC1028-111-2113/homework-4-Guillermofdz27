def main():
    #escribe tu código abajo de esta línea
suma= 0
p= 0
y=float(input())
while y >0:
    suma= suma + float(y)
    p=p+1
    y= float(input())
if y<= 0:
    prom = suma/p
    print(str(prom))
    pass
if __name__=='__main__':
    main()
