from time import gmtime, strftime
import re


def tools_gentimestamp():
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())  # timestamp in format YYYY-MM-DD HH:MM:SS


def tools_get_tags_from_msg(msg):  # extract tags from a message
    return re.findall('#(\S+)', msg)


def tools_get_tags_from_file():
    pass


def write(message, path='D:\\Programming\\Python\\Toy_Note\\test.txt'):
    """ append file with message and timestamp """
    file = open(path, 'a')
    timestamp = tools_gentimestamp()
    file.write(timestamp + '\t' + message + '\n')
    file.close()


def loadfile(path='D:\\Programming\\Python\\Toy_Note\\test.txt'):   # loads note into memory
    file = open(path, 'r')
    file_content = file.read()
    file.close()
    return file_content


def load(path='D:\\Programming\\Python\\Toy_Note\\test.txt'):
    """ Load datafile into string """

    file = open(path, 'r')
    file_content = file.read()
    file.close()
    return file_content



