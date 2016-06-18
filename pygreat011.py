# klasy


class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay *= (1.0 + percent)

# self to nowy obiekt
# atrybuty - state information
# zachowania - metody
# metody automatycznie otrzymają przetwarzaną instancję (self)
