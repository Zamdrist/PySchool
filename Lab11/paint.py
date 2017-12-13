# Lab 11 - Paint rooms
# Author: Steve Schroeder
# Define three rooms using dimensions and color, return detail
#
import room


def main():
    try:
        bedroom, dinning_room, hallway = program_input()
        room_list = program_processing(bedroom, dinning_room, hallway)
        program_output(room_list)
    except:
        print("An error occurred. Program ending")
        # PyCharm says this is too broad of an exception


def program_input():
    bedroom = room.Room(25, 20, 12, "bedroom")
    bedroom.setColor("green")
    bedroom.setPaint_needed()

    dining_room = room.Room(12, 11, 8, "dining room")
    dining_room.setColor("yellow")
    dining_room.setPaint_needed(2)

    hallway = room.Room(15, 4, 8, "hallway")
    hallway.setColor("white")
    hallway.setPaint_needed()

    return bedroom, dining_room, hallway


def program_processing(bedroom, dining_room, hallway):
    room_list = [bedroom, dining_room, hallway]
    return room_list


def program_output(room_list):
    for room_named in room_list:
        print(room_named)


main()
