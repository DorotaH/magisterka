from operator import itemgetter
def index_on_inner_list(list_data, index_no):
    return sorted(list_data, key=itemgetter(index_no))