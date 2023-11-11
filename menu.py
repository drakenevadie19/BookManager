import sys
import book_dao


#All declared menus
# ---------------------------------------------------------------------------------------
menu_options = {
    1: 'Add a Publisher',
    2: 'Add a Book',
    3: 'Edit a Book',
    4: 'Delete Books',
    5: 'Search Books',
    6: 'Exit',
}

delete_menu_options = {
    1: 'Delete by ISBN',
    2: 'Delete by Title'
}

search_menu_options = {
    1: 'Search all books',
    2: 'Search by Title',
    3: 'Search by ISBN',
    4: 'Search by Publisher',
    5: 'Search by Price Range (Min-Max)',
    6: 'Search by Year',
    7: 'Search by Title and Publisher',
}

edit_menu_options = {
    1: 'Edit Title',
    2: 'Edit Year',
    3: 'Edit Publisher',
    4: 'Edit Previous Edition',
    5: 'Edit Price',
    6: 'Edit all',
}
# ---------------------------------------------------------------------------------------

# All Searching methods
# ---------------------------------------------------------------------------------------
#Find all books
def search_all_books():
    # Use a data access object (DAO) to 
    # abstract the retrieval of data from 
    # a data resource such as a database.
    results = book_dao.findAll()

    # Display results
    print("The following are all books.")
    for item in results:
        print(item[0], item[1])
    print("The end of books.")

#Find books by their title
def search_by_title():
    title = input('Enter the book title: ')
    results = book_dao.findByTitle(title)
    if len(results) == 0:
        print("No book found")
    else:
        print("The following are books with the input title.")
        for item in results:
            print(item[0], item[1])
        print("The end of books.")

#Find books by their ISBN
def search_by_ISBN():
    ISBN = input('Enter the book ISBN: ')
    results = book_dao.findByISBN(ISBN)

    if len(results) == 0:
        print("No book found")
    else:
        print("The following are books with the input ISBN.")
        for item in results:
            print(item[0], item[1])
        print("The end of books.")

#Find books by their publisher
def search_by_publisher():
    publisher = input('Enter the book publisher: ')
    results = book_dao.findByPublisher(publisher)
    if len(results) == 0:
        print("No book found")
    else:
        print("The following are books with the input publisher.")
        for item in results:
            print(item[0], item[1], item[3])
        print("The end of books.")

#Find books within a price range
def search_by_price_range():
    min = input('Enter the min price: ')
    max = input('Enter the max price: ')
    results = book_dao.findByPriceRange(min, max)
    if len(results) == 0:
        print("No book found")
    else:
        print("The following are books with the input price range.")
        for item in results:
            print(item[0], item[1], item[5])
        print("The end of books.")

#Find books by published year
def search_by_year():
    year = int(input('Enter the year: '))
    results = book_dao.findByYear(year)
    if len(results) == 0:
        print("No book found")
    else:
        print("The following are books with the input year.")
        for item in results:
            print(item[0], item[1], item[2])
        print("The end of books.")

#Find book by title and publiser
def search_by_title_publisher():
    title = input('Enter the title: ')
    publisher = input('Enter the publisher: ')
    results = book_dao.findByTitleNPublisher(title, publisher)
    if len(results) == 0:
        print("No book found")
    else:
        print("The following are books with the input title and publisher.")
        for item in results:
            print(item[0], item[1], item[3])
        print("The end of books.")

# Print menus
# ---------------------------------------------------------------------------------------
def print_menu():
    print()
    print("Please make a selection")
    for key in menu_options.keys():
        print (str(key)+'.', menu_options[key], end = "  ")
    print()
    print("The end of top-level options")
    print()

def print_search_menu():
    print()
    print("----------------------------------------")
    for key in search_menu_options.keys():
        print(str(key)+'.', search_menu_options[key], end = "  ")
        print()
    print("----------------------------------------")
    print()

def print_delete_menu():
    print("----------------------------------------")
    for key in delete_menu_options.keys():
        print(str(key)+'.', delete_menu_options[key], end = "  ")
    print()
    print("----------------------------------------")
    print()

def print_edit_menu():
    print()
    for key in edit_menu_options.keys():
        print (str(key)+'.', edit_menu_options[key], end = "  ")
    print()
    print("The end of top-level options")
    print()
# ---------------------------------------------------------------------------------------

# All Checking Method
def checkValidTitle():
    title = ""
    while title == "":
        title = input("Enter new Book's Title: ")
        if len(title) > 50:
            title = ""
            print("Error: Book's Title can not exceed 50 chatacters!")
        elif title == 'NULL':
            print("Warning!! You should provide a Title for your book!")
        elif len(book_dao.findByTitle(title)) != 0:
            print("Warning!! There already exists a book with title: " + title + ".")
            continue1 = input("Do you want to continue? (y/n)")
            if (continue1 == 'n'):
                title = ""
    return title

def checkValidYear():
    year = ""
    while year == "":
        year = input("Enter new Book's Establish Year: ")
        if year != 'NULL':
            try:
                int(year)
            except ValueError:
                year = ""
                print("Error: Book's Establish Year must be integers!")
            if int(year) < 0:
                year = ""
                print("Error: Book's Establish Year must be positive!")
        elif year == 'NULL':
            print("Warning!! You should provide a Year of Publishing for your book!")
    return year

def checkValidPublisher():
    published_by = ""
    while published_by == "":
        published_by = input("Enter new Book's Publisher: ")
        if len(published_by) > 25:
            published_by = ""
            print("Error: Book's Title can not exceed 25 chatacters!")
        elif published_by == 'NULL':
            print("Warning!! You should provide a Publisher for your book!")
        elif len(book_dao.findPublisher(published_by)) == 0:
            published_by = ""
            print("Error: Publisher Does not exist!")
    return published_by

def checkValidPreviousEdition():
    previous_edition = ""
    while previous_edition == "":
        previous_edition = input("Enter new Book's Previous Edition: ")
        if len(previous_edition) > 10:
            previous_edition = ""
            print("Error: Book's Previous Edition length can not exceed 10!")
        elif previous_edition == 'NULL':
            print("Warning!! You should provide a Previous Edition for your book!")
    return previous_edition

def checkValidPrice():
    price = ""
    while price == "":
        price = input("Enter new Book's Price: ")
        if price != "NULL":
            try:
                float(price)
            except ValueError:
                price = ""
                print("Error: Book's Establish Year must be Float!")
            if float(price) < 0:
                price = ""
                print("Error: Book's price must be positive!")
        elif price == 'NULL':
            print("Warning!! You should provide a price for your book!")
    return price

# Option 1: Add a Publisher
def option1():  # add a publisher
    print()
    print("-------Add a new Publisher-------")
    print("Type NULL for no entry.")
    name = input("Enter Name: ")
    phone = ""
    while phone == "":
        phone = input("Enter Phone Number: ")
        if len(phone) != 10:
            phone = ""
            print("Error: Phone number length must be 10!")
        try:
            int(phone)
        except ValueError:
            phone = ""
            print("Error: Phone number must consist of integers!")
    city = ""
    while city == "":
        city = input("Enter City: ")
        if len(city) > 20:
            city = ""
            print("Error: City name too long (max 20 characters)!")
    result = book_dao.addPublisher(name, phone, city)
    print(result)
    print("------------------End of Adding a Publisher Method------------------")

# Option 2: Insert a Book
def option2():
    print()
    print("-------Add a new Book-------")
    print("Type NULL for no entry.")
    print("Make sure the your Book's publisher is already exist or You can add a new Publisher before add your new book.")
    ISBN = ""
    while ISBN == "":
        ISBN = input("Enter Book's ISBN: ")
        if len(ISBN) != 10:
            ISBN = ""
            print("Error: ISBN number length must be 10!")
        # Checking whether a book with this ISBN existing in the database?
        elif len(book_dao.findByISBN(ISBN)) != 0:
            print("There already exists a book with ISBN: " + ISBN + ". Please try again!")
            ISBN = ""
    title = ""
    while title == "":
        title = input("Enter Book's Title: ")
        if len(title) > 50:
            title = ""
            print("Error: Book's Title can not exceed 50 chatacters!")
    year = ""
    while year == "":
        year = input("Enter Book's Establish Year: ")
        try:
            int(year)
        except ValueError:
            year = ""
            print("Error: Book's Establish Year must be integers!")
        if int(year) < 0:
            year = ""
            print("Error: Book's Establish Year must be positive!")
    published_by = ""
    while published_by == "":
        published_by = input("Enter Book's Publisher: ")
        if len(published_by) > 25:
            published_by = ""
            print("Error: Book's Title can not exceed 25 chatacters!")
    previous_edition = ""
    while previous_edition == "":
        previous_edition = input("Enter Book's Previous Edition: ")
        if len(previous_edition) > 10:
            previous_edition = ""
            print("Error: Book's Previous Edition length can not exceed 10!")
    price = ""
    while price == "":
        price = input("Enter Book's Price: ")
        try:
            float(price)
        except ValueError:
            price = ""
            print("Error: Book's Establish Year must be Float!")
        if float(price) < 0:
            price = ""
            print("Error: Book's price must be positive!")
    result = book_dao.addBook(ISBN, title, year, published_by, previous_edition, price)
    print(result)
    print("------------------End of Adding a Book Method------------------")

# Option 3: Edit a Book
def option3():
    print()
    print("-------Edit a Book's information-------")
    print("Choose Option to Edit a Book: ")
    print_edit_menu()
    edit = ""
    while edit == "":
        edit = input("Enter Your Editing Option: ")
        if edit != '1' and edit != '2' and edit != '3' and edit != '4' and edit != '5' and edit != '6':
            edit = ""
            print("Please input a valid interger from 1-6!")
    result = "Check the database to make sure that your ISBN is valid"

    #Make sure that the ISBN is valid
    ISBN = ""
    while ISBN == "":
        ISBN = input("What is the Book's ISBN, that you want to edit: ")
        if len(ISBN) != 10:
            ISBN = ""
            print("Error: ISBN number length must be 10!")
        elif len(book_dao.findByISBN(ISBN)) == 0:
            print("We could not find any book with ISBN: " + ISBN + ". Please check again!")
            ISBN = ""

    # If User choose to edit book's title
    if edit == '1':
        print("You choose to edit the book's title! Let's go!")
        title = checkValidTitle()
        result = book_dao.editBookTitle(ISBN, title)
    # If User choose to edit book's Publish Year
    elif edit == '2':
        print("You choose to edit the book's Publish year! Let's go!")
        year = checkValidYear()
        result = book_dao.editBookYear(ISBN, year)
    # If User choose to edit book's Publisher
    elif edit == '3':
        print("You choose to edit the book's Publisher! Let's go!")
        published_by = checkValidPublisher()
        result = book_dao.editBookPublisher(ISBN, published_by)
    # If User choose to edit book's Previous Edition
    elif edit == '4':
        print("You choose to edit the book's Previous Edition! Let's go!")
        previous_edition = checkValidPreviousEdition()
        result = book_dao.editBookPreviousEdition(ISBN, previous_edition)
    # If User choose to edit book's Price
    elif edit == '5':
        print("You choose to edit the book's Price! Let's go!")
        price = checkValidPrice()
        result = book_dao.editBookPrice(ISBN, price)
    # This is for when user want to change many value of the book => can save time
    elif edit == '6':
        print("You choose to edit the book's all element! Let's go!")
        print("Type NULL if you don't know what to change to!")
        title = checkValidTitle()
        year = checkValidYear()
        published_by = checkValidPublisher()
        previous_edition = checkValidPreviousEdition()
        price = checkValidPrice()
        result = book_dao.editBook(ISBN, title, year, published_by, previous_edition, price)

    print(result)
    print("------------------End of Editing Method------------------")

# Option 4: Delete a Book
def option4():
    print("-------Delete a Book-------")
    print("Choose Option to Deleting Book: ")
    print_delete_menu()
    delete = ""
    while delete == "":
        delete = input("Enter Your Deleting Option: ")
        if delete != '1' and delete != '2':
            delete = ""
            print("Please input a valid interger from 1-2!")
    result = "Check the database to make sure that your ISBN or title are valid"

    # If user choose to delete by Book's ISBN
    if delete == '1':
        ISBN = ""
        while ISBN == "":
            ISBN = input("What is the Book's ISBN, that you want to delete: ")
            if len(ISBN) != 10:
                ISBN = ""
                print("Please input a valid ISBN with length of 10")
            elif len(book_dao.findByISBN(ISBN)) == 0:
                print("We could not find any book with ISBN: " + ISBN + ". Please check again!")
                ISBN = ""
        result = book_dao.deleteBookByISBN(ISBN)
    # If user choose to delete by Book's Title
    elif delete == '2':
        title = ""
        while title == "":
            title = input("Enter Book's Title to delete: ")
            if len(title) > 50:
                title = ""
                print("Please input a valid Title name that not exceed 50 chatacters!")
            elif len(book_dao.findByTitle(title)) == 0:
                print("We could not find any book with title: " + title + ". Please check again!")
                title = ""
        result = book_dao.deleteBookByTitle(title)
    print(result)
    print("------------------End of Deleting Method------------------")

# Option 5: Search for a Book
def option5():
    print("-------Search for a Book-------")
    print("Choose Option to Searching Book: : ")
    # print_search_menu
    print_search_menu()
    search = ""
    while search == "":
        search = input("Enter Searching Option: ")
        if search != '1' and search != '2' and search != '3' and search != '4' and search != '5' and search != '6' and search != '7':
            search = ""
            print("Please input a valid interger from 1-7!")

    # If user choose to Search all books
    if search == '1':
        print("Search Option 1: Search all books.")
        search_all_books()
    elif search == '2':
        print("Search Option 2: Search by Title.")
        search_by_title()
    elif search == '3':
        print("Search Option 3: Search by ISBN.")
        search_by_ISBN()
    elif search == '4':
        print("Search Option 4: Search by Publisher.")
        search_by_publisher()
    elif search == '5':
        print("Search Option 5: Search by Price Range (Min-Max).")
        search_by_price_range()
    elif search == '6':
        print("Search Option 6: Search by Year.")
        search_by_year()
    elif search == '7':
        print("Search Option 7: Search by Title and Publisher.")
        search_by_title_publisher()
    print("------------------End of Searching Method------------------")


if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        except:
            print('Wrong input. Please enter a number ...')

        # Check what choice was entered and act accordingly
        if option == 1:
            option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            option5()
        elif option == 6:
            print('Thanks your for using our database services!')
            print('Have a nice day!!')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 6.')











