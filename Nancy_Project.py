# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:49:56 2024

@author: NANCY DAVID
"""

import pandas as pd
import numpy as np
# Question 1--------------------------
#Highest rated movie in the dataset
#load the dataset
df = pd.read_csv('movie_dataset.csv')
# print(df)

max_rating_idx = df['Rating'].idxmax()
movie_names = df['Title']
print(movie_names[max_rating_idx])
# ANSWER:The Dark Knight
#------------------------------------

# Question 2--------------------------
#Average revenue
revenue= df["Revenue (Millions)"]
revenue2 = revenue.dropna()
average_value = np.mean(revenue)
print(average_value)
# ANSWER:82.95637614678898
# in millions
#------------------------------------

# Question 3--------------------------
# df = pd.DataFrame(df)
movies_2015_2017 = df[(df["Year"] >= 2015) & (df["Year"] <= 2017)]
average_revenue_2015_2017 = movies_2015_2017["Revenue (Millions)"].mean()
print("The average revenue of movies from 2015 to 2017 is:", average_revenue_2015_2017)
# ANSWER: 63.099905660377345

# Question 4--------------------------
# Number of movies released in 2016
movies_2016 = df[df["Year"] == 2016]
num_movies_2016 = len(movies_2016)
print("The number of movies released in 2016 is:", num_movies_2016)
# ANSWER:297

# Question 5--------------------------
# Movies that were directed by Christopher Nolan
movies_directed_by_nolan = df[df["Director"] == "Christopher Nolan"]
num_movies_directed_by_nolan = len(movies_directed_by_nolan)
print("The number of movies directed by Christopher Nolan is:", num_movies_directed_by_nolan)
# ANSWER:5


# Question 6--------------------------
# The number of movies in the dataset have a rating of at least 8.0
highly_rated_movies = df[df["Rating"] >= 8.0]
num_highly_rated_movies = len(highly_rated_movies)
print("The number of movies with a rating of at least 8.0 is:", num_highly_rated_movies)
# ANSWER:98

# Question 7--------------------------
# The median rating of movies directed by Christopher Nolan
median_rating_nolan = movies_directed_by_nolan["Rating"].median()
print("The median rating of movies directed by Christopher Nolan is:", median_rating_nolan)
# ANSWER:8.6

# Question 8--------------------------
# The year with the highest average rating
year_highest_avg_rating = df.groupby("Year")["Rating"].mean().idxmax()
print("The year with the highest average rating is:", year_highest_avg_rating)
# ANSWER:2007


# Question 9--------------------------
# The percentage increase in the number of movies made between 2006 and 2016
movies_2006 = df[df["Year"] == 2006]
movies_2016 = df[df["Year"] == 2016]

num_movies_2006 = len(movies_2006)
num_movies_2016 = len(movies_2016)

percentage_increase = ((num_movies_2016 - num_movies_2006) / num_movies_2006) * 100
print("The percentage increase in the number of movies made between 2006 and 2016 is:", percentage_increase)
# ANSWER:575


# Question 10--------------------------
# The most common actor in all the movies
actors = df["Actors"].str.split(", ")
all_actors = [actor for sublist in actors for actor in sublist]
most_common_actor = pd.Series(all_actors).value_counts().index[0]
print("The most common actor in all the movies is:", most_common_actor)
# ANSWER:Mark Wahlberg


# Question 11--------------------------
# Number of unique genres in the dataset
unique_genres = df["Genre"].str.split(", ")
unique_genres = pd.Series([genre for sublist in unique_genres for genre in sublist]).unique()
num_unique_genres = len(unique_genres)
print("The number of unique genres in the dataset is:", num_unique_genres)
#END
#To calculate correlaation
numerical_features = ["Genre", "Revenue (Millions)", "Metascore", "Runtime (Minutes)", "Rating", "Votes"]

# Compute the correlation matrix
correlation_matrix = df[numerical_features].corr()

# Print the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)