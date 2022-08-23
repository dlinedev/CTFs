from ast import While
from pwn import *

def game(round):
    correct_count = 0
    month = round[0]
    day = int(round[1])
    while True:
        if month == 'January':
            ChooseMonth(day)
        else:
            ChooseDay(month, day)
        proc.clean()
        next = proc.recvline().strip()
        if str(next).find("You won")>1:
            print('-------------yes----------------')
            correct_count +=1
            if correct_count >= 100:
                while True:
                    print(str(proc.recvline()).replace("\\n", ""))
            print(str(proc.recvline()).replace("\\n", ""))
            print(str(proc.recvline()).replace("\\n", ""))
            print(str(proc.recvline()).replace("\\n", ""))
            next = proc.recvline().strip()
        print(str(next).replace("\\n", ""))
        next_split = str(next).replace("b'", "").replace("> ", "").replace("'", "").replace("\\n'", "").split(' ',2)
        month = next_split[0]
        day = int(next_split[1])

def ChooseDay(month, day):
    if month == 'February' and day < 20:
        proc.sendline("February 20".encode())
        print('February 20')
    elif month == 'February'and day < 21:
        proc.sendline("February 21".encode())
        print('February 21')
    elif month == 'March' and day < 22:
        proc.sendline("March 22".encode())
        print('March 22')
    elif month == 'April'and day < 23:
        proc.sendline("April 23".encode())
        print('April 23')
    elif month == 'May'and day < 24:
        proc.sendline("May 24".encode())
        print('May 24')
    elif month == 'June'and day < 25:
        proc.sendline("June 25".encode())
        print('June 25')
    elif month == 'July'and day < 26:
        proc.sendline("July 26".encode())
        print('July 26')
    elif month == 'August'and day < 27:
        proc.sendline("August 27".encode())
        print('August 27')
    elif month == 'September'and day < 28:
        proc.sendline("September 28".encode())
        print('September 28')
    elif month == 'October'and day < 29:
        proc.sendline("October 29".encode())
        print('October 29')
    elif month == 'November'and day < 30:
        proc.sendline("November 30".encode())
        print('November 30')
    elif month == 'December'and day < 31:
        proc.sendline("December 31".encode())
        print('December 31')   
    else:
        ChooseMonth(day)

def ChooseMonth(day):
    if day < 20:
        proc.sendline("January 20".encode())
        print('January 20')
    if day == 20:
        proc.sendline("February 20".encode())
        print('February 20')
    if day == 21:
        proc.sendline("February 21".encode())
        print('February 21')
    if day == 22:
        proc.sendline("March 22".encode())
        print('March 22')
    if day == 23:
        proc.sendline("April 23".encode())
        print('April 23')
    if day == 24:
        proc.sendline("May 24".encode())
        print('May 24')
    if day == 25:
        proc.sendline("June 25".encode())
        print('June 25')
    if day == 26:
        proc.sendline("July 26".encode())
        print('July 26')
    if day == 27:
        proc.sendline("August 27".encode())
        print('August 27')
    if day == 28:
        proc.sendline("September 28".encode())
        print('September 28')
    if day == 29:
        proc.sendline("October 29".encode())
        print('October 29')
    if day == 30:
        proc.sendline("November 30".encode())
        print('November 30')
    if day == 31:
        proc.sendline("December 31".encode())
        print('December 31')   

while True:
    proc = remote('neoannophobia.chal.imaginaryctf.org', 1337)
    response = proc.recvline()
    stopsign = 0
    round1 = ''
    while stopsign != 1:
        startText = proc.recvline()
        print(str(startText).replace("\\n", ""))
        if str(startText).find('ROUND 1')>1:
            stopsign = 1
            print(str(proc.recvline()).replace("\\n", ""))
            round1 = proc.recvline()
            print(round1)
            break
    round1 = str(round1).replace("b'", "").replace("\\n'", "").split(' ',1)
    print('--------------------------------')
    game(round1)
    exit()

