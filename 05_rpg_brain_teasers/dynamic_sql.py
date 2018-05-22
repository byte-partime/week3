
class QueryBuilder(object):
    """docstring for QueryBuilder"""
    
    def __init__(self):
        self.rules = {
            'city': 'city = {}',
            'state': 'state = {}',
            'min_price': 'price >= {}'
        }


    def build_listings_query(params):
        query = "select * from listings"

        if len(params) == 0:
            return query
        elif len(params) > 10:
            print("I am greater than 10")
        elif len(params) < 10:

        else:


    








        