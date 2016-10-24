#import getTimes
#import MENU_edit_2
import createNewDay2
#import dailyTimes



def beginMenu():
    print('What would you like to do: ')
    print('[n]: Create New Day')
    print('[e]: Edit Day')
    print('[d]: View Days Info')
    print('[w]: View weeks Info')

    while True:
        try:
            b = input('<<: ')


            if b == 'n':
                print('poop!')
                createNewDay2.getTimes()
                print('23 skidoo')
                break
            if b == 'e':
                print('shoop!')
#                MENU_edit_2.editMenu()
                break
            if b == 'd':
                print('boosh!')
#                dailyTimes.showDailyTimes()
                break
            if b == 'w':
                print('spoon!')
                break
            else:
                continue
        except ValueError:
            continue
        break

bM = beginMenu()
