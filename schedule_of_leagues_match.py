## Import random to choose teams ##
from random import  *

class Schedule_league:
    def random_teams(self, list_of_teams_main):
        ## Make list for append random teams ##
        list_of_selected_teams = []

        sub_list_teams = list_of_teams_main.copy()

        ## Append random teams to list##
        for team in range(len(list_of_teams_main)):
            selected_team = choice(sub_list_teams)
            sub_list_teams.remove(selected_team)
            list_of_selected_teams.append(selected_team)

        ## Devide teams to two list ##
        sub_list_A = list_of_selected_teams[:int((len(list_of_selected_teams)/2))]
        sub_list_B = list_of_selected_teams[int((len(list_of_selected_teams)/2)):]

        return sub_list_A, sub_list_B


    def games_specifications(self, list_of_teams_main):
        number_of_all_match = ((len(list_of_teams_main))*((len(list_of_teams_main))-1))/2
        weeks_number = (len(list_of_teams_main))-1
        number_of_weeks_game = int((len(list_of_teams_main))/2)

        return weeks_number, number_of_weeks_game


    def show_schedule(self, list_1, list_2, weeks_number, number_of_weeks_game):
        dict_of_matchs = {}
        for week in range(weeks_number):
            list_weeks_game = []
            for team in range(number_of_weeks_game):
                first_team = list_1[team]
                second_team = list_2[team]
                match = 'Match {} : {} VS {}'.format(team + 1, first_team, second_team)
                list_weeks_game.append(match)

            list_1.append(list_2[-1])
            del list_2[-1]

            list_2.insert(0,list_1[1])
            del list_1[1]
            dict_of_matchs["Games of Week {}".format( week + 1)] = list_weeks_game
        
        return dict_of_matchs


    def schedule(self, list = ["team_a","team_b","team_c","team_d","team_e","team_f","team_g","team_h","team_i","team_j"]):
        # list, number_of_teams = get_list_of_teams()
        # list_of_teams_main = get_teams_name(list, number_of_teams)

        if len(list) < 3:
            return print("You can't start your league with {} team.".format(len(list))) 

        for team_name in list:
            if type(team_name) != str:
                return print("Your teams name must be a  <class 'string'> not {}.".format(type(team_name)))

            if list.count(team_name.replace(" ","")) > 1:
                return print("There are more than one team with name '{}' in the team list.".format(team_name))
            
            if len(team_name.replace(' ', '')) == 0:
                return print('There are none value in team list.')

        if len(list) >= 3:
            print("Your league have {} teams.".format(len(list)))

        if len(list) % 2 != 0 :
                list.append('Break')

        sub_list_A, sub_list_B = self.random_teams(list)

        weeks_number, number_of_weeks_game = self.games_specifications(list)

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