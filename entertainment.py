import media  # here importing media library
import fresh_tomatoes  # importing fresh tomatoes

# storing information in variable ironm
ironm = media.Movie("Iron Man",
                    "A film based on the Marvel Comics character.",
                    "https://goo.gl/qbRdKU",
                    "https://www.youtube.com/watch?v=8hYlB38asDY")

# output the value of ironm storyline
print(ironm.storyline)

# storing information in variable hulk
hulk = media.Movie("The Incredible Hulk",
                   "A superhero film based on the Marvel Comics character.",
                   "https://goo.gl/K3DaLU",
                   "https://www.youtube.com/watch?v=xbqNb2PFKKA")

# output the value of hulk storyline
print(hulk.storyline)

# storing information in variable thor
thor = media.Movie("Thor",
                   "A film based on the Marvel Comics character.",
                   "https://goo.gl/PNtm31",
                   "https://www.youtube.com/watch?v=JOddp-nlNvQ")

# output the value of thor storyline
print(thor.storyline)

# storing information in variable captain
captain = media.Movie("Captain America", "A story of Warrior",
                      "https://goo.gl/9fv8nK",
                      "https://www.youtube.com/watch?v=JerVrbLldXw")

# output the value of captain storyline
print(captain.storyline)

# storing information in variable avengers
avengers = media.Movie("The Avengers",
                       "A film based on the Marvel Comics team.",
                       "https://goo.gl/C7kg6c",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")

# output the value of avengers storyline
print(avengers.storyline)

# storing information in variable blackp
blackp = media.Movie("Black Panther",
                     "A film based on the Marvel Comics character.",
                     "https://goo.gl/UcHiGr",
                     "https://www.youtube.com/watch?v=xjDjIWPwcPU")

# output the value of blackp storyline
print(blackp.storyline)

# an array of given movies
movies = [ironm, hulk, thor, captain, avengers, blackp]

# calling fresh_tomatoes library to display information
fresh_tomatoes.open_movies_page(movies)

# output the movie document
print(media.Movie.__doc__)
