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
            exit()
        else:
            exit()

    def open_diary():
        nonlocal journal
        username = user_input("Put in Your Username -> ")
        password = user_input("Put in Your Password -> ")
        if len(username) < 6:
            display("Username must be six characters or more than")
            open_diary()
        if len(password) < 6:
            display("Password must be six characters or more than")
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

    def exit():
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
            exit()
        else:
            user_menu()

    def gist_us():
        title = user_input("What's the title-> ")
        body = user_input("What the gist-> ")
        validate(title, body)
        display(title + "\n" + body + "\n" + "Gist saved successfully")
        user_menu()

    def validate(title, body):
        if len(title) < 6:
            display("Username must be six characters or more than")
            open_diary()
        if len(title) < 6:
            display("Password must be six characters or more than")
            open_diary()
        else:
            journal.createEntry(title, body)

    def find_your_gist():
        identity = user_input("Put in your ID: ")
        username = user_input("Put in your username: ")
        if not identity.isdigit():
            display("Invalid Id")
            find_your_gist()
            raise ValueError("This ID doesn't exist")
        else:
            diary = diaries.findByUsername(username)
            entry = diary.findEntryById(int(identity))
            display(entry.getEntry())
            user_menu()

    def delete_your_gist():
        identity: str = user_input("Put in your ID: ")
        username = user_input("Put in username: ")
        password = user_input("Put in your password: ")
        diary = diaries.findByUsername(username)
        diary.deleteEntry(int(identity))
        diaries.deleteDiary(username, password)

    def add_to_gist():
        identity: str = user_input("Put in your ID: ")
        title: str = user_input("What is the Title of your new gist: ")
        body: str = user_input("Gist us: ")
        journal.updateEntry(int(identity), title, body)
        display(title + '\n' + body + "\n" + "Successfully saved :)")

    user_menu()


if __name__ == "__main__":
    main()
