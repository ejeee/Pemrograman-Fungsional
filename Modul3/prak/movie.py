from functools import reduce

movies = [
    {"title": "Avengers: Endgame", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {"title": "Spider-Man: No Way Home", "year": 2021, "rating": 7.6, "genre": "Action"},
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quiet Place Part II", "year": 2020, "rating": 7.4, "genre": "Horror"},
    {"title": "No Time To Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title": "The Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title": "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"},
]
# menghitung jumlah genre film
def count_genres(movies, genre): 
    genre_movies = filter(lambda movie: movie["genre"].lower() == genre.lower(), movies)
    return genre, len(list(genre_movies))

genre_counts = dict(map(lambda genre: count_genres(movies, genre), set(movie["genre"] for movie in movies)))
# dictionary 

# koleksi nilai tunggal
def avg_rate_by_year(movies, year):
    ratings = [movie["rating"] for movie in movies if movie["year"] == year]
    if len(ratings) > 0:
        avg_rating = sum(ratings) / len(ratings)
        return avg_rating
    else:
        return 0  

year_to_average_rating = {}
for movie in movies:
    year = movie["year"]
    if year not in year_to_average_rating:
        year_to_average_rating[year] = avg_rate_by_year(movies, year)

def higher_rate(movies):
    if not movies:
        return None
    highest_rated = max(movies, key=lambda movie: movie["rating"])
    return highest_rated

highest_rated = higher_rate(movies)

def find_movie_by_title(movies, title):
    found_movies = [movie for movie in movies if movie["title"].lower() == title.lower()]
    return found_movies

def find_movie(movies):
    title_to_search = input("\nEnter the movie title: ")
    matching_movies = find_movie_by_title(movies, title_to_search)

    if matching_movies:
        for movie in matching_movies:
            title = movie["title"]
            year = movie["year"]
            genre = movie["genre"]
            rating = movie["rating"]
            print(f"Movie information: {title} ({year}) \nGenre: {genre} \nRating: {rating}")
    else:
        print("Not found.")

def total_ratings_by_year(movies, year):
    ratings = [movie["rating"] for movie in movies if movie["year"] == year]
    return reduce(lambda x, y: x + y, ratings, 0)

def main():
    while True:
        print("\nMenu: ")
        print("1. Count movies by genre")
        print("2. Average rate movies by year")
        print("3. Total ratings by year")
        print("4. Find the highest movie rating")
        print("5. Search movie")
        print("6. Exit")
        choose = int(input("Input menu number (1/2/3/4/5): "))

        if choose == 1:
            print("\nTotal movies by genres:")
            for genre, count in genre_counts.items():
                print(f"{genre}: {count}")
        elif choose == 2:
            print("\nAverage rate movies by year:")
            year_to_average_rating_dict = {}
            for year, avg_rating in year_to_average_rating.items():
                year_to_average_rating_dict[year] = avg_rating
            print(year_to_average_rating_dict)
        elif choose == 3:
            print("\nTotal ratings for movies by year:")
            for year in set(movie["year"] for movie in movies):
                total = total_ratings_by_year(movies, year)
                print(f"Year {year}: Total Ratings = {total}")
        elif choose == 4:
            if highest_rated:
                title = highest_rated["title"]
                year = highest_rated["year"]
                genre = highest_rated["genre"]
                rating = highest_rated["rating"]
                print(f"\nHighest movie rating: {title} ({year}) \nGenre: {genre} \nRating: {rating}")
            else:
                print("Not found.")
        elif choose == 5:
            find_movie(movies)
        elif choose == 6:
            break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()
