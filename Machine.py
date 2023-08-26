class WaterTank:
    def __init__(self):
        self.capacity = 2.00
        self.level = 0.00
        self.minimum = 0.2
    
    def fill_water(self, amount):
        if amount + self.capacity > self.capacity:
            print('Overfill!')
            self.level = self.capacity
    
    def take_water(self, amount = 1):
        if self.check_water() is True:
            self.level -= 0.2 * amount
    
    def check_water(self):
        if self.level - self.minimum > self.minimum:
            return True
        else:
            return False
    
    def show_water(self):
        print('Water tank level: ', self.level)
        if self.level < self.minimum:
            print('Insufficient water!')
    
    def clear_water(self):
        self.level = 0

class DregDrawer():
    def __init__(self):
        self.capacity = 10
        self.level = 0
    
    def fill_drawer(self):
        self.level += 1
    
    def check_drawer(self):
        if self.level < self.capacity:
            return True
        else:
            return False
    
    def show_drawer(self):
        print('Dreg drawer level: ', self.level)
        if self.level == self.capacity:
            print('Dreg drawer is full!')

class CoffeeTank:
    def __init__(self):
        self.capacity = 1
        self.level = 0
    
    def fill_coffee(self):
        self.level = self.capacity
    
    def show_coffee(self):
        print('Coffee level: ', self.level)
        if self.level == 0:
            print('Insufficient coffee!')
    
    def check_coffe(self):
        if self.level == 0:
            return False
        else:
            return True
    
    def make_powder(self, portion):
        if portion == 1:
            self.level -= 0.1
        elif portion == 2:
            self.level -= 0.2

class Machine:
    def __init__(self):
        self.water_tank = WaterTank()
        self.dreg_drawer = DregDrawer()
        self.coffee_tank = CoffeeTank()
    
    def make_one_portion(self):
        if self.coffee_tank.check_coffe() is False:
            print('\nInsuficient coffee\n')
            return
        if self.water_tank.check_water() is False:
            print('\nInsuficient water\n')
            return
        if self.dreg_drawer.check_drawer() is False:
            print('\nDreg drawer is full\n')
            return
        self.coffee_tank.make_powder(1)
        self.water_tank.take_water()
        self.dreg_drawer.fill_drawer()
        print('One coffee is ready! Have a nivce day')

coffee_machine = Machine()

def start():
    coffee_machine.make_one_portion()

def fill_water():
    coffee_machine.water_tank.fill_water(2)

def fill_coffee():
    coffee_machine.coffee_tank.fill_coffee()

def check_status():
    coffee_machine.coffee_tank.show_coffee()
    coffee_machine.water_tank.show_water()
    coffee_machine.dreg_drawer.show_drawer()
    if (
        coffee_machine.coffee_tank.check_coffe() is True
        and coffee_machine.water_tank.check_water() is True
        and coffee_machine.dreg_drawer.check_drawer() is True
        ):
        print('Machine is ready for coffee =)')

def command(user_choice = 0):
    check_status()
    if user_choice == 1:
        start()
        command()
    elif user_choice == 2:
        fill_water()
        command()
    elif user_choice == 3:
        fill_coffee()
        command()
    elif user_choice == 4:
        check_status()
        command()
    else:
        command(
            int(
                input(
                    '1 - Make One Coffee\n'
                    '2 - Fill water\n'
                    '3 - Fill coffee\n'
                    '4 - Check status\n\n'
                )
            )
        )

if __name__ == '__main__':
    command()