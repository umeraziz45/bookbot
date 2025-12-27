def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        
    return file_contents

def character_count(text):
    text = text.lower()
    count = {}
    for character in text:
        if character in count:
            count[character] += 1
        else:
            count[character] = 1
    return count

def sort_helper(obj):
    return obj['num']


def sorted_list(obj):
    final_list = []
    for item in obj:
        final_list.append({"char": item, "num": obj[item]})
    final_list.sort(reverse = True, key = sort_helper)
    return final_list

def print_function(items):
    for obj in items:
        if obj['char'].isalpha():
            print(f'{obj["char"]}: {obj["num"]}')
        else:
            continue


