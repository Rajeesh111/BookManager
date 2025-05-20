
import database

database.connect()


def menu():
    while True:
        print("\n--- Book Manger")
        print("1.Add Book")
        print("2.View Book")
        print("3.Search Book")
        print("4.Update Book")
        print("5.Delete Book")
        print("6.Exit")

        choice=input("Enter your choice (1-6): ")

        if choice == "1":
            title=input("Enter title: ")
            author=input("Enter author: ")
            year=input("Enter year: ")
            genre=input("Enter genre: ")
            database.insert(title,author,year,genre)
            print("Book added successfully")

        elif choice == "2":
            books=database.view()
            for book in books:
                print(book)

        elif choice == "3":
            title=input("Title (leave blank if unknown): ")
            author=input("Author (leave blank if unknown): ")
            year=input("Year (leave blank if unknown): ")
            genre=input("Genre (leave blank if unknown): ")
            results=database.search(title,author,year,genre)
            for book in results:
                print(book)

        elif choice == "4":
            id=int(input("Enter book ID to update: "))
            title=input("New title: ")
            author=input("New author: ")
            year=input("New year: ")
            genre=input("New genre: ")
            database.update(id,title,author,year,genre)
            print("Book updated")

        elif choice == "5":
            id=int(input("Enter book ID to delete: "))
            database.delete(id)
            print("Book deleted")

        elif choice == "6":
            print("Goodbye")

        else:
            print("Invalid choice. Please try again.")

menu()




