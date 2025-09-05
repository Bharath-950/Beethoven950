# cinema_app.py

from movie_manager import (
    create_movie, read_all, read_by_id,
    update_movie, delete_by_id, book_ticket
)
from movie import Movie

def menu():
    message = '''
🎟️ Cinema Ticket Booking System

1 - Add Movie
2 - View All Movies
3 - View Movie by ID
4 - Update Movie
5 - Delete Movie
6 - Book Ticket
7 - Exit

Enter your choice: '''

    try:
        choice = int(input(message))
    except ValueError:
        print(" Invalid input. Please enter a number.")
        return -1

    if choice == 1:
        title = input(" Movie Title: ")
        genre = input(" Genre: ")
        show_time = input(" Show Time (e.g., 7:30 PM): ")
        try:
            seats = int(input(" Available Seats: "))
            price = float(input(" Ticket Price: "))
            movie = Movie(-1, title, genre, show_time, seats, price)
            create_movie(movie)
            print(" Movie added successfully.")
        except ValueError:
            print(" Invalid seat or price input.")

    elif choice == 2:
        movies = read_all()
        if not movies:
            print(" No movies available.")
        else:
            print("\n Movie Listings:")
            for m in movies:
                print(m)

    elif choice == 3:
        try:
            id = int(input("Enter Movie ID: "))
            movie = read_by_id(id)
            if movie:
                print(" Movie Details:")
                print(movie)
            else:
                print("Movie not found.")
        except ValueError:
            print(" ID must be a number.")

    elif choice == 4:
        try:
            id = int(input("Enter Movie ID to update: "))
            old_movie = read_by_id(id)
            if not old_movie:
                print(" Movie not found.")
                return choice

            print(" Old Movie Info:")
            print(old_movie)
            title = input("New Title: ")
            genre = input("New Genre: ")
            show_time = input("New Show Time: ")
            seats = int(input("New Available Seats: "))
            price = float(input("New Ticket Price: "))
            updated = Movie(id, title, genre, show_time, seats, price)
            update_movie(updated)
            print(" Movie updated.")
        except ValueError:
            print(" Invalid input.")

    elif choice == 5:
        try:
            id = int(input("Enter Movie ID to delete: "))
            movie = read_by_id(id)
            if not movie:
                print(" Movie not found.")
                return choice
            confirm = input(f"Are you sure you want to delete '{movie.title}'? (y/n): ")
            if confirm.lower() == 'y':
                delete_by_id(id)
                print(" Movie deleted.")
        except ValueError:
            print(" ID must be a number.")

    elif choice == 6:
        try:
            id = int(input("Enter Movie ID to book: "))
            movie = read_by_id(id)
            if not movie:
                print(" Movie not found.")
                return choice
            print(f"🎬 Booking for: {movie.title}")
            seats = int(input("Enter number of seats to book: "))
            success, total = book_ticket(id, seats)
            if success:
                print(f"✅ Booking successful! Total: ${total:.2f}")
            else:
                print(" Not enough seats available.")
        except ValueError:
            print(" Invalid input.")

    elif choice == 7:
        print("👋 Thanks for using the Cinema Ticket Booking System.")
        return choice

    else:
        print(" Invalid choice. Select between 1–7.")

    return choice


def main():
    print(" Welcome to Cinema Ticket Booking App")
    choice = menu()
    while choice != 7:
        choice = menu()


if __name__ == "__main__":
    main()
