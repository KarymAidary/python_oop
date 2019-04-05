from baselist import BaseList


class Element:
    def __init__(self, number, next=None):
        self.number = number
        self.next = next

    def __repr__(self):
        return str(self.number)

class Count(BaseList):
    def __len__(self):
        lenght = "[]"
        if not self.first:
            return lenght
        else:
            lenght = 0
            element = self.first
            while element.next != self.first:  
                element = element.next
                lenght += 1
            return lenght           

    def add(self, number):
        new_child = Element(number=number, next=None)
        if not self.first:
            self.first = new_child
            self.last = self.first
        else:
            self.last.next = new_child
            self.last = new_child
            self.last.next = self.first  
                               

if __name__ == "__main__":
    counter = Count()  
    count = 1
    
    while count < 6: 
        counter.add(count)
        count += 1


    


    # while counter.list_lenght != '[]':
    counter.remove(5)
              
    print(counter)