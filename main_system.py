from bulletin_board_system import BullentinBoardSyetem
from cleaning_time_table_system import CleaningTimeTableSystem
from item_list_system import ItemListSyetem
from meeting_time_table_system import MeetingTimeTableSystem
from member import Member
from roulette_system import RouletteSyetem
from school_time_table_system import SchoolTimeTableSystem

from flask import Flask, jsonify, request

import atexit


class MainSystem:
    def __init__(self):
        self.bulletin_board_system = BullentinBoardSyetem()
        self.cleaning_time_table_system = CleaningTimeTableSystem()
        self.item_list_system = ItemListSyetem()
        self.meeting_time_table_system = MeetingTimeTableSystem()
        self.roulette_system = RouletteSyetem()
        self.school_time_table_system = SchoolTimeTableSystem()
        self.member_list: list[Member] = []


system = MainSystem()
server = Flask(__name__)


# Write back item list while shutting down server
def exit_handler():
    system.item_list_system.item_list.to_csv("./db/item_list.csv", index=False)
    print("\nWrite back item list succeccfully.")


atexit.register(exit_handler)


@server.route("/")
def root():
    return ""


@server.route("/add_restraunt", methods=["POST"])
def roulette1():
    print(request.headers)
    system.roulette_system.addToMemberRestaurantList(
        request.headers["Member-Id"], request.values["name"]
    )
    return "success"


@server.route("/clear_restraunt", methods=["POST"])
def roulette2():
    print(request.headers)
    system.roulette_system.clearMemberRestaurantList(request.headers["Member-Id"])
    return "success"


@server.route("/get_restraunt_list", methods=["POST"])
def roulette3():
    print(request.headers)
    return jsonify(
        {
            "list": system.roulette_system.getMemberRestaurantList(
                request.headers["Member-Id"]
            )
        }
    )


@server.route("/cleaning_get_members", methods=["POST"])
def cleaning1():
    print(request.headers)
    return jsonify(
        {
            "list": system.cleaning_time_table_system.getHatarakuMembers(
                request.headers["Member-Id"]
            )
        }
    )


@server.route("/cleaning_get_startD", methods=["POST"])
def cleaning2():
    print(request.headers)
    return jsonify(
        {
            "startD": system.cleaning_time_table_system.getSemesterStartD(
                request.headers["Member-Id"]
            )
        }
    )


@server.route("/cleaning_get_endD", methods=["POST"])
def cleaning3():
    print(request.headers)
    return jsonify(
        {
            "endD": system.cleaning_time_table_system.getSemesterEndD(
                request.headers["Member-Id"]
            )
        }
    )


@server.route("/meeting_get_time", methods=["POST"])
def meeting1():
    print(request.headers)
    return jsonify(
        {
            "time": system.meeting_time_table_system.getmeeting_time(
                request.headers["Member-Id"]
            )
        }
    )


@server.route("/course_get_time", methods=["POST"])
def course1():
    print(request.headers)
    return jsonify(
        {
            "time": system.school_time_table_system.getMemberClassTimeSchedual(
                request.headers["Member-Id"], request.values["name"]
            )
        }
    )


@server.route("/course_get_members", methods=["POST"])
def course2():
    print(request.headers)
    return jsonify(
        {
            "members": system.school_time_table_system.getAllMembers(
                request.headers["Member-Id"]
            )
        }
    )


@server.route("/item_list_add_item", methods=["POST"])
def item1():
    print(request.headers)
    return jsonify(
        {
            "list": system.item_list_system.addItem(
                request.headers["Member-Id"], request.values["information"]
            )
        }
    )


@server.route("/item_list_delete_item", methods=["POST"])
def item2():
    print(request.headers)
    return jsonify(
        {
            "list": system.item_list_system.deleteItem(
                request.headers["Member-Id"], request.values["id"]
            )
        }
    )


@server.route("/item_list_get_list", methods=["POST"])
def item3():
    print(request.headers)
    return jsonify(
        {"list": system.item_list_system.getItemList(request.headers["Member-Id"])}
    )


@server.route("/item_list_get_item", methods=["POST"])
def item4():
    print(request.headers)
    return jsonify(
        {
            "info": system.item_list_system.getItemById(
                request.headers["Member-Id"], request.values["id"]
            )
        }
    )


if __name__ == "__main__":
    server.run()
