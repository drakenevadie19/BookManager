from mysql_connector import connection
import mysql.connector

# Option 1: Add a Publisher
def addPublisher(name, phone, city):
    # inserts a tuple into Publisher
    cursor = connection.cursor()
    query = "insert into Publisher values('" + name + "', '" + phone + "', '" + city + "')"
    try:
        cursor.execute(query)
        connection.commit()
    except mysql.connector.errors.IntegrityError:
        cursor.close()
        return "Duplicate entry: publisher <" + name + "> already exists!"
    cursor.close()
    return "Publisher <" + name + "> added successfully"


# Option 2: Insert a Book
def addBook(ISBN, title, year, published_by, previous_edition, price):
    # inserts a tuple into Book
    cursor2 = connection.cursor()

    query = "INSERT INTO bookmanager.Book(ISBN, title, year, published_by, previous_edition, price) VALUES (%s, %s, %s, %s, %s, %s)"
    # Check for NULL
    if (title == "NULL"):
        title = None

    if (year == "NULL"):
        year = None
    else:
        year = str(year)

    if (published_by == "NULL"):
        published_by = None
    else:
        published_by = str(published_by)

    if (previous_edition == "NULL"):
        previous_edition = None
    else:
        previous_edition = str(previous_edition)

    if (price == "NULL"):
        price = 0
    else:
        price = str(price)

    #Make sure there is no other mistakes
    try:
        cursor2.execute(query, (ISBN, title, year, published_by, previous_edition, price,))
        connection.commit()
    except mysql.connector.errors.IntegrityError as e:
        cursor2.close()
        return e
    cursor2.close()
    return "Book <" + ISBN + "> added successfully"
#-------------------------End of Inserting Method------------------------------------


# Option 3: Edit a Book
# 3.1: Edit Title
def editBookTitle(ISBN, title):
    connection.reconnect()
    cursor = connection.cursor()
    query = "Update Book set title = %s where ISBN = %s"
    val = (title, str(ISBN))

    # Execute Query
    cursor.execute(query, val)
    connection.commit()
    connection.close()
    return "Update on Book <" + ISBN + "> successfully"

# 3.2: Edit Year
def editBookYear(ISBN, year):
    connection.reconnect()
    cursor = connection.cursor()
    query = "Update Book set year = %s where ISBN = %s"
    val = (str(year), str(ISBN))

    # Execute Query
    cursor.execute(query, val)
    connection.commit()
    connection.close()
    return "Update on Book <" + ISBN + "> successfully"

# 3.3: Edit Publisher
def editBookPublisher(ISBN, publisher):
    connection.reconnect()
    cursor = connection.cursor()
    query = "Update Book set published_by = %s where ISBN = %s"
    val = (publisher, str(ISBN))

    # Execute Query
    cursor.execute(query, val)
    connection.commit()
    connection.close()
    return "Update on Book <" + ISBN + "> successfully"

# 3.4: Edit Previous Edition
def editBookPreviousEdition(ISBN, previous_edition):
    connection.reconnect()
    cursor = connection.cursor()
    query = "Update Book set previous_edition = %s where ISBN = %s"
    val = (previous_edition, str(ISBN))

    # Execute Query
    cursor.execute(query, val)
    connection.commit()
    connection.close()
    return "Update on Book <" + ISBN + "> successfully"

# 3.5: Edit Price
def editBookPrice(ISBN, price):
    connection.reconnect()
    cursor = connection.cursor()
    query = "Update Book set price = %s where ISBN = %s"
    val = (str(price), str(ISBN))

    # Execute Query
    cursor.execute(query, val)
    connection.commit()
    connection.close()
    return "Update on Book <" + ISBN + "> successfully"

# 3.6: Edit All
def editBook(ISBN, title, year, published_by, previous_edition, price):
    # inserts a tuple into Book
    cursor3 = connection.cursor()
    anychange = False
    query = "Update Book AS b SET title = %s, year = %s, published_by = %s, previous_edition = %s, price = %s where ISBN = %s"
    # Check for NULL
    if (title == "NULL"):
        title = None

    if (year == "NULL"):
        year = None
    else:
        year = str(year)
        anychange = True

    if (published_by == "NULL"):
        published_by = None
    else:
        published_by = str(published_by)
        anychange = True

    if (previous_edition == "NULL"):
        previous_edition = None
    else:
        previous_edition = str(previous_edition)
        anychange = True

    if (price == "NULL"):
        price = 0
    else:
        price = str(price)
        anychange = True

    val = (title, year, published_by, previous_edition, price, ISBN)

    if anychange == False:
        return "There is no change"
    else :
        try:
            cursor3.execute(query, val)
            connection.commit()
        except mysql.connector.errors.IntegrityError as error:
            cursor3.close()
            return error
    cursor3.close()
    return "Update on Book <" + ISBN + "> successfully"
#-------------------------End of Editing Method------------------------------------


# Option 4: Delete a Book
# 4.1: Delete a book by ISBN
def deleteBookByISBN(ISBN):
    connection.reconnect()
    cursor4 = connection.cursor()

    # Since there is a foreign key constraint on this query,
    # we will turn off the checks
    cursor4.execute("SET FOREIGN_KEY_CHECKS = 0;")
    connection.commit()

    #Query
    query = "DELETE FROM Book WHERE ISBN = %s"
    val = (str(ISBN),)
    try:
        cursor4.execute(query, val)
    except mysql.connector.errors.IntegrityError as error:
        cursor4.close()
        return error

    cursor4.execute("SET FOREIGN_KEY_CHECKS = 1;")
    connection.commit()
    cursor4.close()
    return "Delete Book <" + ISBN + "> successfully"

# 4.2: Delete a book by Title
def deleteBookByTitle(title):
    connection.reconnect()
    cursor4 = connection.cursor()

    # Since there is a foreign key constraint on this query,
    # we will turn off the checks
    cursor4.execute("SET FOREIGN_KEY_CHECKS = 0;")
    connection.commit()

    #Query
    query = "DELETE FROM Book WHERE title = %s"
    val = (title,)
    try:
        cursor4.execute(query, val)
    except mysql.connector.errors.IntegrityError as error:
        cursor4.close()
        return error

    cursor4.execute("SET FOREIGN_KEY_CHECKS = 1;")
    connection.commit()
    cursor4.close()
    return "Delete Book <" + title + "> successfully"
#-------------------------End of Deleting Method------------------------------------


# Option 5: Search for a Book
# 5.1: Search all books
def findAll():
    connection.reconnect()
    cursor = connection.cursor()
    query = "select * from bookmanager.Book"
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return results

# 5.2: Search by Title
def findByTitle(title):
    # returns all tuples in Book with specified title attribute
    connection.reconnect()
    cursor = connection.cursor()
    query = "select Book.ISBN, Book.title from bookmanager.Book where Book.title='" + title + "'"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

# 5.3: Search by ISBN
def findByISBN(ISBN):
    connection.reconnect()
    cursor = connection.cursor()
    query = "select * from bookmanager.Book B where B.ISBN =  (%s)"
    cursor.execute(query, (ISBN,))
    results = cursor.fetchall()
    return results

# 5.4: Search by Publisher
def findByPublisher(publisher):
    connection.reconnect()
    cursor = connection.cursor()
    query = "select * from bookmanager.Book B where B.published_by =  (%s)"
    cursor.execute(query, (publisher,))
    results = cursor.fetchall()
    return results

# 5.5: Search by Price Range (Min-Max)
def findByPriceRange(min, max):
    connection.reconnect()
    cursor = connection.cursor()
    query = "select * from bookmanager.Book B where B.price >= (%s) and B.price <= (%s)"
    cursor.execute(query, (min, max,))
    results = cursor.fetchall()
    return results

# 5.6: Search by Year
def findByYear(year):
    connection.reconnect()
    cursor = connection.cursor()
    query = "select * from bookmanager.Book B where B.year =  (%s)"
    cursor.execute(query, (year,))
    results = cursor.fetchall()
    return results

# 5.7: Search by Title and Publisher
def findByTitleNPublisher(title, publisher):
    connection.reconnect()
    cursor = connection.cursor()
    query = "select * from bookmanager.Book B where B.title = (%s) and B.published_by = (%s)"
    cursor.execute(query, (title, publisher,))
    results = cursor.fetchall()
    return results
#-------------------------End of Searching Method------------------------------------

# Additional Methods
# Checking whether Publisher exists?
def findPublisher(publisher):
    connection.reconnect()
    cursor = connection.cursor()
    query = "select * from bookmanager.Publisher P where P.name = (%s)"
    cursor.execute(query, (publisher,))
    results = cursor.fetchall()
    return results