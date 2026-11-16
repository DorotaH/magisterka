def profit_amount(actual_cost, sale_amount):
    if not (actual_cost > sale_amount):
        return None
    else:
        amount = actual_cost - sale_amount
        return amount
