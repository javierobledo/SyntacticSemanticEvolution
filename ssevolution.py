from mysql.connector import MySQLConnection, Error, errorcode

from SyntacticSemanticEvolution.corpus.eccotcp.read_xml import read_db_config

DB_NAME = 'ecco_tcp'


def connect():
    """ Connect to MySQL database """
    db_config = read_db_config()
    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('connection established.')
        else:
            print('connection failed.')

    except Error as error:
        print(error)

    finally:
        return conn

cnx = connect()
cursor = cnx.cursor()

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cnx.database = DB_NAME
except Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)


if __name__ == '__main__':
    connect()