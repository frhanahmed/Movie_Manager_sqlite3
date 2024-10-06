import sqlite3


# Creating a connection with Database..
conn = sqlite3.connect("Movie_Manager.db")

# Creating a cursor which will help in executing QUERIES....
cursor = conn.cursor()


# Creation of a table
cursor.execute('''
        CREATE TABLE IF NOT EXISTS Movies(
               Id INTEGER PRIMARY KEY,
               Name TEXT NOT NULL,
               Year TEXT NOT NULL 
               )
''')


# Displaying the names of all the movies.....
def list_movies():
    cursor.execute("SELECT * FROM Movies")
    for row in cursor.fetchall():
        print(row)


# Adding Movies Details In Database..
def add_movie(name, year):
    cursor.execute("INSERT INTO Movies (Name, Year) VALUES (?, ?)", (name, year))
    conn.commit()


# Updating Existing Movie Details
def update_movie(movie_id, new_name, new_year):
    cursor.execute("UPDATE Movies SET Name = ?, Year = ? WHERE Id = ?", (new_name, new_year, movie_id))
    conn.commit()


# Deleting Existing Movie from Database
def delete_movie(movie_id):
    cursor.execute("DELETE FROM Movies where Id = ?", (movie_id,))
    conn.commit()



def main():
    while True:
        print("*"*70)
        print("\n\nMovie Manager with DB..\n")
        print("1. List All Favourite Movies")
        print("2. Add Movie")
        print("3. Update Movie Name")
        print("4. Delete Movie")
        print("5. Exit App")
        choice = input("Enter Your Choice: ")
        print("\n")

        match choice:
            case '1':
                print("*"*70)
                list_movies()
            case '2':
                name = input("Enter the Movie name: ")
                year = input("Enter the Year: ")
                add_movie(name, year)
            case '3':
                movie_id = input("Enter the Movie ID to update: ")
                name = input("Enter the Movie name: ")
                year = input("Enter the Year: ")
                update_movie(movie_id, name, year)
            case '4':
                movie_id = input("Enter Movie ID to delete: ")
                delete_movie(movie_id)
                print(f"\nYour Movie {name} is deleted successfully....")
            case '5':
                print("Your Movie Manager App Exited Successfully....")
                break
            case _:
                print("Invalid Option!! \n Please enter correct option..")

    conn.close()           

if __name__ == "__main__":
    main()
