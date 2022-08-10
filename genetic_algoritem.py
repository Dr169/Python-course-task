from random import *
import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px

class Genetic_algoritem():
    def give_random_renge(self, list, beginning, end, Primary_population = 100):
        for _ in range(Primary_population):
            choose = randint(beginning, end)
            list.append(choose)

    def fitness_function(self, DataFrame, chromosome):
        rate = (((
            (DataFrame.loc[chromosome,"Secrecy"]**2 * DataFrame.loc[chromosome,"Honestly"]**2) + 
            (DataFrame.loc[chromosome,"Common_interests"]**2 + DataFrame.loc[chromosome,"Mental_health"]**2) + 
            (DataFrame.loc[chromosome,"Politeness"]*2 + DataFrame.loc[chromosome,"Physical_health"]*2) + 
            (DataFrame.loc[chromosome,"Appearance"] + DataFrame.loc[chromosome,"Salary"] + DataFrame.loc[chromosome,"Religious"])/3)) - 
            (DataFrame.loc[chromosome,"Age_difference"] + DataFrame.loc[chromosome,"Distance"]))

        return rate

    def mutation(self, DataFrame,Primary_population):
        
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
        random_chromosome = choice(range(Primary_population))

        new_chromosome = DataFrame.iloc[random_chromosome:random_chromosome + 1, :].copy()

        random_attribute = choice(DataFrame.columns[:-1])

        if random_attribute in first_range:
            new_chromosome.loc[random_chromosome,random_attribute] = randint(1, 5)
            DataFrame = DataFrame.append(new_chromosome, ignore_index = True)
            
        elif random_attribute in second_range:
            new_chromosome.loc[random_chromosome,random_attribute] = randint(1, 3)
            DataFrame = DataFrame.append(new_chromosome, ignore_index = True)
        
        # if random_attribute == 'Sex':
        #     new_chromosome.loc[random_chromosome,random_attribute] = randint(1, 2)
        #     DataFrame = DataFrame.append(new_chromosome, ignore_index = True)

        elif random_attribute == 'Age_difference':
            new_chromosome.loc[random_chromosome,random_attribute] = randint(0, 20)
            DataFrame = DataFrame.append(new_chromosome, ignore_index = True)

        elif random_attribute == 'Salary':
            new_chromosome.loc[random_chromosome,random_attribute] = randint(1, 10)
            DataFrame = DataFrame.append(new_chromosome, ignore_index = True)

        return DataFrame

    def cross_over(self, DataFrame,Primary_population):
        
        first_random_chromosome = choice(range(Primary_population))
        second_random_chromosome = choice(range(Primary_population))

        random_attribute = choice(range(1,10))

        first_new_chromosome = DataFrame.iloc[first_random_chromosome:first_random_chromosome + 1, :random_attribute].copy()

        second_new_chromosome = DataFrame.iloc[second_random_chromosome:second_random_chromosome + 1, random_attribute:].copy()

        third_new_chromosome = DataFrame.iloc[first_random_chromosome:first_random_chromosome + 1, random_attribute:].copy()

        fourth_new_chromosome = DataFrame.iloc[second_random_chromosome:second_random_chromosome + 1, :random_attribute].copy()

        final_new_chromosome_1 = pd.merge(first_new_chromosome, second_new_chromosome, how="cross")
        final_new_chromosome_2 = pd.merge(third_new_chromosome, fourth_new_chromosome, how="cross")

        DataFrame = DataFrame.append(final_new_chromosome_1, ignore_index = True)
        DataFrame = DataFrame.append(final_new_chromosome_2, ignore_index = True)

        return DataFrame

    def Build_next_generations(self, DataFrame, Number_of_generation, Primary_population, persent_of_mutation = 20, persent_of_cross_over = 5):
        
        Rate_best_chromosome = []

        for i in range(Number_of_generation):
            for _ in range(int((Primary_population/100)*persent_of_mutation)):
                DataFrame = self.mutation(DataFrame,Primary_population)
                
            for _ in range(int((Primary_population/100)*persent_of_cross_over)):
                DataFrame = self.cross_over(DataFrame,Primary_population)

            list_of_rate = []
            for chromosome in range(len(DataFrame)):
                rate = self.fitness_function(DataFrame.iloc[chromosome:chromosome + 1,:], chromosome)
                list_of_rate.append(rate)
                
            new_DataFrame = pd.DataFrame({'Rate': list_of_rate})
            DataFrame.update(new_DataFrame)

            DataFrame.sort_values(by=['Rate'], ascending=False, ignore_index=True, inplace = True)
            DataFrame.drop(DataFrame.tail(int((Primary_population/100)*(persent_of_mutation + persent_of_cross_over*2))).index, inplace = True)
            Rate_best_chromosome.append(DataFrame.loc[0,'Rate'])
        
        return Rate_best_chromosome 

    def plot_best_gene(self, Number_of_generation,Rate_best_chromosome):

        fig = plt.figure(figsize=(20,10))
        plt.plot(list(range(1,Number_of_generation+1)), Rate_best_chromosome, color='red', linestyle='dashed', linewidth = 1,
                marker='o', markerfacecolor='blue', markersize=8)
        plt.xlabel("Generation")
        plt.ylabel("Rate")
        plt.title('The process of genetic modification')
        plt.show()

        fig = px.line(x=list(range(Number_of_generation)), y=Rate_best_chromosome)
        fig.show()

    def generations(self,Primary_population = 100, Number_of_generation = 10):
        if type(Primary_population) != int:
            return print("Please give number.")
        
        if Primary_population < 100:
            return print("You can't make your population with {} people. Please give number more than 100.".format(Primary_population))
        
        elif Primary_population >= 100:
            print("Your Primary population have {} people.".format(Primary_population))

        if type(Number_of_generation) != int:
            return print("Please give number.")

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

        self.give_random_renge(age_difference,0,20,Primary_population)
        self.give_random_renge(honestly,1,5,Primary_population)
        self.give_random_renge(distance,1,5,Primary_population)
        # self.give_random_renge(sex,1,2,Primary_population)
        self.give_random_renge(salary,1,10,Primary_population)
        self.give_random_renge(common_interests,1,3,Primary_population)
        self.give_random_renge(physical_health,1,5,Primary_population)
        self.give_random_renge(mental_health,1,5,Primary_population)
        self.give_random_renge(politeness,1,5,Primary_population)
        self.give_random_renge(secrecy,1,3,Primary_population)
        self.give_random_renge(religious,1,3,Primary_population)
        self.give_random_renge(appearance,1,5,Primary_population)
        self.give_random_renge(rate,0,0,Primary_population)

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

        Rate_best_chromosome = self.Build_next_generations(df,Number_of_generation,Primary_population)

        best_genes_plot = self.plot_best_gene(Number_of_generation,Rate_best_chromosome)

        return best_genes_plot