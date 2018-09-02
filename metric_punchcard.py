import os
from datetime import date


def main(): # returns a list containing all calculated times
    calculated_times = []
    clear = os.system('clear')
    clear
    print('Input example: 16.00 == 4:00pm\nDay: 1')
    while True:
        try:
            time_in = round(float(input('Time in: ')), 2)
            time_out = round(float(input('Time out: ')), 2)
            time_calc = time_out - time_in
            calculated_times.append(time_calc)
            if len(calculated_times) == 14:
                total_hours = round(sum(calculated_times), 2)
                clear
                print('Total hours:', total_hours)
                subtract_response = str(input('\nCalculate remaining time/overtime? '))
                if subtract_response.startswith('y'):
                    if total_hours < 80:
                        print('Hours left: {}'.format(80 - total_hours))
                    elif total_hours > 0:
                        print('Overtime: {}'.format(total_hours - 80))
                    elif total_hours == 0:
                        print('You have exactly 80 hours!')
                    else:
                        print('There was an issue calculating your hours...')
                elif subtract_response.startswith('n'):
                    break
                else:
                    break
                break
            else:
                print('Day:{}'.format(len(calculated_times) + 1))
                continue
        except Exception as err:
            clear
            print('There was an error (most likely a value error: {}'.format(err))
    clear
    return calculated_times

def formatter(calculated_times):
    try:
        current_date = date.today()
        total_hours = round(sum(calculated_times), 2)
        write_data = "{}: total hours: {} {}".format(current_date, total_hours, calculated_times)
        with open('workfile.txt', 'w') as f:
            f.write(write_data)
    except Exception as err:
        print('Debug:', err)

if __name__ == '__main__':
    times_list = main()
    formatter(times_list)
