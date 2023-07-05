def demo_menu():
    main_menu = (f'''\t\t\t\t 1. Phonebook
                     2. Message
                     3. Chat
                     4. Call register
                     5. Tones
                     6. Settings
                     7. Call divert
                     8. Games
                     9. Calculator
                     10. Reminders
                     11. Clock
                     12. Profiles
                     13. SIM services''')
    print(f" <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print(f" <<<<<<<<<<<<<<<< Welcome to Nokia 3310 >>>>>>>>>>>>>>>\n {main_menu}")
    print(f" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    menu_list = input("Press 0 to select: ")
    demo_menu()
    if menu_list == "1":
        demo_phonebook()
    if menu_list == "2":
        demo_message()
    if menu_list == "3":
        demo_chat()
    if menu_list == "4":
        demo_call_register()
    if menu_list == "5":
        demo_tones()
    if menu_list == "6":
        demo_settings()
    if menu_list == "7":
        demo_call_divert()
    if menu_list == "8":
        demo_games()
    if menu_list == "9":
        demo_calculator()
    if menu_list == "10":
        demo_reminders()
    if menu_list == "11":
        demo_clock()
    if menu_list == "12":
        demo_profiles()
    if menu_list == "13":
        demo_sim_services()


def demo_phonebook():
    print(
        f"Phonebook: Phonebook:\n1. Search\n2. Service Nos.\n3. Add name\n4. Erase\n5. Edit.\n6.Assign tone.\n7. Send "
        f"b'/card.\n8. Options.\n9. Speed dials.\n10.Voice tags ")


demo_phonebook_list = input("Select a menu: ")
if demo_phonebook_list == "0":
    demo_menu()


def demo_message():
    print(f''' Message;             
             1. Write messages.      
             2.Inbox.                
             3. Outbox.              
             4. Picture messages.    
             5. Templates.           
             6. Smileys.             
             7. Message settings''')


demo_phonebook_list = input("Select a menu: ")
if demo_phonebook_list == "0":
    demo_menu()


def demo_chat():
    print("3. Chat")


demo_phonebook_list = input("Select a menu: ")
if demo_phonebook_list == "0":
    demo_menu()


def demo_call_register():
    print(f'''Call register;       
   1. Missed calls.               
   2. Received calls.             
   3. Dialled numbers.            
   4.Erase recent call lists.     
   5.Show calls duration.         
   6.Show call costs.             
   7. Call cost settings.         
   8. Prepaid credit.''')


demo_phonebook_list = input("Select a menu: ")
if demo_phonebook_list == "0":
    demo_menu()


def demo_tones():
    print(f'''Tones;       
         1. Ringing Tone.           
         2. Ringing volume.         
         3. Incoming call alert.    
         4. Composer.               
         5. Message alert tone.     
         6. Keypad tones.           
         7. Warning and game tones. 
         8. Vibrating alert.        
         9. Screen saver''')


demo_phonebook_list = input("Select a menu: ")
if demo_phonebook_list == "0":
    demo_menu()


def demo_settings():
    print(f'''Settings             
       1. Call settings.                  
       2. Phone settings.                 
       3. Security settings.              
       4. Restore factory settings.''')


demo_phonebook_list = input("Select a menu: ")
if demo_phonebook_list == "0":
    demo_menu()


def demo_call_divert():
    print("7. Call divert")


demo_phonebook_list = input("Select a menu: ")
if demo_phonebook_list == "0":
    demo_menu()


def demo_games():
    print("8. Games")


demo_phonebook_list = input("Select a menu: ")
if demo_phonebook_list == "0":
    demo_menu()


def demo_calculator():
    print("9. Calculator")


demo_phonebook_list = input("Select a menu: ")
if demo_phonebook_list == "0":
    demo_menu()


def demo_reminders():
    print("10. Reminders")


demo_phonebook_list = input("Select a menu: ")
if demo_phonebook_list == "0":
    demo_menu()


def demo_clock():
    print(f'''Clock;                   
           1. Alarm clock.                        
           2. Clock settings.                     
           3. Date setting.                       
           4. Stopwatch.                          
           5. Countdown timer.                    
           6. Auto update of date and time.''')


demo_phonebook_list = input("Select a menu: ")
if demo_phonebook_list == "0":
    demo_menu()


def demo_profiles():
    print("12. Profiles")


demo_phonebook_list = input("Select a menu: ")
if demo_phonebook_list == "0":
    demo_menu()


def demo_sim_services():
    print("13. SIM services")


demo_phonebook_list = input("Select a menu: ")
if demo_phonebook_list == "0":
    demo_menu()
