def soma(*args):
    total = 0
    for n in args:
        total += n
    return total

print(__name__)

if __name__ == '__main__': #Codigo rodado apenas se este for o modulo principal
    print(soma(5, 6, 4))