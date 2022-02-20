x = input('Идет ли дождь? ').lower()
if x == 'yes':
    a = input('Ветрено ли на улице? ').lower()
    if a == 'yes':
        print('It is too windy for an umbrella')
    else:
        print('Take an umbrella')
else:
    print('Enjoy your day')

