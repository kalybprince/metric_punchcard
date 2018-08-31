import os

def main():
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
                total_hours = sum(calculated_times)
                clear
                print('Total hours:', total_hours)
                subtract_response = str(input('\nCalculate remaining time/overtime? '))
                if subtract_response.startswith('y'):
                    hours_to_go = total_hours - 40
                    if hours_to_go < 0:
                        print('Hours left: {}'.format(40 - total_hours))
                    elif hours_to_go > 0:
                        print('Overtime: {}'.format(hours_to_go))
                    elif hours_to_go == 0:
                        print('You have exactly 40 hours!')
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

if __name__ == '__main__':
    main()
