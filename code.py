import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 
import os

managers_raw_data = pd.read_excel("C:/Users/João Reis/Desktop/codingassignment/coding_assignment_joaoreis/footballdata/raw/managers_epl.xlsx")
print(managers_raw_data.head())
print("Number of coaches per nationality:")
print(managers_raw_data.groupby("Nat.").size())

print()
print()

epl_2007_raw_data = pd.read_excel("C:/Users/João Reis/Desktop/codingassignment/coding_assignment_joaoreis/footballdata/raw/epl_2007.xlsx")
epl_2007_raw_data.sort_values(by="team_points_season",ascending=False,inplace=True)
epl_2007_raw_data["Final Classification"]=np.arange(1,len(epl_2007_raw_data)+1)
print(epl_2007_raw_data)

print()
print()

X = epl_2007_raw_data['team_goaldiff_season']
Y = epl_2007_raw_data['team_points_season']
X = np.reshape(np.array(X),(-1, 1))
reg = LinearRegression().fit(X,Y)
intercept, slopecoefficient = reg.intercept_, reg.coef_
print("The intercept equals", intercept, ".", "The slope coefficient is equal to", slopecoefficient)
plt.plot(X,Y,"o")
plt.plot(X, intercept + slopecoefficient*X)
plt.xlabel('Team Goal Difference on 2007 Season')
plt.ylabel('Team Points on 2007 Season')
plt.show()

print()
print()


f_data_pl = pd.read_csv("C:/Users/João Reis/Desktop/codingassignment/coding_assignment_joaoreis/footballdata/raw/fdata_pl_2008.csv")
f_data_pl["Meanings"] = "FTHG : Full time home goals / FTAG : Full time away goals / FTR : Full time Result / HTHG : Half time home goals / HTAG : Half time away goals / HTR : Half time home goals / HS : Home team shots / AS : Away team shots / HST : Home team shots on target / AST : Away team shots on target / HC : Home team corners / AC : Away team corners / HF : Home team Fouls / AF : Away team Fouls / HY : Home team yellow cards / AY : Away team yellow cards / HR : Home team red cards / AR : Away team red cards"
print(f_data_pl.head(2))
f_data_pl.to_csv("C:/Users/João Reis/Desktop/codingassignment/coding_assignment_joaoreis/footballdata/raw/fdata_pl_2008.csv")

print()
print()

list = managers_raw_data["Nat."]
print(list)
coach_nationality = input("Choose coaches' country of origin: ")
while not coach_nationality in list:
    print("There were/are no coaches from that country! Try another one!")
    coach_nationality = input("Choose coaches' country of origin: ")
else: 
    print(managers_raw_data["Name" , "Club"])

print()
print()

def adding_meanings(filepath):
    for filename in os.listdir(filepath):
        if ".csv" in filename:
            f_data_pl = pd.read_csv(filename)
            f_data_pl["Meanings"] = "FTHG : Full time home goals / FTAG : Full time away goals / FTR : Full time Result / HTHG : Half time home goals / HTAG : Half time away goals / HTR : Half time home goals / HS : Home team shots / AS : Away team shots / HST : Home team shots on target / AST : Away team shots on target / HC : Home team corners / AC : Away team corners / HF : Home team Fouls / AF : Away team Fouls / HY : Home team yellow cards / AY : Away team yellow cards / HR : Home team red cards / AR : Away team red cards"
            print(f_data_pl.head(2))
            f_data_pl.to_csv("filepath/filename")
            
adding_meanings("C:/Users/João Reis/Desktop/codingassignment/coding_assignment_joaoreis/footballdata/raw")











