import  re
def text_match_wordz_middle(text):
        patterns = '\Bz\B'
        if not re.search(patterns,  text):
                return('Not matched!')
        else:
                return 'Found a match!'
