while True:
    menber = int(input('กรุณาป้อนรหัสนักเรียน : '))
    score = int(input('กรุณาป้อนคะแนน 0 - 100 : '))

    if score >= 90:
        print('คุณรหัส %d ได้เกรด A ', menber)
        status = input('ต้องการคำนวณตัดเกรดใหม่หรือไม yes/no : ')
    elif score >= 80:
        print('คุณรหัส %d ได้เกรด B ', menber)
        status = input('ต้องการคำนวณตัดเกรดใหม่หรือไม yes/no : ')
    elif score >= 70:
        print('คุณรหัส %d ได้เกรด C ', menber)
        status = input('ต้องการคำนวณตัดเกรดใหม่หรือไม yes/no : ')
    elif score >= 60:
        print('คุณรหัส %d ได้เกรด D ', menber)
        status = input('ต้องการคำนวณตัดเกรดใหม่หรือไม yes/no : ')
    else:
        print('คุณรหัส %d ได้เกรด F ', menber)
        status = input('ต้องการคำนวณตัดเกรดใหม่หรือไม yes/no : ')

    if status == "no":
        break
# แบบที่ 1 *********************************************************************

while input('ต้องการคำนวณตัดเกรดใหม่หรือไม yes/no : ') == "yes":
    menber = int(input('กรุณาป้อนรหัสนักเรียน 6 หลัก : '))
    score = int(input('กรุณาป้อนคะแนน 0 - 100 : '))

    if score >= 90:
        print('คุณรหัส %d ได้เกรด A ' % menber)
    elif score >= 80:
        print('คุณรหัส %d ได้เกรด B ' % menber)
    elif score >= 70:
        print('คุณรหัส %d ได้เกรด C ' % menber)
    elif score >= 60:
        print('คุณรหัส %d ได้เกรด D ' % menber)
    else:
        print('คุณรหัส %d ได้เกรด F ' % menber)

# แบบที่ 2 *********************************************************************
status = None

while status not in ("yes", "no"):
    status = input("Enter yes or no : ")

    if status == "yes":
        menber = int(input('กรุณาป้อนรหัสนักเรียน 6 หลัก : '))
        score = int(input('กรุณาป้อนคะแนน 0 - 100 : '))

        if score >= 90:
            print('คุณรหัส %d ได้เกรด A ' % menber)
        elif score >= 80:
            print('คุณรหัส %d ได้เกรด B ' % menber)
        elif score >= 70:
            print('คุณรหัส %d ได้เกรด C ' % menber)
        elif score >= 60:
            print('คุณรหัส %d ได้เกรด D ' % menber)
        else:
            print('คุณรหัส %d ได้เกรด F ' % menber)

        status = None

    elif status == 'no':
        break

    else:
        print("Please enter yes or no.")

# แบบที่ 3 *********************************************************************

status = ['yes', 'y']

while input('ต้องการคำนวณตัดเกรดใหม่หรือไม yes/no : ').lower() in status :
    try:
        menber = int(input('กรุณาป้อนรหัสนักเรียน 6 หลัก : '))
        score = int(input('กรุณาป้อนคะแนน 0 - 100 : '))

        if score >= 90:
                print('คุณรหัส %d ได้เกรด A ' % menber)
        elif score >= 80:
                print('คุณรหัส %d ได้เกรด B ' % menber)
        elif score >= 70:
                print('คุณรหัส %d ได้เกรด C ' % menber)
        elif score >= 60:
                print('คุณรหัส %d ได้เกรด D ' % menber)
        else:
                print('คุณรหัส %d ได้เกรด F ' % menber)
    except ValueError:
        print('กรุณาป้อนรหัสนักเรียนและคะแนน')

# แบบที่ 4 *********************************************************************

status = ['yes', 'y']

while input('ต้องการคำนวณตัดเกรดใหม่หรือไม yes/no : ').lower() in status :
    try:
        menber = int(input('กรุณาป้อนรหัสนักเรียน 6 หลัก : '))
        score = int(input('กรุณาป้อนคะแนน 0 - 100 : '))

        if score >= 90:
                print('คุณรหัส %d ได้เกรด A ' % menber)
        elif score >= 80:
                print('คุณรหัส %d ได้เกรด B ' % menber)
        elif score >= 70:
                print('คุณรหัส %d ได้เกรด C ' % menber)
        elif score >= 60:
                print('คุณรหัส %d ได้เกรด D ' % menber)
        else:
                print('คุณรหัส %d ได้เกรด F ' % menber)
    except ValueError:
        print('กรุณาป้อนรหัสนักเรียนและคะแนน')

# แบบที่ 5 *********************************************************************

status = ['yes', 'y']

while input('ต้องการคำนวณตัดเกรดใหม่หรือไม yes/no : ').lower() in status:

    menber = int(input('กรุณาป้อนรหัสนักเรียน 6 หลัก : '))
    score = int(input('กรุณาป้อนคะแนน 0 - 100 : '))

    if score >= 90:
        print('คุณรหัส %d ได้เกรด A ' % menber)
    elif score >= 80:
        print('คุณรหัส %d ได้เกรด B ' % menber)
    elif score >= 70:
        print('คุณรหัส %d ได้เกรด C ' % menber)
    elif score >= 60:
        print('คุณรหัส %d ได้เกรด D ' % menber)
    else:
        print('คุณรหัส %d ได้เกรด F ' % menber)

# แบบที่ 6 *********************************************************************

status = ['no', 'n']

while True:

    menber = int(input('กรุณาป้อนรหัสนักเรียน 6 หลัก : '))
    score = int(input('กรุณาป้อนคะแนน 0 - 100 : '))

    if score >= 90:
        print('คุณรหัส %d ได้เกรด A ' % menber)
    elif score >= 80:
        print('คุณรหัส %d ได้เกรด B ' % menber)
    elif score >= 70:
        print('คุณรหัส %d ได้เกรด C ' % menber)
    elif score >= 60:
        print('คุณรหัส %d ได้เกรด D ' % menber)
    else:
        print('คุณรหัส %d ได้เกรด F ' % menber)

    if input('ต้องการคำนวณตัดเกรดใหม่หรือไม yes/no : ').lower() in status :
        break
    else:
        continue

# แบบที่ 7 *********************************************************************