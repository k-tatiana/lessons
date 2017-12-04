# Реализовать функционал работы с работниками.
# Работнику можно задавать ФИО, возраст (от 20 до 80), а так же умения (их может быть несколько;
# задаются как по одному так и списком; можно удалять умения по 1 или по несколько).
# Есть работники 2х видов с почасовой оплатой и с фиксированной.
# Для работников с почасовой оплатой метод считающий зарплату возвращает 300*(кол-во часов),
# для работников с фиксированной зарплатой просто получаемую ими зарплату.

class AgeException(Exception):
    pass

class Worker:
    def __init__(self, FIO, age, abilities):
        self.fio = FIO
        self.age = age
        self.ability = abilities

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        if age <= 80 and age >= 20:
            self._age = age
        else:
            raise AgeException

    def __str__(self):
        return 'FIO - %s, age - %s,  abilities - %s' % (self.fio, self.age, self.ability)

w = Worker('Котик', 22, ('Красота','Ухоженность','Вышивать умеет'))

print(w)

class WorkerWithSalary(Worker):
    def __init__(self, fio, age, abilities, hour):
        super().__init__(fio,age, abilities)
        self.hour = hour

    @property
    def salary(self):
        return self.hour * 300

    def __str__(self):
        return '''Имя ему - %s, живет он в мире %s лет, обладает такими качествами как %s, и при всем при этом зарабатывает
         %s тугриков''' % (self.fio, self.age, self.ability, self.salary)

s = WorkerWithSalary('Василий', 20, ('Доброта','Волосатость'), 25)
print(s)

class WorkerFixPayment(Worker):
    def __init__(self, fio, age, abilities, salary):
        super().__init__(fio,age,abilities)
        self.salary = salary

    def __str__(self):
        return '''А это просто %s, которому %s лет, он хорошо %s, вкалывыает за %s тугриков''' % \
               (self.fio, self.age, self.ability, self.salary)


AnotherGreatWorker = WorkerFixPayment('Федя',30, ('Рисовать умеет'), 2400)

print(AnotherGreatWorker)

########################################################################################################################
#Реализовать декоратор который считает время работы функции и печатающей это время после завершения функции

import timeit
def function_time_calq_decorator(function_to_decorate):
    function_to_decorate()
    return(timeit.timeit("function_to_decorate()", setup="from __main__ import function_to_decorate", number=1))

@function_time_calq_decorator
def _start(number):
    for i in range (number*100):
        yield i
    print('ha-haa!')

gen = _start(20)







