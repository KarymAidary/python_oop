from element import Element


class BaseList:

    def __init__(self):
        self.first = None
        self.last = None

    def __getitem__(self, item):
        if isinstance(item, int):
            if item == 1:
                return self.first
            else:
                element = self.first
                counter = 1
                while item:
                    counter += 1
                    element = element.next
                    if counter != item:
                        continue
                    else:
                        return element

    def __call__(self, *args, **kwargs):
        if not self.first:
            return '[]'
        else:
            string_start = "[({})".format(self.first)
            counter = 1
            element = self.first.next
            string_middle = ''
        while self.list_lenght != counter:
            string_middle += ", ({})".format(element)
            element = element.next
            counter += 1
        list_elements_string = string_start + string_middle + "]"
        return '{}'.format(list_elements_string)

    def __repr__(self):
        return self.__call__()

    def __len__(self):
        lenght = 0
        if not self.first:
            return lenght
        else:
            counter = 0
            element = self.first
            while element != None:
                element = element.next
                counter += 1
            return counter

    def __delitem__(self, item):
        element = self.__getitem__(item - 1)
        element_to_delete = element.next
        next_element = element_to_delete.next
        element.next = next_element

    def __replace_item__(self, item, power, coefficient):
        previous_element = self.__getitem__(item - 1)
        current_element = previous_element.next
        new_element = Element(coefficient=coefficient, power=power, next=current_element.next)
        previous_element.next = new_element    

    @property
    def list_lenght(self):
        return self.__len__()

    def replace(self, item, power, coefficient):
        self.__replace_item__(item, power, coefficient)
    
    def remove(self, item):
        self.__delitem__(item=item)
        return 'Successfully delete!'

    def add(self, coefficient, power):
        new_element = Element(coefficient=coefficient, power=power, next=None)
        if not self.first:
            self.first = new_element
            self.last = self.first
        else:
            self.last.next = new_element
            self.last = new_element

    def get_element(self, item):
        return self.__getitem__(item)
