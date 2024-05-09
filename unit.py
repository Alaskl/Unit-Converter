
# menu

def print_menu():
    print('Welcome to this garbage')
    print('Kilometers to Miles')
    print('Miles to Kilometers')

#user input (km to mi)

def km_miles():
    km = float(input('Enter the kilometer value:'))
    print('Miles:'.format(km))
    miles = km/1.609
    print(miles)

#user input (mi to km)

def miles_km():
    miles = float(input('Enter the mile value')) 
    print('Kilometers:'.format(miles))
    km = miles * 1.609
    print(km)

print_menu()

option = input('choose between A (km to miles) or B (miles to km)')

if option == 'A':
    km_miles()
if option == 'B':
    miles_km()
