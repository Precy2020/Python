from Diary_series.diaries import Diaries
from Diary_series.diary import Diary


def main():
    diaries = Diaries()
    journal = Diary("username", "password")

    def user_input(prompt):
        return input(prompt)

    def display(message):
        print(message)

    def main_menu():
        mainMenu = """   
                        )(=)(=)(=)(=)(=)(=)(=)(=)
                        A Beautiful Day to you :)
                        Welcome to La'mour Diary

                        <1> Open Diary
                        <2> Login
                        <3> Exit

                        )(=)(=)(=)(=)(=)(=)(=)(=)
                        """
        userResponse = user_input(mainMenu)
        if userResponse == "1":
            open_diary()
        elif userResponse == "2":
            login()
        elif userResponse == "3":
            exit_program()
        else:
            exit_program()

    def open_diary():
        nonlocal journal
        username = user_input("Put in Your Username -> ")
        password = user_input("Put in Your Password -> ")
        if len(username) < 6 or len(password) < 6:
            display("Username and password must be six characters or more.")
            open_diary()
        else:
            diaries.add(username, password)
            display("Congrats " + username + " :) you just got registered successfully!")
            user_menu()

    def login():
        nonlocal journal
        username = user_input("Enter your Username:= ")
        password = user_input("Enter your Password:= ")
        diary = diaries.findByUsername(username)
        if diary and diary.getPassword() == password:
            display("Hello " + diary.getUsername() + " great to have you back here :)")
            user_menu()
        else:
            display(":( Username or Password not found!")

    def exit_program():
        return

    def user_menu():
        memberMenu = """ 
                             |o|o|o|o|o|o|o|o|o|o|
                             1_ Gist us
                             2_ Find your gist
                             3_ Delete your gist
                             4_ Add to gist
                             5_ Exit
                             |o|o|o|o|o|o|o|o|o|o|
                            """
        userResponse = user_input(memberMenu)
        if userResponse == "1":
            gist_us()
        elif userResponse == "2":
            find_your_gist()
        elif userResponse == "3":
            delete_your_gist()
        elif userResponse == "4":
            add_to_gist()
        elif userResponse == "5":
            exit_program()
        else:
            user_menu()

    def gist_us():
        title = user_input("What's the title-> ")
        body = user_input("What the gist-> ")
        _validate(title, body)
        display(title + "\n" + body + "\n" + "Gist saved successfully")
        user_menu()

    def _validate(title, body):
        if len(title) < 6 or len(body) < 6:
            display("Title and body must be six characters or more.")
            gist_us()
        else:
            try:
                journal.createEntry(title, body)
            except ValueError as e:
                display(str(e))
            user_menu()

    def find_your_gist():
        try:
            identity = user_input("Put in your ID: ")
            username = user_input("Put in your username: ")
        except ValueError:
            display("Invalid ID. Please enter a valid integer.")
            find_your_gist()
            return

        if not identity.isdigit():
            display("Invalid Id")
            find_your_gist()
            return

        try:
            diary = diaries.findByUsername(username)
            entry = diary.findEntryById(int(identity))
            display(entry.getEntry())
            user_menu()
        except ValueError as e:
            display(str(e))
            user_menu()

    def delete_your_gist():
        try:
            identity = int(user_input("Put in your ID: "))
            username = user_input("Put in username: ")
            password = user_input("Put in your password: ")
        except ValueError:
            display("Invalid input. Please enter valid values.")
            delete_your_gist()
            return

        try:
            diary = diaries.findByUsername(username)
            diary.deleteEntry(identity)
            diaries.deleteDiary(username, password)
            main_menu()
        except ValueError as e:
            display(str(e))
            main_menu()

    def add_to_gist():
        identity = user_input("Put in your ID: ")
        title = user_input("What is the Title of your new gist: ")
        body = user_input("Gist us: ")
        journal.updateEntry(int(identity), title, body)
        display(title + '\n' + body + "\n" + "Successfully saved :)")

    main_menu()


if __name__ == "__main__":
    main()
