"""import neccessary files for classes and methods used"""
import media
import fresh_tomatoes

"""initialized array to hold movie objects"""
fav_movies = []

"""creating and appending movie objects"""
inception = media.Movie("Inception",
                        "https://tinyurl.com/za7f966",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")
fav_movies.append(inception)
godFather = media.Movie("The Godfather",
                        "https://tinyurl.com/ydenxa29",
                        "https://www.youtube.com/watch?v=kTlhEX0kmL8")
fav_movies.append(godFather)
avengers = media.Movie("Avengers",
                       "https://tinyurl.com/ycdnw5bn",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")
fav_movies.append(avengers)
starWarsForceAwaken = media.Movie("Star Wars: The Force Awakens",
                                  "https://tinyurl.com/y779v6wr",
                                  "www.youtube.com/watch?v=sGbxmsDFVnE")
fav_movies.append(starWarsForceAwaken)

"""using given method to create website"""
fresh_tomatoes.open_movies_page(fav_movies)
