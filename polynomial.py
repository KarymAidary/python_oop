from baselist import BaseList


class Polynomial(BaseList):
    
    def sum_polynomial(self, polynomial1, polynomial2):   
        pass

    def meaning(self, symbol, polynomial):
        if isinstance(polynomial, List) and isinstance(symbol, int):
            counter = 0
            polynomial_total = 0
            while polynomial.list_lenght != counter: 
                counter += 1
                member = polynomial.get_element(counter).coefficient * symbol ** polynomial.get_element(counter).power 
                polynomial_total += member 
        else:
            polynomial_total = "is not instance"
        return polynomial_total         

    def add(self, coefficient, power):
        BaseList.add(self, coefficient, power)      
                    

    def equality(self, polynomial1, polynomial2):
        if isinstance(polynomial1, BaseList) and isinstance(polynomial2, BaseList):
            if self.meaning(3, polynomial1) == self.meaning(3, polynomial2):
                print("equality")
            else:
                print("Not equality")  
        else:
            print("is not instance")                


if __name__ == "__main__":
    polynomial = Polynomial()
    p = Polynomial()
    q = Polynomial()
    p.add(7, 4) #coefficient, power
    p.add(3, 2)
    p.add(1, 1)
    p.add(2, 0)
    q = Polynomial()
    q.add(-2, 5)
    q.add(2, 3)
    q.add(1, 1)
    q.add(-6, 0)

    print(q)