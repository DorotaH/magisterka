def loss_amount(actual_cost, sale_amount):
	return sale_amount - actual_cost if sale_amount > actual_cost else None
