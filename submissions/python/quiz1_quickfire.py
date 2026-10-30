import pandas as pd

MOVIE = "assignments/python/quiz1_data/movies.csv"
SCREEN = "assignments/python/quiz1_data/screenings.csv"

movie = pd.read_csv(MOVIE)
screen = pd.read_csv(SCREEN)

print("Question 1")
print(f"Movies: {len(movie)}, Minutes: {movie['minutes'].sum():,.2f}")

print("Question 2")
piz = movie[(movie["year"] >= 2010) & (movie["rating"] >= 8.0)]
piz = piz.sort_values("rating", ascending=False)
print(piz[["title", "year", "rating"]].to_string(index=False))

print("Question 3")
genres = movie.groupby("genre", as_index=False)["minutes"].sum()
genres = genres.sort_values("minutes", ascending=False)
print(genres[genres["minutes"] >= 400].to_string(index=False))

print("Question 4")
piz = movie[movie["minutes"] > 150]
piz["hours"] = piz["minutes"] / 60
piz = piz.sort_values("hours", ascending=False)
print(round(piz, 2).to_string(index=False))

print()
print("Question 5")
averages = movie["rating"].sum() / len(movie)
print(f"Average rating: {round(averages, 2)}")
movie["vs_average"] = (movie["rating"] - averages).round(2)
piz = movie[movie["vs_average"] > 0]
print(f"Above Average: {len(piz)}")

print()
print("Question 6")
screen = screen.groupby("movie_id", as_index=False)["tickets"].sum()
both = pd.merge(movie, screen, on="movie_id", how="outer", suffixes = ("_movie", "_screen"), indicator=True)
more = both[both["tickets"] >= 1000]
more = more.sort_values("tickets", ascending=False)
print(more[["title", "tickets"]].to_string(index=False))

print()
print("Question 7")
never = both[both["_merge"] == "left_only"]
nonexist = both[both["_merge"] == "right_only"]
never = never.fillna(0)
print(never[["movie_id", "title", "tickets"]].to_string(index=False))
print(nonexist[["movie_id", "tickets"]].to_string(index=False))

print()
print("Question 8")

def genre_stats(movies, genre):
    genre_movies = movies[movies["genre"] == genre]
    return {
        "genre": genre,
        "movies": len(genre_movies),
        "minutes": genre_movies["minutes"].sum(),
    }

genre_rows = []
for genre in ["Drama", "Comedy", "Sci-Fi"]:
    genre_rows.append(genre_stats(movie, genre))

genre_table = pd.DataFrame(genre_rows)
print(genre_table.to_string(index=False))
genre_table.to_csv("submissions/python/quiz1_genres.csv", index=False)
print("Saved submissions/python/quiz1_genres.csv")

print()
print("Question 9")
print("a. The function itself calculates the total minutes in the Movies table. It will print the total minutes amount because the function itself contains a print statement. The final print command will print nothing because there is no return statement in the function.")
print("b. The code adds a new column called average where it puts the calculated average into each line. It then prints the total of the column. It does not print the average rating.")
print("c. This code prints the total minutes in each genre of film. It is not a column since as_index = False is not present. It is an index. To make it a column, as_index=False should be added. ")   qwerASDDFGHZ