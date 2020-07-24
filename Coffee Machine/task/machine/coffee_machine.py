
class Coffee:
    def __init__(self):
        self.curr_money = 550
        self.curr_water = 400
        self.curr_milk = 540
        self.curr_beans = 120
        self.curr_cups = 9
    def print_state(self):
        print('The coffee machine has:')
        print(str(self.curr_water) + ' of water')
        print(str(self.curr_milk) + ' of milk')
        print(str(self.curr_beans) + ' of coffee beans')
        print(str(self.curr_cups) + ' of disposable cups')
        print(str(self.curr_money) + ' of money')
    def take(self):
        print('I gave you $'+str(self.curr_money))
        self.curr_money = 0

    def fill(self):
        water_added = input('Write how many ml of water do you want to add:')
        water_added = int(water_added.lstrip(">"))
        self.curr_water += water_added
        milk_added = input('Write how many ml of milk do you want to add:')
        milk_added = int(milk_added.lstrip(">"))
        self.curr_milk += milk_added
        beans_added = input('Write how many grams of coffee beans do you want to add:')
        beans_added = int(beans_added.lstrip(">"))
        self.curr_beans += beans_added
        cups_added = input('Write how many disposable cups of coffee do you want to add:')
        cups_added = int(cups_added.lstrip(">"))
        self.curr_cups += cups_added

    def notenough_water(self):
        print('Sorry, not enough water!')
    def notenough_coffee(self):
        print('Sorry, not enough coffee beans!')
    def notenough_cups(self):
        print('Sorry, not enough cups!')
    def notenough_milk(self):
        print('Sorry, not enough milk!')


    def buy(self):
        num = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        if num == 'back':
            return
        num = int(num.lstrip(">"))
        if num == 1:
            if self.curr_water >= 250 and self.curr_beans >= 16 and self.curr_cups >= 1 :
                self.curr_water -= 250
                self.curr_cups -= 1
                self.curr_beans -= 16
                self.curr_money += 4
                print('I have enough resources, making you a coffee!')
            else:
                self.notenough_water()
        elif num == 2:
            if self.curr_water >= 350 and self.curr_milk >= 75 and self.curr_beans >= 20 and self.curr_cups >= 1:
                self.curr_water -= 350
                self.curr_milk -= 75
                self.curr_beans -= 20
                self.curr_cups -= 1
                self.curr_money += 7
                print('I have enough resources, making you a coffee!')
            else:
                self.notenough_water()
        else:
            if self.curr_water >= 200 and self.curr_milk >= 100 and self.curr_beans >= 12 and self.curr_cups >= 1:
                self.curr_water -= 200
                self.curr_milk -= 100
                self.curr_beans -= 12
                self.curr_cups -= 1
                self.curr_money += 6
                print('I have enough resources, making you a coffee!')
            else:
                self.notenough_water()

    def orderMachine(self):
        while True:
            action_type = input('Write action (buy, fill, take, remaining, exit):')
            action_type = str(action_type.lstrip(">"))
            if action_type == 'remaining':
                self.print_state()
            elif action_type == 'buy':
                self.buy()
            elif action_type == 'fill':
                self.fill()
            elif action_type == 'take':
                self.take()
            else:
                break

coffee_object = Coffee()
coffee_object.orderMachine()



















