import  re
def text_match_one(text):
        patterns = 'ab+?'
        if not re.search(patterns,  text):
                return('Not matched!')
        else:
                return 'Found a match!'
