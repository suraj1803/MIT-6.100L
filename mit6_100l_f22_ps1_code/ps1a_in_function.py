def part_a(yearly_salary, portion_saved, cost_of_dream_home):
	#########################################################################
	monthly_salary = yearly_salary / 12
	portion_down_payment = 0.25
	down_payment = cost_of_dream_home * portion_down_payment
	rate_of_interest = 0.05
	months = 0
	amount_saved = 0
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	while amount_saved < down_payment:
	    amount_saved += monthly_salary * portion_saved  + amount_saved * rate_of_interest / 12
	    months += 1
	print("Number of months:", months)
	return months