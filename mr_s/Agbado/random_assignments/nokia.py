def main_menu():
    menu = (input("select from menu: "))
    if menu == '1':
        phonebook()
    if menu == '2':
        message()
    if menu == '3':
        chat()
    if menu == '4':
        call_register()
    if menu == '5':
        tone()
    if menu == '6':
        settings()
    if menu == '7':
        call_divert()
    if menu == '8':
        games()
    if menu == '9':
        calculator()
    if menu == '10':
        reminders()
    if menu == '11':
        clock()
    if menu == '12':
        profiles()
    if menu == '13':
        sim_services()
    if menu == '0':
        leave()
    if menu > '0' or menu < '13':
        print('invalid input!!!')
        off_on()
        main_menu()



def phonebook():
    print('''****************************
             Phonebook:
             \t1. Search\n
             \t2. Service Nos.\n
             \t3. Add name.\n
             \t4. Erase.\n
             \t5. Edit.\n
             \t6. Assign tone.\n
             \t7. Send b'/card.\n
             \t8. Options.>>\n
             \t9. Speed dials.\n
             \t10.Voice tags\n
             \t00.Main menu\n
             *****************************''')
    book = input('choose: ')
    if book == '1':
        print('No contact available yet')
        phonebook()
    if book == '2':
        print('Ops None found!')
        phonebook()
    if book == '3':
        print('Ops None found!')
        phonebook()
    if book == '4':
        print('Ops None found!')
        phonebook()
    if book == '5':
        print('Ops None found!')
        phonebook()
    if book == '6':
        print('Ops None found!')
        phonebook()
    if book == '7':
        print('Ops None found!')
        phonebook()
    if book == '8':
        print('Ops None found!')
        phonebook()
    if book == '9':
        print('Ops None found!')
        phonebook()
    if book == '10':
        print('Ops None found!')
        phonebook()
    if book == '00':
        off_on()
        main_menu()


def message():
    print(f'''Message;\n
            \t1. Write messages.\n
            \t2.Inbox.\n
            \t3. Outbox.\n
            \t4. Picture messages.\n
            \t5. Templates.\n
            \t6. Smileys.\n
            \t7. Message settings\n
            \t8. Go back''')
    text = input('>>> ')
    if text == '1':
        write_message()
        message()
    if text == '2':
        print('No message found yet!')
        message()
    if text == '3':
        print('Ops! nothing found here! ')
        message()
    if text == '4':
        print('Ops! nothing found here!')
        message()
    if text == '5':
        print('Ops! nothing found here!')
        message()
    if text == '6':
        print('Ops! nothing found here! ')
        message()
    if text == '7':
        print('Ops! nothing found here! ')
        message()
    if text == '0':
        off_on()
        main_menu()


def write_message():
    jot = input(f'''Choose a Template:
                 1. Hi lovely!
                 2. Am currently busy.
                 3. I'll reply shortly
                 4. Not available at the moment''')
    if jot <= '4':
        print("Message sent successfully! ")
        message()
    else:
        print('invalid input! ')
        message()


def chat():
    print('Ops! No chat found here!')
    off_on()
    main_menu()


def call_register():
    print('''Call register;\n1. Missed calls\n2. Received calls\n3. Dialled numbers\n4.Erase recent call lists.\n
5.Show calls duration.\n6.Show call costs\n7. Call cost settings.\n8. Prepaid credit.\n0. Go back''')
    register = input('>>> ')
    if register == '1':
        print("Nothing here! ")
        call_register()
    if register == '2':
        print("Nothing here! ")
        call_register()
    if register == '3':
        print("Nothing here! ")
        call_register()
    if register == '4':
        print("Nothing here! ")
        call_register()
    if register == '5':
        print("Nothing here! ")
        call_register()
    if register == '6':
        print("Nothing here! ")
        call_register()
    if register == '7':
        print("Nothing here! ")
        call_register()
    if register == '8':
        print("Nothing here! ")
        call_register()
    if register == '0':
        off_on()
        main_menu()


def tone():
    print(f'''1. Ringing tone
              2. Ringing volume
              3. Incoming call alert
              4. Composer
              5. Message alert tone
              6. Keypad tones
              7. Warning and game tones
              8. Vibrating alert
              9. Screen saver
              0. Go back ''')
    sound = input('>>> ')
    if sound == '1':
        ringing_tone()
        tone()
    if sound == '2':
        print('volume successfully set!')
        tone()
    if sound == '3':
        print('none found!')
        tone()
    if sound == '4':
        print('none found!')
        tone()
    if sound == '5':
        print('none found!')
        tone()
    if sound == '6':
        print('none found!')
        tone()
    if sound == '7':
        print('none found!')
        tone()
    if sound == '8':
        print('none found!')
        tone()
    if sound == '9':
        print('none found!')
        tone()
    if sound == '0':
        off_on()
        main_menu()


def ringing_tone():
    print('1. ding dong.\n2. waterfall.\n3. bell.\n4. nokia anthem')
    melody = input('>>> ')
    if melody == '1':
        print('ringtone successfully set!!!')
        ringing_tone()
    if melody == '2':
        print('ringtone successfully set!!!')
        ringing_tone()
    if melody == '3':
        print('ringtone successfully set!!!')
        ringing_tone()
    if melody == '4':
        print('ringtone successfully set!!!')
        ringing_tone()
    if melody == '0':
        tone()


def settings():
    print('1. Calling Settings.\n2. Phone Settings\n3. Security Settings\n4. Restore Factory Settings\n 00. Back')
    work_on = input('>>> ')
    if work_on == '1':
        call_settings()
    if work_on == '2':
        phone_settings()
    if work_on == '3':
        security_settings()
    if work_on == '4':
        restore_factory_setting()
    if work_on == '00':
        off_on()
        main_menu()


def call_settings():
    print('''1. Automatic redial
             2. Speed dialling
             3. Call waiting options
             4. Own number sending
             5. Phone line in use
             6. Automatic answer 
             0. Go back ''')
    call_set = input('>>> ')
    if call_set == '1':
        print('Done!')
        call_settings()
    if call_set == '2':
        print('Done!')
        call_settings()
    if call_set == '3':
        print('Done!')
        call_settings()
    if call_set == '4':
        print('Done!')
        call_settings()
    if call_set == '5':
        print('Done!')
        call_settings()
    if call_set == '6':
        print('Done!')
        call_settings()
    if call_set == '0':
        main_menu()


def phone_settings():
    print('''1. Language\n2. Cell info display\n3. Welcome note\n
4. Network selection\n5. Lights2\n6. Confirm SIM service actions''')
    setting = input('>>> ')
    if setting == '1':
        language()
    phone_settings()
    if setting == '2':
        print('Nothing to show')
    if setting == '3':
        print('Nothing to show')
    if setting == '4':
        print('Nothing to show')
    if setting == '5':
        print('Nothing to show')
    if setting == '6':
        print('Nothing to show')


def security_settings():
    print('''1. PIN code request\n2. Call barring service\n3. Fixed dialling\n
4. Closed user group\n5. Phone security\n6. Change access codes''')
    secure = input('>>> ')
    if secure == '1':
        print('Nothing is here')
        security_settings()
    if secure == '2':
        print('Nothing is here')
        security_settings()
    if secure == '3':
        print('Nothing is here')
        security_settings()
    if secure == '4':
        print('Nothing is here')
        security_settings()
    if secure == '5':
        print('Nothing is here')
        security_settings()
    if secure == '6':
        print('Nothing is here')
        security_settings()
    if secure == '0':
        settings()


def restore_factory_setting():
    print('phone reset successfully!!!')
    off_on()


def language():
    print('1. English.\n2. Yoruba.\n3. Hausa.\n4. Ibo.\n5. French.\n6. Spanish\n00. Back')
    tribe = input('>>> ')
    if tribe == '1':
        print('Successful!')
    if tribe == '2':
        print('Successful!')
    if tribe == '3':
        print('Successful!')
    if tribe == '4':
        print('Successful!')
    if tribe == '5':
        print('Successful!')
    if tribe == '6':
        print('Successful!')
    if tribe == '00':
        phone_settings()


def call_divert():
    print("Ops! nothing is found here")
    off_on()
    main_menu()


def games():
    print('1. Snake.\n2. Puzzle\n3. Sudoku\n00. Back')
    play = input('>>> ')
    if play == '1':
        print('Loading....')
        games()
    if play == '2':
        print('Loading....')
        games()
    if play == '3':
        print('Loading....')
        games()
    if play == '00':
        off_on()
        main_menu()


def calculator():
    print('Loading....')
    off_on()
    main_menu()


def reminders():
    print("Loading")
    off_on()
    main_menu()


def clock():
    print('''1. Alarm clock
             2. Clock settings
             3. Date setting
             4. Stopwatch
             5. Countdown timer
             6. Auto update of date and time
             00. Back ''')
    second = input('>>> ')
    if second == '1':
        print('Loading....')
        clock()
    if second == '2':
        print('Loading....')
        clock()
    if second == '3':
        print('Loading....')
        clock()
    if second == '4':
        print('Loading....')
        clock()
    if second == '5':
        print('Loading....')
        clock()
    if second == '6':
        print('Loading....')
        clock()
    if second == '00':
        off_on()
        main_menu()


def profiles():
    print('Ops! No profile yet')
    off_on()
    main_menu()


def sim_services():
    print('No sim found')
    off_on()
    main_menu()


def leave():
    SystemExit(0)


def off_on():
    print("****************************************")
    print("****************************************")
    print("*************** NOKIA 3310 *************")
    print("****************************************")
    print("****************************************")
    print(f'''Multiple Choice:\n1. Phonebook\n2. Message\n3. Chat\n4. Call register\n5. Tone\n6. Settings
7. Call divert\n8. Games\n9. Calculator\n10. Reminders\n11. Clock\n12. Profiles\n13. SIM services\n0. Exit''')


print("Press 1 tO On and 0 to exit")
on = input('>>> ')
if on == '1':
    off_on()
main_menu()
if on == '0':
    SystemExit(0)
else:
    print('invalid input!')

