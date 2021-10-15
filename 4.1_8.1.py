def spisok(n): #n - количество отрезков
    lst = []
    for i in range(n):
        a, b = input().split()
        lst.append([int(a), int(b)])
        print(lst, 'spisok')
    lst = sorted(lst, key = lambda x: x[1])
    return(lst)

"""
Возьмём все точки-концы отрезков (как левые, так и правые) и отсортируем их. При этом для каждой точки
сохраним вместе с ней номер отрезка, а также то, каким концом его она является (левым или правым). Кроме
того, отсортируем точки таким образом, что, если есть несколько точек с одной координатой, то сначала
будут идти левые концы, и только потом - правые. Заведём стек, в котором будут храниться номера
отрезков, рассматриваемых в данный момент; изначально стек пуст. Будем двигаться по точкам в
отсортированном порядке. Если текущая точка - левый конец, то просто добавляем номер её отрезка в стек.
Если же она является правым концом, то проверяем, не был ли покрыт этот отрезок (для этого можно просто
завести массив булевых переменных). Если он уже был покрыт, то ничего не делаем и переходим к следующей
точке (забегая вперёд, мы утверждаем, что в этом случае в стеке текущего отрезка уже нет). Если же он
ещё не был покрыт, то мы добавляем текущую точку в ответ, и теперь мы хотим отметить для всех текущих
отрезков, что они становятся покрытыми. Поскольку в стеке как раз хранятся номера непокрытых ещё отрезков,
то будем доставать из стека по одному отрезку и отмечать, что он уже покрыт, пока стек полностью не
опустеет. По окончании работы алгоритма все отрезки будут покрыты, и притом наименьшим числом точек
(повторимся, здесь важно требование, что при равенстве координат сначала идут левые концы, и только
затем правые).
"""

"""
def sortirovka(n):
    lst = []
    r1 = [[5, 6], [4, 7], [3, 8], [2, 9], [1, 10]]
    #r1 = spisok(n)
    print(r1, lst, 'Begin', sep=' - ')
    for i in r1:
        print(i, 'i', sep=' - ')
        lst.append(i[1])
        print(r1, lst, 'first', sep=' - ')
        for y in r1:
            print(y, 'y', sep=' - ')
            if y[0] <= i[1] and y[1] >= i[1]:
                r1.remove(y)
                print(r1, lst, 'second', sep=' - ')
    print()
    return(print(r1, lst, sep=' - '))
"""

def sortirovka(n):
    lst = []
    r1 = [[5, 6], [4, 7], [3, 8], [2, 9], [1, 10]]
    #r1 = spisok(n)
    print(r1, lst, 'Begin', sep=' - ')
    for i in r1:
        print(i, 'i', sep=' - ')
        lst.append(i[1])
        print(r1, lst, 'first', sep=' - ')
        for y in r1:
            print(y, 'y', sep=' - ')
            if y[0] <= i[1] and y[1] >= i[1]:
                r1.remove(y)
                print(r1, lst, 'second', sep=' - ')
    print()
    return(print(r1, lst, sep=' - '))


def main():
    n = 1 #int(input())
    sortirovka(n)


if __name__ == "__main__":
    main()
