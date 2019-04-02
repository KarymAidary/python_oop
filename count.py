from baselist import BaseList


class Element:
    def __init__(self, number, next=None):
        self.number = number
        self.next = next

    def __repr__(self):
        return str(self.number)

class Count(BaseList):
    def __len__(self):
        lenght = 0
        if not self.first:
            return lenght
        else:
            lenght = 1
            element = self.first
            while element.next != self.first:  
                element = element.next
                lenght += 1
            return lenght 

    def __delitem__(self, item_index):
        previus_el = self.__getitem__(item_index - 1)
        el_to_del = previus_el.next
        next_el = el_to_del.next
        previus_el.next = next_el


    # def remove(self, item_index):
    #     super().__delitem__(item_index)           

    @property
    def list_lenght(self):
        return self.__len__()

    def add(self, number):
        new_child = Element(number=number, next=None)
        if not self.first:
            self.first = new_child
            self.last = self.first
        else:
            self.last.next = new_child
            self.last = new_child
            self.last.next = self.first

    def get_element(self, item):
        return super().__getitem__(item)    





if __name__ == "__main__":
    counter = Count()  
    count = 1
    
    while count < 30: 
        counter.add(count)
        count += 1



    count = 0
    while count <= 64:
        count += 1
        counter.__delitem__(3)
        if counter.list_lenght == 2:
            break
              
    print(counter)