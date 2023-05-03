from vehicles import Vehicles


class Car(Vehicles):

    def __init__(self, color, count_of_wheels, company, manufacturing_country):

        super().__init__(color, count_of_wheels)

        self._company = company
        self.manufacturing_country = manufacturing_country

    


