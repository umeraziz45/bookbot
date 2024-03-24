def main():
     book_path='books/frankenstein.txt'
     text = get_book_text(book_path)
     wc = word_count(text)
     
     word_dict = word_check(text)
     sorted_report = dict_to_list(word_dict)

     print_report(sorted_report, wc)
    

def get_book_text(path):
     with open(path) as f:
        return f.read()

def word_count(stuff):
     word_list = stuff.split()
     return len(word_list)

def word_check(book):
     book_dict = {}
     for letter in book:
         
          lowered_string = letter.lower()
          if lowered_string in book_dict:
               book_dict[lowered_string] += 1
          else:
               book_dict[lowered_string] = 1
     return book_dict

def sort_on(dict):
     for item in dict:
          return dict[item]

def dict_to_list(char_dict):
     word_list = []
     
     for item, value in char_dict.items():
          if item.isalpha():
               word_list.append({item:value})

     word_list.sort(reverse=True, key=sort_on) 

     return word_list

def print_report(sorted_list, wc):
   print(f'--- Begin report of books/frankenstein.txt ---')
   print(f'{wc} words found in the document')

   for item in sorted_list:
     for key, value in item.items():
           print(f'The \"{key}\" character was found {value} times')
   print('--- End report ---')


main()