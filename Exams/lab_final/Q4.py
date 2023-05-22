week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
rainfall_list = []
min_rainfall = 100000000
max_rainfall = 0
min_rainfall_day = ''
max_rainfall_day = ''

for day in week:
    rainfall = float(input(f'Enter the rainfall of {day}: '))
    rainfall_list.append(rainfall)

    if min_rainfall > rainfall:
        min_rainfall = rainfall
        min_rainfall_day = day

    if max_rainfall < rainfall:
        max_rainfall = rainfall
        max_rainfall_day = day


print(f'\nThe minimum rainfall of the week was {min_rainfall} mm on {min_rainfall_day}.')
print(f'The maximum rainfall of the week was {max_rainfall} mm on {max_rainfall_day}.')

mean = round(sum(rainfall_list)/len(rainfall_list), 3)
print(f'The Mean or average rainfall of the week was {mean} mm.')

squared_deviation = []
for rainfall in rainfall_list:
    squared_deviation.append((mean - rainfall) ** 2)

standard_deviation = round((sum(squared_deviation)/len(rainfall_list)) ** (1/2), 3)
print(f'The Standard Deviation of the rainfall of the week was {standard_deviation} mm.')

