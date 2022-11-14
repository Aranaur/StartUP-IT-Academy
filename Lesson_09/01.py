class FirstCar:
    def __init__(self, manufacturer, color, displ):
        self.manufacturer = manufacturer
        self.color = color
        self.displ = displ

    @staticmethod
    def move_forward():
        print('Move forward')

    @staticmethod
    def move_backward():
        print('Move backward')


class SecondCar(FirstCar):
    @staticmethod
    def turn_left():
        print('Turn left')

    @staticmethod
    def turn_right():
        print('Turn right')


car_1 = SecondCar(manufacturer='Toyota',
                  color='gray',
                  displ=4.7)
car_1.turn_left()
car_1.move_forward()
car_1.move_backward()
car_1.turn_right()
