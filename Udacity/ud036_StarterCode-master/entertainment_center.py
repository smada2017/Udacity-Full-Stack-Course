"""import neccessary files for classes and methods used"""
import media
import fresh_tomatoes

"""initialized array to hold movie objects"""
fav_movies = []

"""creating and appending movie objects"""
inception = media.Movie("Inception",
                        "https://tinyurl.com/za7f966",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")
fav_movies.append(inception)
godFather = media.Movie("The Godfather",
                        "https://tinyurl.com/ydenxa29",
                        "https://www.youtube.com/watch?v=dNE2PvbesQU")
fav_movies.append(godFather)
avengers = media.Movie("Avengers",
                       "https://tinyurl.com/ycdnw5bn",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")
fav_movies.append(avengers)
starWarsForceAwaken = media.Movie("Star Wars: The Force Awakens",
                                  "https://tinyurl.com/y779v6wr",
                                  "https://tinyurl.com/qz75fbn")
fav_movies.append(starWarsForceAwaken)

"""using given method to create website"""
fresh_tomatoes.open_movies_page(fav_movies)
