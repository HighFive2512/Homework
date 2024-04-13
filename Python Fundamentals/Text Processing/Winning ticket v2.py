def check_if_winning_ticket(ticket):
    ticket = ticket.strip()
    if len(ticket) != 20:
        return "invalid ticket"
    firsthalf = ticket[:10]
    secondhalf = ticket[10:]
    for eachsymbol in ("@", "#", "$", "^"):
        for eachindx in range(10, 5, -1):
            repetition = eachindx * eachsymbol
            if repetition in firsthalf and repetition in secondhalf:
                if len(repetition) == 10:
                    return f'ticket "{ticket}" - {len(repetition)}{eachsymbol} Jackpot!'
                elif len(repetition) != 10:
                    return f'ticket "{ticket}" - {len(repetition)}{eachsymbol}'

    return f'ticket "{ticket}" - no match'


uinput = input().split(",")
for eachword in uinput:
    print(check_if_winning_ticket(eachword))
