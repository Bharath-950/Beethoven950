# movie_manager.py

from movie import Movie

movies = []

def create_movie(movie):
    global movies
    if len(movies) == 0:
        movie.id = 1
    else:
        movie.id = movies[-1].id + 1
    movies.append(movie)

def read_all():
    return movies

def read_by_id(id):
    for movie in movies:
        if movie.id == id:
            return movie
    return None

def update_movie(updated_movie):
    movie = read_by_id(updated_movie.id)
    if movie:
        movie.title = updated_movie.title
        movie.genre = updated_movie.genre
        movie.show_time = updated_movie.show_time
        movie.available_seats = updated_movie.available_seats
        movie.ticket_price = updated_movie.ticket_price

def delete_by_id(id):
    movie = read_by_id(id)
    if movie:
        movies.remove(movie)

def book_ticket(movie_id, seats_requested):
    movie = read_by_id(movie_id)
    if movie and movie.available_seats >= seats_requested:
        movie.available_seats -= seats_requested
        total_price = movie.ticket_price * seats_requested
        return True, total_price
    return False, 0
