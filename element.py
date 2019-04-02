class Element:

    def __init__(self, coefficient=1, power=1, next=None):
        self.coefficient = coefficient
        self.power = power
        self.next = next

    def __repr__(self):
        return '%s, %s' % (self.coefficient, self.power)

    def get_coefficient(self):
        return self.coefficient

    def set_coefficient(self, coefficient):
        self.coefficient = coefficient

    def get_power(self):
        return self.power

    def set_power(self, power):
        self.power = power