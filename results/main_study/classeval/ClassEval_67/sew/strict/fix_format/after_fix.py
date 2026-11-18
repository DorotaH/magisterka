class  Order:

    def __init__(self):
        self.menu=list()
        # menu = [{"dish": dish name, "price": price, "count": count}, ...]
        self.selected_dishes=list()
        # selected_dish = {"dish": dish name, "count": count, price: price}
        self.sales=dict()
        #


    def add_dish(self, dish):
        for menu_dish in self.menu:
            if  dish["dish"] == menu_dish["dish"]:
                if not menu_dish["count"] < dish["count"]:
                    menu_dish["count"] -= dish["count"]
                    break
                else:
                    return False
        self.selected_dishes.append(dish)
        return  True
    def calculate_total(self):
        total=0
        for dish in self.selected_dishes:
            total += dish["price"] * dish["count"] * self.sales[dish["dish"]]
        return  total
    def checkout(self):
        if  len(self.selected_dishes) == 0:
            return  False
        total=self.calculate_total()
        self.selected_dishes=list()
        return  total
