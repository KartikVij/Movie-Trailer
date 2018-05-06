**This project is done with an aim to learn the new-edge technology of web development. The content of the project is from Udacity's Front End Nanodegree-1**

**TITLE :** MOVIE TRAILER

**PYTHON VERSION :** Python 2.7

**PROJECT :** A python file generating a movie website

**CODE CHECKER:** PEP8

**To run the project we need to follow these steps:**

1.  Unzip the file.
2.  Now list will be get displayed.
3.  Go to the entertainment file and right click on the file.
4.  Now click on the Edit with IDLE.
5.  A python file will get displayed.
6.  Now go to the run option and click on Run Module.
7.  The webbrowser page will open and display the lsit of Trailers. 

**Description:**

A server-side code that stores a list of movies, a movie trailer URL, and serve this data as web page; allowing visitors to review their movies and watch trailers.
In this readme file, I explain in detail how our website; fresh_tomatoes.py functions with media.py and entertainment.py to display trailer of movie.

**We started off with a plan:**


1.  Go to the website
2.  See all of the movies displayed
3.  Click on one to play its trailer

**Class structure**


We will need classes to build this movie website. We want our Movie class to be a template for a generic movie, and then create instances of that class like this:
ironm= Movie() 
and add details to each specific movie. So, we first need to come up with a list of properties that we think every movie should have:
1.  title
2.	trailer
3.	storyline
4.	poster_image
Defining our class
We created a file called media.py. Inside of it, start our Movie class by typing:
class Movie():
We Created a second file, called entertainment.py and connected it to the media.py file.
import media
ironm= media.Movie()
Let's define init. It will be defined like any other function in Python, and we use this with two underscore(__)before and after init.
And we define class movie like this:


class Movie():
    def __init__(self, title, storyline, poster_image, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

**Going back to our other file:**

import media

ironm = media.Movie("Iron Man",
                    "A film based on the Marvel Comics character.",
                    "https://goo.gl/qbRdKU",
                    "https://www.youtube.com/watch?v=8hYlB38asDY")

**What's going on behind the scenes?**

**When we run this code:**

ironm= media.Movie() several things happen.
init gets called All references to self inside of init point to ironm. The variables associated with the instance ironm get assigned values:ironm.title becomes "Iron Man" ironm.storyline becomes "A film based on the Marvel Comics character.".
The same is used to create the other movies like Sultan,Bajirao,Kaabil and 3 idiots

**Showing Trailers**
We defined our show_trailer method inside of the Movie class. Methods defined inside of a class are called instance methods.
import webbrowser

class Movie():
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
import media
ironm = media.Movie("Iron Man",
                    "A film based on the Marvel Comics character.",
                    "https://goo.gl/qbRdKU",
                    "https://www.youtube.com/watch?v=8hYlB38asDY")


ironm.show_trailer()
The web browser should open with the trailer playing!
Creating the Movie Website
We used this file called fresh_tomatoes.py in our own entertainment code. Let's create a list of movies that we are going to use:

import fresh_tomatoes

movies = [ironm, hulk, thor, captain, avengers, blackp]

fresh_tomatoes.open_movies_page(movies)

