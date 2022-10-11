import random 
print("Welcome to the Team Allocator")

while True:
 

    players= ["Ayesha", "Reem", "Nour","Anthony", "Farah","Warda", "Fatimah", "Malak", "Misbah", "Ayna", "Natasha","Hoor" ]


    random.shuffle(players)

    team1= players[0:len(players)//2]

    captain1= random.choice(team1)
    print("Team 1 captain= " + captain1 + "\n")

    print("Team 1:")
    for player in team1:
        print(player)

    team2= players[len(players)//2:]
    print("\n Team 2 captain: "+ random.choice(team2))

    print(team2)
    for player in team2:
        print(player)

    response= input("Would you like to pick teams again? Type 'y' for yes and 'n' for no \n ")
    if response == "n":
        break

    

