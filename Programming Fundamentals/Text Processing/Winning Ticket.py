def check_if_winner(ticketnum):
    cur_indx = 0
    maxrepcount = 0
    repetition = 0
    while cur_indx < len(ticketnum):
        if ticketnum[cur_indx] in ('@', '#', '$', '^'):
            cursymbol = ticketnum[cur_indx]
            repetition += 1
            cur_indx += 1
            for eachsym in ticketnum[cur_indx:]:
                if eachsym == cursymbol:
                    cur_indx += 1
                    repetition += 1
                    if cur_indx == 10:
                        maxrepcount[cursymbol] = repetition
                else:
                    maxrepcount[cursymbol] = repetition
                    repetition = 0
                    break
        else:
            cur_indx += 1

    for eachsymbol, occurrence in maxrepcount.items():
        if 6 <= occurrence < 10:
            return f'{ticketnum} - {occurrence} - {eachsymbol}'
        elif occurrence == 10:
            return f'{ticketnum} - {occurrence} - {eachsymbol}'
    return f'{ticketnum} no match'


uinput = input().split(',')

for eachticket in uinput:
    eachticket = eachticket.strip()
    if len(eachticket) == 20:
        result = ''
        first_half, second_half = eachticket[:10], eachticket[10:]
        res_first_half, res_second_half = check_if_winner(first_half), check_if_winner(second_half)
        if 'no match' in res_first_half or 'no match' in res_second_half:
            print(f'ticket "{eachticket}" - no match')
        elif res_first_half.split(' - ')[1] < res_second_half.split(' - ')[1]:
            print(f'ticket "{eachticket}" - {res_first_half.split(" - ")[1]}{res_first_half.split(" - ")[2]}')
        elif res_first_half.split(' - ')[1] > res_second_half.split(' - ')[1]:
            print(f'ticket "{eachticket}" - {res_second_half.split(" - ")[1]}{res_second_half.split(" - ")[2]}')
        else:
            if int(res_first_half.split(" - ")[1]) == 10:
                print(f'ticket "{eachticket}" - {res_first_half.split(" - ")[1]}{res_first_half.split(" - ")[2]} Jackpot!')
            else:
                print(f'ticket "{eachticket}" - {res_first_half.split(" - ")[1]}{res_first_half.split(" - ")[2]}')
    else:
        print('invalid ticket')
