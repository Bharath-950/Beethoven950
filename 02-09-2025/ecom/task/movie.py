# movie.py

class Movie:
    def __init__(self, id, title, genre, show_time, available_seats, ticket_price):
        self.id = id
        self.title = title
        self.genre = genre
        self.show_time = show_time
        self.available_seats = available_seats
        self.ticket_price = ticket_price

    def __str__(self):
        return (f"[ID={self.id}, Title={self.title}, Genre={self.genre}, "
                f"ShowTime={self.show_time}, Seats={self.available_seats}, "
                f"Price=${self.ticket_price}]")

    def __repr__(self):
        return self.__str__()
