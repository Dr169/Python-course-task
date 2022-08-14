## Import random to choose teams ##
from random import  *

class ScheduleLeague:
    def __init__(self, list_of_teams):
        self.list_of_teams = list_of_teams

    def random_teams(self, list_of_teams_main):
        ## Make list for append random teams ##
        list_of_selected_teams = []

        sub_list_teams = list_of_teams_main.copy()


        ## Append random teams to list ##
        for team in range(len(list_of_teams_main)):
            selected_team = choice(sub_list_teams)
            sub_list_teams.remove(selected_team)
            list_of_selected_teams.append(selected_team)

        ## Devide teams to two sub list ##
        sub_list_A = list_of_selected_teams[:int((len(list_of_selected_teams)/2))]
        sub_list_B = list_of_selected_teams[int((len(list_of_selected_teams)/2)):]

        return sub_list_A, sub_list_B


    def games_specifications(self, list_of_teams_main):
        weeks_number = (len(list_of_teams_main))-1
        number_of_weeks_game = int((len(list_of_teams_main))/2)

        return weeks_number, number_of_weeks_game


    def show_schedule(self, sub_list_A, sub_list_B, weeks_number, number_of_weeks_game):
        dict_of_matchs = {}
        for week in range(weeks_number):
            list_weeks_game = []
            for team in range(number_of_weeks_game):
                first_team = sub_list_A[team]
                second_team = sub_list_B[team]
                match = 'Match {} : {} VS {}'.format(team + 1, first_team, second_team)
                list_weeks_game.append(match)

            sub_list_A.append(sub_list_B[-1])
            del sub_list_B[-1]

            sub_list_B.insert(0,sub_list_A[1])
            del sub_list_A[1]
            dict_of_matchs["Games of Week {}".format( week + 1)] = list_weeks_game
        
        return dict_of_matchs


    def schedule(self):
        # list_of_teams, number_of_teams = get_list_of_teams()
        # list_of_teams_main = get_teams_name(list_of_teams, number_of_teams)

        if len(self.list_of_teams) < 3:
            print("You can't start your league with {} team. You need more than 2 teams.".format(len(self.list_of_teams))) 
            return

        for team_name in self.list_of_teams:
            if type(team_name) != str:
                print("Your teams name must be a  <class 'string'> not {}.".format(type(team_name)))
                return

            if self.list_of_teams.count(team_name.replace(" ","")) > 1:
                print("There are more than one team with name '{}' in the team list.".format(team_name))
                return

            if len(team_name.replace(' ', '')) == 0:
                print('There are none value in team list.')
                return

        if len(self.list_of_teams) >= 3:
            print("Your league have {} teams.".format(len(self.list_of_teams)))

        if len(self.list_of_teams) % 2 != 0 :
                self.list_of_teams.append('Break')

        sub_list_A, sub_list_B = self.random_teams(self.list_of_teams)

        weeks_number, number_of_weeks_game = self.games_specifications(self.list_of_teams)

        matchs = self.show_schedule(sub_list_A, sub_list_B, weeks_number, number_of_weeks_game)

        return matchs


    # def get_list_of_teams():
    #     ## Make list for append teams ##
    #     list_of_teams_main = [# 'Almería',# 'Athletic',# 'Atlético',# 'Barcelona',# 'Betis',# 'Espanyol',# 'Cádiz',# 'Celta',# 'Elche',
    #                         # 'Getafe',# 'Girona',# 'Mallorca',# 'Osasuna',# 'Rayo',# 'Real Sociedad',# 'Real MadridReal',# 'Real ValladolidReal',
    #                         # 'Sevilla',# 'Valencia',# 'Villarreal'
    #                         ]

    #     ## Get number of your league teams ##
    #     while True:
    #         try:
    #             number_of_teams = int(input("enter number of league team : "))
    #         except ValueError:
    #             print("You should give number.")
    #             continue
            
    #         if number_of_teams < 3:
    #             print("You can't start your league with {} team.".format(number_of_teams))

    #         elif number_of_teams >= 3:
    #             print("Your league have {} teams.".format(number_of_teams))

    #             if number_of_teams % 2 != 0 :
    #                 list_of_teams_main.append('Break')
    #             break
        
    #     return list_of_teams_main, number_of_teams

        
    # def get_teams_name(list_of_teams_main, number_of_teams):  
    #     ## Get name of your league teams ##
    #     count = number_of_teams
    #     while count:
    #         new_team = input("enter your team name : ")

    #         if new_team.replace(' ', '') in list_of_teams_main:
    #             print('{} is exist in your team'.format(new_team))
    #             continue
            
    #         elif len(new_team.replace(' ', '')) == 0:
    #             print('None value is unvaluable')
    #             continue
            
    #         else:
    #             list_of_teams_main.append(new_team)

    #         count -= 1
        
    #     return list_of_teams_main