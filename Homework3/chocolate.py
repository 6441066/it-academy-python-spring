class chocolade:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def cut_kusok_area(self, k):
        """ Вернет True, если можно одним разломом отделить
            от шоколадки кусок площадью ровно k

            Площадь k и разлом это кратные длине и(или) ширине величины
            поэтому проверяем кратность k хотя бы одной из сторон"""
        if k % self.n == 0 or k % self.m == 0:
            return True
        return False

    def cut_dolek(self, k):
        """Вернет True, если можно отломить от шоколадки РОВНО
           k долек за некоторое количество разломов."""
        if k <= self.n * self.m:
            return True
        return False
    def cut_dolek_razlomov(self, k, t):
        """ Вернет True, если можно отломить от шоколадки ровно
           k долек с помощью t разломов"""
      pass

    def __str__(self):
        return "Это моя шоколадка шириной {} долек и длинной {} долек".format(self.n, self.m)


my_chocolate = chocolade(5, 8)
print(my_chocolate)
print(my_chocolate.cut_kusok_area)