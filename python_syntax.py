a=input('Enter your monthly income. ')
b=input('Enter your total monthly expenses. ')
monthly_saving= int(a) - int(b)
projected_saving=monthly_saving * 12 + (monthly_saving * 12 * 0.05)


print('your monthly saving is ', monthly_saving)
print("your anual saving with 5% intersest is", projected_saving)