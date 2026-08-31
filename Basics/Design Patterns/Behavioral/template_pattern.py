"""
Problem Statement

Imagine you are building a system that reads data from different file types like CSV, XML and JSON. Every file reader needs to follow the same basic process. Open the file read the content and close the file.

If you dont use the template method pattern you will end up writing the same opening and closing logic over and over again in each file reader class.

Problem in the code

1 - Repeated code : the open() and close() methods are written again in every single file reader class.
2 - Hard to maintain : if you need to modify the file open() and close() you have to update in all reader class separately which breaks DRY principle

"""

######### WITHOUT TEMPLATE PATTERN ###########
# class JSONParser:
#     def open(self):
#         print("opening json file")

#     def parse(self):
#         self.open()
#         print("parsing json file")
#         self.close()

#     def close(self):
#         print("closing json file")

# class CSVParser:
#     def open(self):
#         print("opening csv file")

#     def parse(self):
#         self.open()
#         print("parsing csv")
#         self.close()

#     def close(self):
#         print("closing the file")

# csv_parser = CSVParser()
# csv_parser.parse()
# json_parser = JSONParser()
# json_parser.parse()


########### WITH TEMPLATE PATTERN ############
from abc import ABC, abstractmethod
class DataParser(ABC):

    def template_parser(self):
        self.open()
        self.parse()
        self.close()

    def open(self):
        print("Opening the file")

    def close(self):
        print("Closing the file")

    @abstractmethod
    def parse(self):
        pass


class JSONParser(DataParser):
    def parse(self):
        print("Parsing json file")

class CSVParser(DataParser):
    def parse(self):
        print("Parsing csv file")


json_parser = JSONParser()
csv_parser = CSVParser()
json_parser.template_parser()
csv_parser.template_parser()