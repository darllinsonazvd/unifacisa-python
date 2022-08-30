import mysql.connector


def openDatabase(host, user, password, database):
    return mysql.connector.connect(
        host=host, user=user, password=password, database=database
    )


def closeDatabase(connection):
    connection.close()


def insertInDatabase(connection, sql, data):
    cursor = connection.cursor()
    cursor.execute(sql, data)
    connection.commit()
    id = cursor.lastrowid
    cursor.close()

    return id


def listDataBase(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()

    return results


def updateDatabase(connection, sql, dados):
    cursor = connection.cursor()
    cursor.execute(sql, dados)
    connection.commit()
    modifiedLines = cursor.rowcount
    cursor.close()

    return modifiedLines


def deleteRegistryInDatabase(connection, sql, dados):
    cursor = connection.cursor()
    cursor.execute(sql, dados)
    connection.commit()
    modifiedLines = cursor.rowcount
    cursor.close()

    return modifiedLines
