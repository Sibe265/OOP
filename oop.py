class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists
    

class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

def enter_football_player():
    print("Enter football player s data.")
    f_name = input("Enter player s first name: ")
    l_name = input("Enter player s last name: ")
    height = input("Height: ")
    weight = input("Weight: ")
    goals = input("Number of goals: ")
    y_cards = input("Yellow cards: ")
    r_cards = input("Red cards: ")

    new_player = FootballPlayer(first_name=f_name, last_name=l_name, height_cm=height, weight_kg=weight, goals=goals, yellow_cards=y_cards, red_cards=r_cards)

    with open("football_players.json", "w") as football_file:
        football_file.write(str(new_player.__dict__))

    print("Player succesfully entered!")
    print("Player s data: {0}".format(new_player.__dict__))

def enter_basketball_player():
    print("Enter basketball player s data.")
    f_name = input("Enter player s first name: ")
    l_name = input("Enter player s last name: ")
    height = input("Height: ")
    weight = input("Weight: ")
    points = input("Number of points: ")
    rebounds = input("Rebounds: ")
    assists = input("Assists: ")

    new_player = BasketballPlayer(first_name=f_name, last_name=l_name, height_cm=height, weight_kg=weight, points=points, rebounds=rebounds, assists=assists)

    with open("basketball_players.json", "w") as basketball_file:
        basketball_file.write(str(new_player.__dict__))

    print("Player succesfully entered!")
    print("Player s data: {0}".format(new_player.__dict__))
        

choice = input("Football (A) or basketball (B)?")

if choice.upper() == "A":
    enter_football_player()
elif choice.upper() == "B":
    enter_basketball_player()
else:
    print("Wrong entry!")