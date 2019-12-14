if __name__ == '__main__':
    i = int(input("i:="))
    n = int(input("n:="))
    result = [i*(n-t)*10**(t) for t in range(n)]
    s = sum(result)
    print(s)








