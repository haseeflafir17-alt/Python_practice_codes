books = []
while True:
    print("""
1. Add book
2. View all books
3. Search book
4. Borrow book
5. Return book
6. Remove book
7. Count books
8. Reverse book list
9. Clear library
10. Exit    
""")
    choice = int(input("Enter the your choice: "))
    if choice == 1:
        book = input("Enter the book name: ").title()
        if book not in books:
            books.append(book)
            print(f"{book} added")
        else:
            print("Books already exist")
    elif choice == 2:
        if len(books) > 0:
            for b in books:
                print(f"{books.index(b)} : {b}")
        else:
            print("Library is empty")
    elif choice == 3:
        if len(books) > 0:
            b_search = input("Enter the book name to search: ").title()
            found = False
            for b in books:
                if b == b_search:
                    print("Book found")
                    print(f"{books.index(b)} : {b_search}")
                    found = True
                    break
            if not found:
                print("Book not found")
        else:
            print("Library is empty")
    elif choice == 4:
        if len(books) > 0:
            b_search = input("Enter the book name to borrow: ").title()
            found = False
            for b in books:
                if b == b_search:
                    print(f"{books.index(b)} : {b_search} is borrowed")
                    books.remove(b)
                    found = True
                    break
            if not found:
                print("Book unavailable.")
        else:
            print("Library is empty")
    elif choice == 5:
        r_book = input("Enter the book name to return: ").title()
        if r_book not in books:
            books.append(r_book)
            print("Book returned")
        else:
            print("Book already exists.")
    elif choice == 6:
        if len(books) > 0:
            r_book = input("Enter the book name to remove: ").title()
            if r_book in books:
                books.remove(r_book)
                print(f"{r_book} removed ")
            else:
                print(f"{r_book} not available to remove")
        else:
            print("Library is empty")
    elif choice == 7:
        print(f"Total Books: {len(books)}")
    elif choice == 8:
        if len(books) > 0:

            print(f"Reversed Books: {books.reverse()}")
        else:
            print("Library is empty")
    elif choice == 9:
        if len(books) > 0:
            confirm = input("Are you Sure (yes/ no)? ").lower()
            if confirm == "yes":
                books.clear()
                print("Library cleared")
            else:
                print("Library did not cleared")
        else:
            print("Library is empty")
    elif choice == 10:
        print("Exit")
        break
    else:
        print("Invalid choice!")