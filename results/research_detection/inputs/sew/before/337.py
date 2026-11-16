import  re
def text_match_word(text):
        patterns = '\w+\S*$'
        if not re.search(patterns,  text):
                return 'Not matched!'
        else:
                return 'Found a match!'
