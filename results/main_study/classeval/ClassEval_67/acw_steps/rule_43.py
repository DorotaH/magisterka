class Order:

    def __init__(self):
        self.menu = []
        # menu = [{"dish": dish name, "price": price, "count": count}, ...]
        self.selected_dishes = []
        # selected_dish = {"dish": dish name, "count": count, price: price}
        self.sales = {}
        # 


    def add_dish(self, dish):
        for menu_dish in self.menu:
            if dish["dish"] == menu_dish["dish"]:
                if dish["count"] > menu_dish["count"]:
                    return False
                menu_dish["count"] -= dish["count"]
                break
        self.selected_dishes.append(dish)
        return True

    def calculate_total(self):
        return sum(
            dish["count"] * dish["price"] * self.sales[dish["dish"]]
            for dish in self.selected_dishes
        )

    def checkout(self):
        if len(self.selected_dishes) == 0:
            return False
        total = self.calculate_total()
        self.selected_dishes = []
        return total
