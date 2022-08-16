import json
import pandas as pd
from random import *
from matplotlib import pyplot as plt
import plotly.express as px

class TSP:
    def __init__(self , primary_population = 0 , number_of_generation = 0):

        with open('dict_of_distance(TSP problem).json', 'r') as fp:
            self.dict_of_distance = json.load(fp)

        self.list_of_cities = [
            "liverpool","Kiev","Stockholm","Barcelona",
            "Belgrade","Moscow","Lisbon","Warsaw","Oslo",
            "Amsterdam","Rome","Athens","Berlin","Paris",
            "Helsinki","Copenhagen","Prague","Zagreb",
            "Vienna","Istanbul"]

        self.primary_population = primary_population
        self.number_of_generation = number_of_generation

        self.city_1 = []
        self.city_2 = []
        self.city_3 = []
        self.city_4 = []
        self.city_5 = []
        self.city_6 = []
        self.city_7 = []
        self.city_8 = []
        self.city_9 = []
        self.city_10 = []
        self.city_11 = []
        self.city_12 = []
        self.city_13 = []
        self.city_14 = []
        self.city_15 = []
        self.city_16 = []
        self.city_17 = []
        self.city_18 = []
        self.city_19 = []
        self.city_20 = []
        self.Rate = list(range(self.primary_population))

    def mutation(self,dataframe):
        count = int((self.primary_population*20)/100)
        while count:
            random_chromosome = choice(range(self.primary_population))
            random_attribute_1 = choice(dataframe.columns[:-1])
            random_attribute_2 = choice(dataframe.columns[:-1])
            if random_attribute_1 != random_attribute_2:
                new_chromosome = dataframe.iloc[random_chromosome:random_chromosome + 1, :].copy()
                a = new_chromosome.loc[random_chromosome,random_attribute_1]
                b = new_chromosome.loc[random_chromosome,random_attribute_2]

                new_chromosome.loc[random_chromosome,random_attribute_1] = b
                new_chromosome.loc[random_chromosome,random_attribute_2] = a

                dataframe = pd.concat([dataframe,new_chromosome], ignore_index = True)
                count -= 1
            else:
                continue
        
        return dataframe
            
    def cross_over(self,dataframe):
        random_chromosome = choice(range(self.primary_population))
        random_attribute = choice(range(1,19))

        first_new_chromosome = dataframe.iloc[random_chromosome:random_chromosome + 1, :random_attribute].copy()
        second_new_chromosome = dataframe.iloc[random_chromosome:random_chromosome + 1, random_attribute:-1].copy()
        final_new_chromosome_1 = pd.merge(first_new_chromosome, second_new_chromosome, how="cross")
        final_new_chromosome_2 = pd.merge(final_new_chromosome_1, dataframe.iloc[random_chromosome:random_chromosome + 1,-1:], how="cross")

        dataframe = pd.concat([dataframe,final_new_chromosome_2], ignore_index = True)

        return dataframe

    def cost_function(self,dataframe):
        list_of_rate = []
        for chromosome in range(len(dataframe)):
            rate = 0
            for i in range(len(dataframe.columns)-2):
                for city_1 in self.dict_of_distance.keys(): 
                    if dataframe.iloc[chromosome,i] == city_1:
                        for city_2 in self.dict_of_distance[city_1]:
                            if dataframe.iloc[chromosome,i+1] == city_2[0]:
                                rate += int(city_2[1])
            list_of_rate.append(rate)

        return list_of_rate

    def Build_next_generations(self, dataframe, persent_of_mutation = 20, persent_of_cross_over = 10):
        
        rate_best_chromosome = []

        for generation in range(self.number_of_generation):

            if generation % 5 == 0:
                print("generation : ", generation) 

            dataframe = self.mutation(dataframe)
                
            for _ in range(int((self.primary_population*persent_of_cross_over)/100)):
                dataframe = self.cross_over(dataframe)

            list_of_rate = self.cost_function(dataframe)
                
            new_dataframe = pd.DataFrame({'Rate': list_of_rate})
            dataframe.update(new_dataframe)

            dataframe.sort_values(by=['Rate'], ascending=True, ignore_index=True, inplace = True)
            dataframe.drop(dataframe.tail(int((self.primary_population*(persent_of_mutation + persent_of_cross_over)/100))).index, inplace = True)
            rate_best_chromosome.append(dataframe.loc[0,'Rate'])

        best_chromosome = dataframe.iloc[0:1,:-1].values
        
        return rate_best_chromosome, best_chromosome


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

    def make_primary_population(self, temporary_list,sub_list_cities):
        choosen_city = choice(sub_list_cities)
        sub_list_cities.remove(choosen_city)
        temporary_list.append(choosen_city)
    
    def generations(self):

        if type(self.primary_population) != int:
            print("Please give number.")
            return
        
        if self.primary_population < 20:
            print("You can't make your population with {} people. Please give number more than 20.".format(self.primary_population))
            return

        elif self.primary_population >= 20:
            print("Your primary population have {} people.".format(self.primary_population))

        if type(self.number_of_generation) != int:
            print("Please give number.")
            return

        for _ in range(self.primary_population):
            sub_list_cities = self.list_of_cities.copy()

            self.make_primary_population(self.city_1, sub_list_cities)
            self.make_primary_population(self.city_2, sub_list_cities)
            self.make_primary_population(self.city_3, sub_list_cities)
            self.make_primary_population(self.city_4, sub_list_cities)
            self.make_primary_population(self.city_5, sub_list_cities)
            self.make_primary_population(self.city_6, sub_list_cities)
            self.make_primary_population(self.city_7, sub_list_cities)
            self.make_primary_population(self.city_8, sub_list_cities)
            self.make_primary_population(self.city_9, sub_list_cities)
            self.make_primary_population(self.city_10, sub_list_cities)
            self.make_primary_population(self.city_11, sub_list_cities)
            self.make_primary_population(self.city_12, sub_list_cities)
            self.make_primary_population(self.city_13, sub_list_cities)
            self.make_primary_population(self.city_14, sub_list_cities)
            self.make_primary_population(self.city_15, sub_list_cities)
            self.make_primary_population(self.city_16, sub_list_cities)
            self.make_primary_population(self.city_17, sub_list_cities)
            self.make_primary_population(self.city_18, sub_list_cities)
            self.make_primary_population(self.city_19, sub_list_cities)
            self.make_primary_population(self.city_20, sub_list_cities)

        df_1 = pd.DataFrame(columns=[
            "city_1","city_2","city_3","city_4",
            "city_5","city_6","city_7","city_8",
            "city_9","city_10","city_11","city_12",
            "city_13","city_14","city_15","city_16",
            "city_17","city_18","city_19","city_20",
            "Rate"])

        df2 = pd.DataFrame({
                "city_1" : self.city_1, "city_2" : self.city_2,
                "city_3" : self.city_3, "city_4" : self.city_4,
                "city_5" : self.city_5, "city_6" : self.city_6,
                "city_7" : self.city_7, "city_8" : self.city_8,
                "city_9" : self.city_9, "city_10" : self.city_10,
                "city_11" : self.city_11, "city_12" : self.city_12,
                "city_13" : self.city_13, "city_14" : self.city_14,
                "city_15" : self.city_15, "city_16" : self.city_16,
                "city_17" : self.city_17, "city_18" : self.city_18,
                "city_19" : self.city_19, "city_20" : self.city_20,
                "Rate" : self.Rate})
        
        result = pd.concat([df_1, df2], ignore_index = True)

        rate_best_chromosome, best_chromosome = self.Build_next_generations(result)
        best_genes_plot = self.plot_best_gene(rate_best_chromosome)

        print("Best chromosome : " ,best_chromosome)

        return best_genes_plot