def recommend(preference):
    recommendation = []
    for item, genres in recomendations.items():  
        if any(genre in preference for genre in genres):
            recommendation.append(item)
    return recommendation

recomendations = {
    "Jumanji (1995)": ["Adventure", "Children", "Fantasy"],
    "Sudden Death (1995)": ["Action"],
    "Dracula: Dead and Loving It (1995)": ["Comedy", "Horror"],
    "Balto (1995)": ["Adventure", "Animation", "Children"],
    "Nixon (1995)": ["Drama"],
    "Toy Story (1995)": ["Adventure", "Animation", "Children", "Comedy", "Fantasy"],
    "Grumpier Old Men (1995)": ["Comedy", "Romance"],
    "Heat (1995)": ["Action", "Crime", "Thriller"],
    "Sabrina (1995)": ["Comedy", "Romance"],
    "Tom and Huck (1995)": ["Adventure", "Children"],
    "Cutthroat Island (1995)": ["Action", "Adventure", "Romance"],
    "Casino (1995)": ["Crime", "Drama"],
    "Sense and Sensibility (1995)": ["Drama", "Romance"],
    "Waiting to Exhale (1995)": ["Comedy", "Drama", "Romance"],
    "Father of the Bride Part II (1995)": ["Comedy"],
    "GoldenEye (1995)": ["Action", "Adventure", "Thriller"],
    "American President, The (1995)": ["Comedy", "Drama", "Romance"],
    "Four Rooms (1995)": ["Comedy"],
    "Ace Ventura: When Nature Calls (1995)": ["Comedy"],
    "Money Train (1995)": ["Action", "Comedy", "Crime", "Drama", "Thriller"],
    "Get Shorty (1995)": ["Comedy", "Crime", "Thriller"],
    "The Godfather (1972)": ["Crime", "Drama"],
    "The Dark Knight (2008)": ["Action", "Crime", "Drama", "Thriller"],
    "Schindler's List (1993)": ["Biography", "Drama", "History", "War"],
    "Pulp Fiction (1994)": ["Crime", "Drama"],
    "The Lord of the Rings: The Fellowship of the Ring (2001)": ["Action", "Adventure", "Drama", "Fantasy"],
    "Inception (2010)": ["Action", "Adventure", "Sci-Fi", "Thriller"],
    "Forrest Gump (1994)": ["Comedy", "Drama", "Romance", "War"],
    "The Matrix (1999)": ["Action", "Sci-Fi"],
    "The Silence of the Lambs (1991)": ["Crime", "Drama", "Thriller"],
    "Star Wars: Episode IV - A New Hope (1977)": ["Action", "Adventure", "Fantasy", "Sci-Fi"],
    "Jurassic Park (1993)": ["Adventure", "Sci-Fi", "Thriller"],
    "Goodfellas (1990)": ["Biography", "Crime", "Drama"],
    "Seven Samurai (1954)": ["Action", "Adventure", "Drama"],
    "City of God (2002)": ["Crime", "Drama"],
    "Se7en (1995)": ["Crime", "Drama", "Mystery", "Thriller"],
    "The Silence of the Lambs (1991)": ["Crime", "Drama", "Thriller"],
    "Saving Private Ryan (1998)": ["Action", "Drama", "War"],
    "It's a Wonderful Life (1946)": ["Drama", "Family", "Fantasy"],
    "Life Is Beautiful (1997)": ["Comedy", "Drama", "Romance", "War"]
}

user_input = input("Enter your movie preferences (separated by commas): ")
preference = [p.strip() for p in user_input.split(',')]
recommendations_for_user = recommend(preference) 
print("Recommended movies for the preference:")
for movie in recommendations_for_user: 
    print("-", movie)