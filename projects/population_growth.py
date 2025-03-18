# Population Growth Calculator
#Write the necessary code to display the total population count for the next 3 years (without a leap year).

#Here are the specifications:

#In the country we want to investigate:

#- The current population is 380,123,456
#- One person is born every 6 seconds
#- One person dies every 12 seconds
#- One person immigrates every 40 seconds 

current = 380123456
born = 6
dies = 12
immigrate = 40

three_years = 365*24*60*60
born_three_years = three_years/born 
dies_three_years = three_years/ dies
immigrate_three_years = three_years/immigrate
total_population = current + born_three_years - dies_three_years + immigrate_three_years
print(total_population)