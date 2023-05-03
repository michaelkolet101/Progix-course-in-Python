
class Score:

    def __init__(self, path_to_file):
        self.path = path_to_file

        
    def get_score(self):

        f = open(self.path, "r")

        my_score = f.read()

        f.close()

        return int(my_score)


    def set_score(self, new_score):

        f = open(self.path, "w")

        f.write(str(new_score))

        f.close()


class Car:

    def __init__(self, size, price, color, company, speed):
        self.my_size = size
        self.my_price = price
        self.my_color = color
        self.my_company = company
        self.my_speed = speed

    
    def get_size(self):
        return self.my_size
    
    def set_size(self, new_size):
        self.my_size = new_size

    def get_price(self):
        pass

    def set_price(self, new_price):
        pass




def max_imp(num1, num2):

    if num1 > num2:
        return num1
    
    return num2


def len_imp(my_list):
    
    counter = 0

    for itm in my_list:
        counter += 1

    return counter