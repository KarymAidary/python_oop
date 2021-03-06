from element import Element


class BaseList:
    def __init__(self):
        self.first = None
        self.last = None

    def __getitem__(self, item):
        return self.get(item)

    def __repr__(self):
        return self.show()
        
    def __delitem__(self, item_index):
        self.remove(item_index) 

    def __replace_item__(self, item, power, coefficient):
        self.replace(item, power, coefficient)

    @property
    def list_lenght(self):
        lenght = "[]"
        if not self.first:
            return lenght
        else:
            counter = 0
            element = self.first
            while element != None:
                element = element.next
                counter += 1
            return counter

    def show():
        if not self.first:
            return '[]'
        else:
            string_start = "[({})".format(self.first)
            counter = 0
            element = self.first.next
            string_middle = ''
        while self.list_lenght != counter:
            string_middle += ", ({})".format(element)
            element = element.next
            counter += 1
        list_elements_string = string_start + string_middle + "]"
        return '{}'.format(list_elements_string)


    def replace(self, item, power, coefficient):
        previous_element = self.__getitem__(item - 1)
        current_element = previous_element.next
        new_element = Element(coefficient=coefficient, power=power, next=current_element.next)
        previous_element.next = new_element  
    
    def remove(self, item_index):
        element = self.__getitem__(item_index - 1)
        element_to_delete = element.next
        next_element = element_to_delete.next
        element.next = next_element

    def add(self, coefficient, power):
        new_element = Element(coefficient=coefficient, power=power, next=None)
        if not self.first:
            self.first = new_element
            self.last = self.first
        else:
            self.last.next = new_element
            self.last = new_element

    def get(self, item):
        if isinstance(item, int):
            if item == 0:
                return self.first
            elif item == -1:    
                return self.last
            else:
                element = self.first
                counter = 0
                while item !=counter:
                    counter += 1
                    element = element.next
                return element
