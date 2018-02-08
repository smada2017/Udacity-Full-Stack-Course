class Movie():
    """python class that generalizes a typical movie with attributes"""
    def __init__(self, movie_title, poster_img, trailer):
        '''defines all the attributes of the movie class'''
    	self.title = movie_title
    	self.poster_image_url = poster_img
    	self.trailer_youtube_url = trailer
