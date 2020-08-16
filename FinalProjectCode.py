#External library import
import pandas as pd

#Sample Input
friends_watched = {"Friend-0": ["Movie-1", "Movie-2", "Movie-3", "Movie-4", "Movie-6", "Movie-8"],
                   "Friend-1": ["Movie-0", "Movie-1", "Movie-2", "Movie-3", "Movie-8"],
                   "Friend-2": ["Movie-2", "Movie-3", "Movie-5", "Movie-6", "Movie-8"],
                   "Friend-3": ["Movie-0", "Movie-1", "Movie-2", "Movie-3", "Movie-4", "Movie-5", "Movie-8"],
                   "Friend-4": ["Movie-8"]}

movies_list = ["Movie-0", "Movie-1", "Movie-2", "Movie-3", "Movie-4", "Movie-5", "Movie-6", "Movie-7", "Movie-8"]
friends_list = ["Friend-0", "Friend-1", "Friend-2", "Friend-3", "Friend-4"]

movies_similarity = {"Movie-0": ["Movie-3", "Movie-4"],
                     "Movie-1": ["Movie-6"],
                     "Movie-2": ["Movie-5"],
                     "Movie-3": ["Movie-0", "Movie-4"],
                     "Movie-4": ["Movie-0", "Movie-3"],
                     "Movie-5": ["Movie-2"],
                     "Movie-6": ["Movie-1"],
                     "Movie-7": ["Movie-8"],
                     "Movie-8": ["Movie-7"]}

#Function which does the recommendation
def film_recommendation(friends_watched, movies_list, friends_list, movies_similarity):
    n = len(friends_list)
    m = len(friends_list)
    friends_movies = pd.DataFrame(0, columns = movies_list, index = friends_list)
    for key, value in friends_watched.items():
        friends_movies.loc[key, value] = 1
    
    Result = pd.DataFrame(friends_movies.sum(axis=0), columns = ["F"])
    Result["S"] = 0
    
    for key, value in movies_similarity.items():
        Result.loc[key, "S"] = Result.loc[value, "F"].sum()
        if Result.loc[key, "S"] != 0:
            Result.loc[key, "S"] /= n
        else:
            Result.loc[key, "S"] = 1
    
    Result["F/S"] = Result["F"]/Result["S"]
    
    return(Result["F/S"].idxmax())

film_recommendation(friends_watched, movies_list, friends_list, movies_similarity)