## Import random to choose teams ##
from random import  *

## Make list for append teams ##
list_of_teams_main = [
                    # 'Almería',
                    # 'Athletic',
                    # 'Atlético',
                    # 'Barcelona',
                    # 'Betis',
                    # 'Espanyol',
                    # 'Cádiz',
                    # 'Celta',
                    # 'Elche',
                    # 'Getafe',
                    # 'Girona',
                    # 'Mallorca',
                    # 'Osasuna',
                    # 'Rayo',
                    # 'Real Sociedad',
                    # 'Real MadridReal',
                    # 'Real ValladolidReal',
                    # 'Sevilla',
                    # 'Valencia',
                    # 'Villarreal'
                    ]


## Get number of your league teams ##
while True:
    try:
        number_of_teams = int(input("enter number of league team : "))
    except ValueError:
        print("You should give number")
        continue
    
    if number_of_teams < 3:
        print("You can't start your league with {} team".format(number_of_teams))

    elif number_of_teams >= 3:
        print("Your league have {} teams".format(number_of_teams))

        if number_of_teams % 2 != 0 :
            list_of_teams_main.append('Break')
        break
    


## Get name of your league teams ##
count = number_of_teams
while count:
    new_team = input("enter your team : ")

    if new_team.replace(' ', '') in list_of_teams_main:
        print('{} is exist in your team'.format(new_team))
        continue
    
    elif len(new_team.replace(' ', '')) == 0:
        print('None value is unvaluable')
        continue
    
    else:
        list_of_teams_main.append(new_team)

    count -= 1

## Make list for append random teams ##
list_of_selected_teams = []

sub_list_teams = list_of_teams_main.copy()

## Append random teams to list##
for team in range(len(list_of_teams_main)):
    selected_team = choice(sub_list_teams)
    sub_list_teams.remove(selected_team)
    list_of_selected_teams.append(selected_team)

## Devide teams to two list ##
sub_list_A= list_of_selected_teams[:int((len(list_of_selected_teams)/2))]
sub_list_B = list_of_selected_teams[int((len(list_of_selected_teams)/2)):]


number_of_all_match = ((len(list_of_teams_main))*((len(list_of_teams_main))-1))/2
weeks_number = (len(list_of_teams_main))-1
number_of_weeks_game = int((len(list_of_teams_main))/2)

for week in range(weeks_number):
    list_week = []
    for team in range(number_of_weeks_game):
        first_team = sub_list_A[team]
        second_team = sub_list_B[team]
        match = 'Match {} : {} VS {}'.format(team + 1, first_team, second_team)
        list_week.append(match)


    sub_list_A.append(sub_list_B[-1])
    del sub_list_B[-1]

    sub_list_B.insert(0,sub_list_A[1])
    del sub_list_A[1]
    
    print("Game Week {} :".format( week + 1))
    print(list_week)