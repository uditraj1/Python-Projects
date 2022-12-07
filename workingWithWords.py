""" Retrieve and print words """

from urllib.request import urlopen
def fetch_words():
    """ Fetches a list of letters """
    story = '''Hi.
    My name is Udit.
    How are you?'''
    story_words = []
    for line in story:
        story_words.append(line)

    return story_words

def print_items(items):
    """ Prints one letter per line """
    for item in items:
        print(item)

def main():
    """ The main for printing letters """
    words = fetch_words()
    print_items(words)

if __name__ == '__main__':
    main()
    
