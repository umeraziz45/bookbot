import sys
from stats import get_book_text, character_count, sorted_list,print_function

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    
    text = get_book_text(sys.argv[1])
    word_count = len(text.split())
    char_count = character_count(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f'Found {word_count} total words')
    print("--------- Character Count -------")
    print_function(sorted_list(char_count))
    print("============= END ===============")


main()
    
