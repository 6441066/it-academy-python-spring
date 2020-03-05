def cut_kusok_area(n, m, k):
    """Долька площадью k за один разлом

    Вернет True, если можно одним разломом отделить
    от шоколадки кусок площадью ровно k
    Площадь k и разлом это кратные длине и(или) ширине величины
    поэтому проверяем кратность k хотя бы одной из сторон.
    И площадь k должна быть < площади шоколадки ( n * m )
    """

    if (k % n == 0 or k % m == 0) and k < n * m:
        return True
    return False


def cut_dolek(n, m, k):
    """Ровно k долек

    Вернет True, если можно отломить от шоколадки ровно
    k долек за некоторое количество разломов.
    Необходимо рассмотреть крайние случаи:
    1. Один кусочек не отломать ни как, если 1*1 или 2*2 !
    2. Последний кусучек также надо учитывыть при разломе!
    Он всегда даст пару в случае, если k = n * m - 1
    """
    if n == 1 and m == 1 or k == 1 and n == 2 and m == 2 or k == n * m - 1:
        return False
    return True


def cut_dolek_razlomov(n, m, k, t):
    """Ровно k долек за t разломов

    Вернет True, если можно отломить от шоколадки ровно
    k долек с помощью t разломов
    Сначала проверим не попадаем ли мы под крайние случаи.
    """
    if cut_dolek(n, m, k):
        tt = t
        kk = 0
        while tt>0 :
            for i in range(n+1,1,-1):
                for j in range(m+1,1,-1):
                    if cut_kusok_area(n, m, i*j):
                         tt -= 1
                         k = k + i*j
                         if not cut_dolek_razlomov(i, j, kk, tt):
                            if kk==k and tt==0:
                                return True
                    elif kk==k and tt==0:
                        return True
    if kk==k and tt==0:
        return True
    return False


print(cut_kusok_area(5, 8, 10))
print(cut_kusok_area(5, 8, 10))
print(cut_kusok_area(5, 8, 28))
print()
print(cut_dolek(5, 8, 39))
print(cut_dolek(3, 3, 5))
print()
print(cut_dolek_razlomov(5, 8, 0, 0))
print(cut_dolek_razlomov(5, 8, 40, 1))
