"""
https://dailypythonprojects.substack.com/p/favorite-movies-organizer

Create a program that starts with a predefined list of your favorite movies. For example:

favorite_movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight"]

Place the above list in your .py script and then add some code that does the following:

- Adds a new movie to the list (e.g., “Godfather”).

- Removes a specific movie from the list (e.g., “The Matrix”).

- Prints out the total number of movies in the list.

- Prints out the movies in alphabetical order.
"""

favorite_movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight"]

favorite_movies.append("The Godfather")
matrix_index = favorite_movies.index("The Matrix")
favorite_movies.pop(matrix_index)
print(f"total number of movies: {len(favorite_movies)}")
print("Your favorite movies in alphabical order:")
for movie in sorted(favorite_movies):
    print(movie)