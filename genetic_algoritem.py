from random import *
import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px

class GeneticAlgoritem:
    def __init__(self, primary_population = 0, number_of_generation = 0):
        self.primary_population = primary_population
        self.number_of_generation = number_of_generation

    def give_random_renge(self, temporary_list, beginning, end):
        for _ in range(self.primary_population):
            choose = randint(beginning, end)
            temporary_list.append(choose)

    def fitness_function(self, dataframe, chromosome):
        rate = (((
            (dataframe.loc[chromosome,"Secrecy"]**2 * dataframe.loc[chromosome,"Honestly"]**2) + 
            (dataframe.loc[chromosome,"Common_interests"]**2 + dataframe.loc[chromosome,"Mental_health"]**2) + 
            (dataframe.loc[chromosome,"Politeness"]*2 + dataframe.loc[chromosome,"Physical_health"]*2) + 
            (dataframe.loc[chromosome,"Appearance"] + dataframe.loc[chromosome,"Salary"] + dataframe.loc[chromosome,"Religious"])/3)) - 
            (dataframe.loc[chromosome,"Age_difference"] + dataframe.loc[chromosome,"Distance"]))

        return rate

    def mutation(self, dataframe):
        
        first_range =  ["Honestly",
                    "Distance",
                    "Physical_health",
                    "Mental_health",
                    "Politeness",
                    "Appearance"
                    ]

        second_range = ["Common_interests",
                    "Secrecy",
                    "Religious"
                    ]
        random_chromosome = choice(range(self.primary_population))
        new_chromosome = dataframe.iloc[random_chromosome:random_chromosome + 1, :].copy()
        random_attribute = choice(dataframe.columns[:-1])

        if random_attribute in first_range:
            new_chromosome.loc[random_chromosome,random_attribute] = randint(1, 5)
            dataframe = dataframe.append(new_chromosome, ignore_index = True)
            
        elif random_attribute in second_range:
            new_chromosome.loc[random_chromosome,random_attribute] = randint(1, 3)
            dataframe = dataframe.append(new_chromosome, ignore_index = True)
        
        # if random_attribute == 'Sex':
        #     new_chromosome.loc[random_chromosome,random_attribute] = randint(1, 2)
        #     dataframe = dataframe.append(new_chromosome, ignore_index = True)

        elif random_attribute == 'Age_difference':
            new_chromosome.loc[random_chromosome,random_attribute] = randint(0, 20)
            dataframe = dataframe.append(new_chromosome, ignore_index = True)

        elif random_attribute == 'Salary':
            new_chromosome.loc[random_chromosome,random_attribute] = randint(1, 10)
            dataframe = dataframe.append(new_chromosome, ignore_index = True)

        return dataframe

    def cross_over(self, dataframe):
        
        first_random_chromosome = choice(range(self.primary_population))
        second_random_chromosome = choice(range(self.primary_population))
        random_attribute = choice(range(1,10))

        first_new_chromosome = dataframe.iloc[first_random_chromosome:first_random_chromosome + 1, :random_attribute].copy()
        second_new_chromosome = dataframe.iloc[second_random_chromosome:second_random_chromosome + 1, random_attribute:].copy()
        third_new_chromosome = dataframe.iloc[first_random_chromosome:first_random_chromosome + 1, random_attribute:].copy()
        fourth_new_chromosome = dataframe.iloc[second_random_chromosome:second_random_chromosome + 1, :random_attribute].copy()
        final_new_chromosome_1 = pd.merge(first_new_chromosome, second_new_chromosome, how="cross")
        final_new_chromosome_2 = pd.merge(third_new_chromosome, fourth_new_chromosome, how="cross")

        dataframe = dataframe.append(final_new_chromosome_1, ignore_index = True)
        dataframe = dataframe.append(final_new_chromosome_2, ignore_index = True)

        return dataframe

    def Build_next_generations(self, dataframe, persent_of_mutation = 20, persent_of_cross_over = 5):
        
        Rate_best_chromosome = []

        for i in range(self.number_of_generation):
            for _ in range(int((self.primary_population/100)*persent_of_mutation)):
                dataframe = self.mutation(dataframe)
                
            for _ in range(int((self.primary_population/100)*persent_of_cross_over)):
                dataframe = self.cross_over(dataframe)

            list_of_rate = []
            for chromosome in range(len(dataframe)):
                rate = self.fitness_function(dataframe.iloc[chromosome:chromosome + 1,:], chromosome)
                list_of_rate.append(rate)
                
            new_dataframe = pd.DataFrame({'Rate': list_of_rate})
            dataframe.update(new_dataframe)

            dataframe.sort_values(by=['Rate'], ascending=False, ignore_index=True, inplace = True)
            dataframe.drop(dataframe.tail(int((self.primary_population/100)*(persent_of_mutation + persent_of_cross_over*2))).index, inplace = True)
            Rate_best_chromosome.append(dataframe.loc[0,'Rate'])
        
        return Rate_best_chromosome 

    def plot_best_gene(self, Rate_best_chromosome):

        fig = plt.figure(figsize=(20,10))
        plt.plot(list(range(1,self.number_of_generation+1)), Rate_best_chromosome, color='red', linestyle='dashed', linewidth = 1,
                marker='o', markerfacecolor='blue', markersize=8)
        plt.xlabel("Generation")
        plt.ylabel("Rate")
        plt.title('The process of genetic modification')
        plt.show()

        fig = px.line(x=list(range(self.number_of_generation)), y=Rate_best_chromosome)
        fig.show()

    def generations(self):
        
        age_difference = []
        honestly = []
        distance = []
        # sex = []
        salary = []
        common_interests = []
        physical_health = []
        mental_health = []
        politeness = []
        secrecy = []
        religious = []
        appearance = []
        rate = []

        # primary_population, number_of_generation = self.__init__()
        
        if type(self.primary_population) != int:
            print("Please give number.")
            return
        
        if self.primary_population < 100:
            print("You can't make your population with {} people. Please give number more than 100.".format(self.primary_population))
            return

        elif self.primary_population >= 100:
            print("Your primary population have {} people.".format(self.primary_population))

        if type(self.number_of_generation) != int:
            print("Please give number.")
            return

        self.give_random_renge(age_difference,0,20)
        self.give_random_renge(honestly,1,5)
        self.give_random_renge(distance,1,5)
        # self.give_random_renge(sex,1,2)
        self.give_random_renge(salary,1,10)
        self.give_random_renge(common_interests,1,3)
        self.give_random_renge(physical_health,1,5)
        self.give_random_renge(mental_health,1,5)
        self.give_random_renge(politeness,1,5)
        self.give_random_renge(secrecy,1,3)
        self.give_random_renge(religious,1,3)
        self.give_random_renge(appearance,1,5)
        self.give_random_renge(rate,0,0)

        df = pd.DataFrame({
                            "Age_difference":age_difference,
                            "Honestly":honestly,
                            "Distance":distance,
                            # "Sex":sex,
                            "Salary":salary,
                            "Common_interests":common_interests,
                            "Physical_health":physical_health,
                            "Mental_health":mental_health,
                            "Politeness":politeness,
                            "Secrecy":secrecy,
                            "Religious":religious,
                            "Appearance":appearance,
                            "Rate":rate
                            })

        Rate_best_chromosome = self.Build_next_generations(df,self.number_of_generation,self.primary_population)

        best_genes_plot = self.plot_best_gene(Rate_best_chromosome)

        return best_genes_plot