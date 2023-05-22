class Book():
    file_name = ''
    file_data = []
    total_page = 0
    def __init__(self, file_name):
        self.file_name = file_name

    def read_book(self):
        file = open(self.file_name, "r")
        self.file_data = file.read().split("--")
        self.total_page = len(self.file_data)


    def display_book(self, page_no=1):
        page_no = page_no
        while True:
            print()
            print(self.file_data[page_no-1])
            value = input('\nShowing page ' + str(page_no) + " of " + str(self.total_page) + " pages [Enter - read more, press q to quit]")
            print()
            if value == "":
                if page_no == self.total_page:
                    print("***Same page showing. No next page**")
                else:
                    page_no += 1
            elif value == 'q':
                break
            


file_text="This is first page content.\nWrite a program to display a simple form of digital book. “Books” are text files in which each block (page) of text is followed by a double dash. When a book is displayed, the first block of text is shown and the program should wait for the user to press the enter key before displaying the next.--Now we are in the second page.\nExtend the previous challenge so that it is possible to skip forward by an arbitrary number of pages. This should be achieved by allowing the user to enter a number before pressing the enter key.--This is the 3rd page.\nExtend the previous challenge so that it is possible to skip forward by an arbitrary number of pages. This should be achieved by allowing the user to enter a number before pressing the enter key--Now, it is page no 4.\nExtend the previous challenge so that it is possible to skip forward by an arbitrary number of pages. This should be achieved by allowing the user to enter a number before pressing the enter key. If the number is positive, the given number of pages are skipped. If there is no number, the next page is displayed. If the number is positive, the given number of pages are skipped.--This is page-5 and the last page of this book.\nIf there is no number, the next page is displayed. Further extend the book reader so that it can accept negative numbers for skipping pages. Entering -1 should go back to the previous page. There are many ways to achieve this."
f = open("text_file.txt", "w")
f.write(file_text)
f.close()
my_book = Book("text_file.txt")
my_book.read_book()
my_book.display_book()