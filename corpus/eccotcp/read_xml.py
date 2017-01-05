"""
This is the "read_xml" module.

The read_xml module supplies multiple function for unzip, read and store XML files from the ECCO-TCP Dataset
"""
from zipfile import ZipFile
import os


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
    IOError: The dataset directory doesn't exist
    """
    if not files_actually_unziped(origin_directory, destination_directory):
            for file in os.listdir(origin_directory):
                if file.endswith(".zip"):
                    ZipFile(os.path.join(origin_directory, file)).extractall(destination_directory)


def files_actually_unziped(origin_directory, destination_directory):
    """
    Verifies if the origin_directory with zipped files are actually unzipped. If files are unzipped, return True.
    Returns False otherwise. If the origin_directory doesn't exist an IOError is raised.
    :param origin_directory: The directory's path where ECCO-TCP zip files are stored
    :param destination_directory: The directory's path where the ECCO-TCP dataset will be unzipped
    :return: True or False
    >>> files_actually_unziped("/home/jrobledo/foo","/home/jrobledo/bar")
    Traceback (most recent call last):
        ...
    IOError: The dataset directory doesn't exist
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


if __name__ == "__main__":
    import doctest
    doctest.testmod()