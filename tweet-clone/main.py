from typing import Callable

from auth import login
from core import models
from core.db_settings import execute_query
from utils import menus


def show_auth_menu() -> Callable | None:
    """
    Show auth menu
    :return: function based on option
    """
    print(menus.auth_menu)
    option = input("Enter your option: ")
    if option == "1":
        if login.login():
            print("Welcome to main menu")
            return show_main_menu()
        print("Username or password is incorrect")

    elif option == "2":
        if login.register():
            print("Please login now")

    elif option == "3":
        if login.validate():
            print("Welcome to main menu")
            return show_main_menu()
    elif option == "4":
        print("Good bye")
        return None

    return show_auth_menu()


def show_all_tweets_menu() -> Callable:
    """
    Submenu for all tweets
    :return:
    """
    print(menus.all_tweets_menu)
    return show_all_tweets_menu()


def show_main_menu() -> Callable:
    """
    Show main menu to users
    :return: function based on option
    """
    print(menus.main_menu)
    option = input("Enter your option: ")
    if option == "1":
        # show all tweets function called
        return show_all_tweets_menu()

    return show_auth_menu()


if __name__ == '__main__':
    # create tables in here
    # execute_query(query=models.users)
    # execute_query(query=models.tweets)
    # execute_query(query=models.likes)
    execute_query(query=models.codes)
    show_auth_menu()