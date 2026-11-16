def profit_amount(actual_cost, sale_amount):
    if not (actual_cost > sale_amount):
        return None
    amount = actual_cost - sale_amount
    return amount
