daily_slaes = [5 , 10 , 12 , 7 , 3 , 8 , 9 , 15]


total_cups = (sale for sale in daily_slaes if sale > 10)

print(list(total_cups))