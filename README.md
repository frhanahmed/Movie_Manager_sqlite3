SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language. Some applications can use SQLite for internal data storage.
First sqlite3 is imported so that it can be used in the .py file.
After that, a connection is established with sqlite3 library by using the syntax : conn = sqlite3.connect("databse_name.db").
After that, a cursor is created which is used to execute SQL query. It is given as : cursor = conn.cursor()
After executing each query it is necessary to commmit the changes by using: conn.commit()
At the end, conn.close() is executed so that all connection is closed and successfully saved so that the database will not corrupt.
