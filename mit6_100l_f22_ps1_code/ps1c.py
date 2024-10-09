## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
house_cost = 800000
portion_down_payment = 0.25
down_payment = house_cost * portion_down_payment

lower = 0.0
upper = 1.0
gap = 100
months = 36
steps = 0


if initial_deposit >= down_payment - gap:
    r = 0.0
else:
    while upper - lower > 1e-6:
        mid = (lower + upper) / 2
        amount_saved = initial_deposit
        for month in range(months):
            amount_saved += amount_saved * (mid / 12)

        if abs(amount_saved - down_payment) <= gap:
            r = mid
            break
        elif amount_saved < down_payment:
            lower = mid
        else:
            upper = mid

        steps += 1

    if abs(amount_saved - down_payment) > gap :
        r = None

print("Best savings rate:", r)
print("Steps in bisection search:",steps)
