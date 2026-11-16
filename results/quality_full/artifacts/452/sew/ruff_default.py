def loss_amount(actual_cost, sale_amount):
    if not (sale_amount > actual_cost):
        return None
    else:
        amount = sale_amount - actual_cost
        return amount
