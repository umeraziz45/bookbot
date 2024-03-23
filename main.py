def main():
     book_path='books/frankenstein.txt'
     text = get_book_text(book_path)
     wc = word_count(text)
     
     print(word_check(text))
    

def get_book_text(path):
     with open(path) as f:
        return f.read()

def word_count(stuff):
     word_list = stuff.split()
     return len(word_list)

def word_check(book):
     book_dict = {}
     for letter in book:
         # print(word)
          lowered_string = letter.lower()
          if lowered_string in book_dict:
               book_dict[lowered_string] += 1
          else:
               book_dict[lowered_string] = 1
     return book_dict

main()