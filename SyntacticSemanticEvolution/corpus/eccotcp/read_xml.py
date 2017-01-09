"""
This is the "read_xml" module.

The read_xml module supplies multiple function for unzip, read and store XML files from the ECCO-TCP Dataset
"""
from zipfile import ZipFile
import os
from configparser import ConfigParser


def unzip_ecco_tcp_xmls(origin_directory, destination_directory):
    """
    Create, if doesn't exist, the destination_directory and unzip all zip files contained in origin_directory.
    If the origin_directory doesn't exist, an exception is raised.
    :param origin_directory: The directory's path where ECCO-TCP zip files are stored
    :param destination_directory: The directory's path where the ECCO-TCP dataset will be unzipped
    :return: None
    >>> unzip_ecco_tcp_xmls("/home/jrobledo/foo","/home/jrobledo/bar")
    Traceback (most recent call last):
        ...
    OSError: The dataset directory doesn't exist
    >>> unzip_ecco_tcp_xmls("/home/jrobledo/Dropbox/ECCO-TCP","/home/jrobledo/bar")
    """
    if not files_actually_unzipped(origin_directory, destination_directory):
            for file in os.listdir(origin_directory):
                if file.endswith(".zip"):
                    ZipFile(os.path.join(origin_directory, file)).extractall(destination_directory)


def files_actually_unzipped(origin_directory, destination_directory):
    """
    Verifies if the origin_directory with zipped files are actually unzipped. If files are unzipped, return True.
    Returns False otherwise. If the origin_directory doesn't exist an IOError is raised.
    :param origin_directory: The directory's path where ECCO-TCP zip files are stored
    :param destination_directory: The directory's path where the ECCO-TCP dataset will be unzipped
    :return: True or False
    >>> files_actually_unzipped("/home/jrobledo/foo","/home/jrobledo/bar")
    Traceback (most recent call last):
        ...
    OSError: The dataset directory doesn't exist
    """
    names = []
    if not os.path.exists(origin_directory):
        raise IOError("The dataset directory doesn't exist")
    if not os.path.exists(destination_directory):
        os.mkdir(destination_directory)
    for file in os.listdir(origin_directory):
        if file.endswith(".zip"):
            names += ZipFile(os.path.join(origin_directory, file)).namelist()
    other_names = os.listdir(destination_directory)
    return len(set(names) & set(other_names)) == len(set(names))


def read_db_config(filename='/home/jrobledo/PycharmProjects/SyntacticSemanticEvolution/config.ini', section='mysql'):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    >>> sorted(read_db_config().items())
    [('host', 'localhost'), ('password', 'root'), ('user', 'root')]
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)
    # get section, default to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return db


if __name__ == "__main__":
    import doctest
    doctest.testmod()