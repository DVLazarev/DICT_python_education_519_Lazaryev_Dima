def input_m():
    measurement = input("Введите кол-во строк и столбов: ").split()
    n, m = measurement
    mx = []
    for y in range(int(n)):
        mx.append(input().split())
    return mx


def sum_mat():
    mtx = input_m()
    mtx_2 = input_m()
    if len(mtx) == len(mtx_2) and len(mtx[0]) == len(mtx_2[0]):
        for i in range(len(mtx)):
            for x in range(len(mtx[0])):
                print(int(mtx[i][x]) + int(mtx_2[i][x]), end=' ')
            print('')
    else:
        print("ERROR")


def multiplication():
    mtx = input_m()
    const = input("Введите константу: ")
    for i in range(len(mtx)):
        for x in range(len(mtx[0])):
            print(int(mtx[i][x]) * int(const), end=' ')
        print('')


multiplication()
