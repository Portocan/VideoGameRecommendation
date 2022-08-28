from data import *
from linkedlist import LinkedList


def insert_game_types():  # insert game types into linked list
    game_type_list = LinkedList()
    for game_type in types:
        game_type_list.insert_beginning(game_type)
    return game_type_list


def insert_game_data():  # inserting game data into linked list
    game_data_list = LinkedList()
    for game_type in types:
        game_sublist = LinkedList()
        for game in game_data:
            if game[0] == game_type:
                game_sublist.insert_beginning(game)
        game_data_list.insert_beginning(game_sublist)
    return game_data_list


my_type_list = insert_game_types()
my_game_list = insert_game_data()

selected_game_type = ""

while len(selected_game_type) == 0:  # requesting user input if field is empty
    user_input = str(input("\nWhat type of game would you like to play?\nType the beginning of the game type and press "
                           "enter to see if it's here\n")).lower()

    matching_types = []  # search for user_input in game types structure here
    type_list_head = my_type_list.get_head_node()
    while type_list_head is not None:
        if str(type_list_head.get_value()).startswith(user_input):
            matching_types.append(type_list_head.get_value())
        type_list_head = type_list_head.get_next_node()

    for type in matching_types:  # prints list of matching types
        print(type)

    if len(matching_types) == 1:  # check if only one game was found
        select_type = str(input("\nThe only matching type for the input is " + matching_types[0] + "."
                                "\nDo you want to look at " + matching_types[0] + " games? Enter y for yes "
                                "and n for no\n")).lower()

        if select_type == "y":  # retrieving game data
            selected_game_type = matching_types[0]
            print("Selected Game Type: " + selected_game_type)
            game_list_head = my_game_list.get_head_node()
            while game_list_head.get_next_node is not None:
                sublist_head = game_list_head.get_value().get_head_node()
                if sublist_head.get_value()[0] == selected_game_type:
                    while sublist_head.get_next_node() is not None:
                        print("*********************************")
                        print("Name: " + sublist_head.get_value()[1])
                        print("Game Score: " + sublist_head.get_value()[2] + "%")
                        print("ESRB Rating: " + sublist_head.get_value()[3])
                        print("Developer: " + sublist_head.get_value()[4])
                        print("*********************************")
                        sublist_head = sublist_head.get_next_node()
                game_list_head = game_list_head.get_next_node()


            repeat_loop = str(input("\nDo you want to find another game?"  # repeating for additional searches
            " Enter y for yes and n for no.\n")).lower()
            if repeat_loop == "y":
                selected_game_type = ""

    print("butt")