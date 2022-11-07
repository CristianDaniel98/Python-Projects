
if __name__ == '__main__':
    machine = {
        "Water": 300,
        "Milk": 200,
        "Caffe": 100,
        "Money": 0,
        "espresso": {"Water": 50,
                     "Caffe": 18,
                     "Money": 1.50},
        "latte": {"Water": 200,
                  "Milk": 150,
                  "Caffe": 24,
                  "Money": 2.50},
        "cappuccino": {"Water": 250,
                       "Milk": 100,
                       "Caffe": 24,
                       "Money": 3.00}
    }

    flag = bool(1)
    username = "admin"
    password = "qwe123"

    while flag:
        quarters = 0
        dimes = 0
        nickles = 0
        pennies = 5
        user_input = input("What would you like? (espresso/latte/cappuccino): ")

        if user_input == username:
            tries_remain = 5
            while tries_remain > 0:
                input_password = input("Enter password: ")
                if input_password == password:
                    inner_flag = bool(1)
                    while inner_flag:
                        tries_remain = 0
                        user_input = input("Welcome to the Admin interface. Choose a option: ")
                        if user_input == "report":
                            print("Water: " + str(machine["Water"]))
                            print("Milk: " + str(machine["Milk"]))
                            print("Caffe: " + str(machine["Caffe"]))
                            print("Money: " + str(machine["Money"]))

                        if user_input == "water":
                            water = int(input("How many water do you want to insert?: "))
                            machine["Water"] = machine["Water"] + water

                        if user_input == "milk":
                            milk = int(input("How many milk do you want to insert?: "))
                            machine["Milk"] = machine["Milk"] + milk

                        if user_input == "caffe":
                            caffe = int(input("How many caffe do you want to insert?: "))
                            machine["Caffe"] = machine["Caffe"] + caffe

                        if user_input == "logout":
                            inner_flag = bool(0)

                        if user_input == "off":
                            inner_flag = bool(0)
                            flag = bool(0)
                else:
                    tries_remain -= 1
                    print("Invalid password! You have " + str(tries_remain) + " tries remains!")

        if user_input == "espresso":
            print("Espresso price: $1.5")
            if machine["Water"] < machine["espresso"]["Water"]:
                print("Not enough water for espresso!")
            elif machine["Caffe"] < machine["espresso"]["Caffe"]:
                print("Not enough caffe for espresso!")
            else:
                print("Please insert coins.")
                quarters = float(input("How many quarters?($0.25): "))
                dimes = float(input("How many dimes?($0.10): "))
                nickles = float(input("How many nickles?($0.05): "))
                pennies = float(input("How many pennies?($0.01): "))
                total_input = 0.25*quarters + 0.10*dimes + 0.05*nickles + 0.01*pennies
                if total_input < machine["espresso"]["Money"]:
                    print("Sorry that's not enough money. Money refund!")
                else:
                    total_input = total_input - machine["espresso"]["Money"]
                    total_input = float("{:.2f}".format(total_input))
                    print("Here is $" + str(total_input) + " in charge!")
                    machine["Money"] = machine["Money"] + machine["espresso"]["Money"]
                    machine["Water"] = machine["Water"] - machine["espresso"]["Water"]
                    machine["Caffe"] = machine["Caffe"] - machine["espresso"]["Caffe"]

        if user_input == "latte":
            print("Latte price: $2.5")
            if machine["Water"] < machine["latte"]["Water"]:
                print("Not enough water for latte!")
            elif machine["Caffe"] < machine["latte"]["Caffe"]:
                print("Not enough caffe for latte!")
            elif machine["Milk"] < machine["latte"]["Milk"]:
                print("Not enough milk for latte")
            else:
                print("Please insert coins.")
                quarters = float(input("How many quarters?($0.25): "))
                dimes = float(input("How many dimes?($0.10): "))
                nickles = float(input("How many nickles?($0.05): "))
                pennies = float(input("How many pennies?($0.01): "))
                total_input = 0.25*quarters + 0.10*dimes + 0.05*nickles + 0.01*pennies
                if total_input < machine["latte"]["Money"]:
                    print("Sorry that's not enough money. Money refund!")
                else:
                    total_input = total_input - machine["latte"]["Money"]
                    total_input = float("{:.2f}".format(total_input))
                    print("Here is $" + str(total_input) + " in charge!")
                    machine["Money"] = machine["Money"] + machine["latte"]["Money"]
                    machine["Water"] = machine["Water"] - machine["latte"]["Water"]
                    machine["Caffe"] = machine["Caffe"] - machine["latte"]["Caffe"]
                    machine["Milk"] = machine["Milk"] - machine["latte"]["Milk"]

        if user_input == "cappuccino":
            print("Cappuccino price: $3")
            if machine["Water"] < machine["cappuccino"]["Water"]:
                print("Not enough water for cappuccino!")
            elif machine["Caffe"] < machine["cappuccino"]["Caffe"]:
                print("Not enough caffe for cappuccino!")
            elif machine["Milk"] < machine["cappuccino"]["Milk"]:
                print("Not enough milk for cappuccino")
            else:
                print("Please insert coins.")
                quarters = float(input("How many quarters?($0.25): "))
                dimes = float(input("How many dimes?($0.10): "))
                nickles = float(input("How many nickles?($0.05): "))
                pennies = float(input("How many pennies?($0.01): "))
                total_input = 0.25*quarters + 0.10*dimes + 0.05*nickles + 0.01*pennies
                if total_input < machine["latte"]["Money"]:
                    print("Sorry that's not enough money. Money refund!")
                else:
                    total_input = total_input - machine["cappuccino"]["Money"]
                    total_input = float("{:.2f}".format(total_input))
                    print("Here is $" + str(total_input) + " in charge!")
                    machine["Money"] = machine["Money"] + machine["cappuccino"]["Money"]
                    machine["Water"] = machine["Water"] - machine["cappuccino"]["Water"]
                    machine["Caffe"] = machine["Caffe"] - machine["cappuccino"]["Caffe"]
                    machine["Milk"] = machine["Milk"] - machine["cappuccino"]["Milk"]
