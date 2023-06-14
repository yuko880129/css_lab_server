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
    system.bulletin_board_system.announcement_list.to_csv(
        "./db/announcement_list.csv", index=False
    )
    print("\nWrite back list succeccfully.")


atexit.register(exit_handler)


@server.route("/")
def root():
    return ""


@server.route("/add_restraunt", methods=["POST"])
def roulette1():
    system.roulette_system.addToMemberRestaurantList(
        request.headers["Member-Id"], request.values["name"]
    )
    return "success"


@server.route("/clear_restraunt", methods=["POST"])
def roulette2():
    system.roulette_system.clearMemberRestaurantList(request.headers["Member-Id"])
    return "success"


@server.route("/get_restraunt_list", methods=["POST"])
def roulette3():
    return jsonify(
        {
            "list": system.roulette_system.getMemberRestaurantList(
                request.headers["Member-Id"]
            )
        }
    )


@server.route("/cleaning_get_members", methods=["POST"])
def cleaning1():
    return jsonify(
        {
            "list": system.cleaning_time_table_system.getHatarakuMembers(
                request.headers["Member-Id"]
            )
        }
    )


@server.route("/cleaning_get_startD", methods=["POST"])
def cleaning2():
    return jsonify(
        {
            "startD": system.cleaning_time_table_system.getSemesterStartD(
                request.headers["Member-Id"]
            )
        }
    )


@server.route("/cleaning_get_endD", methods=["POST"])
def cleaning3():
    return jsonify(
        {
            "endD": system.cleaning_time_table_system.getSemesterEndD(
                request.headers["Member-Id"]
            )
        }
    )


@server.route("/meeting_get_time", methods=["POST"])
def meeting1():
    return jsonify(
        {
            "time": system.meeting_time_table_system.getmeeting_time(
                request.headers["Member-Id"]
            )
        }
    )


@server.route("/course_get_time", methods=["POST"])
def course1():
    return jsonify(
        {
            "time": system.school_time_table_system.getMemberClassTimeSchedual(
                request.headers["Member-Id"], request.values["name"]
            )
        }
    )


@server.route("/course_get_members", methods=["POST"])
def course2():
    return jsonify(
        {
            "members": system.school_time_table_system.getAllMembers(
                request.headers["Member-Id"]
            )
        }
    )


@server.route("/item_list_add_item", methods=["POST"])
def item1():
    return jsonify(
        {
            "list": system.item_list_system.addItem(
                request.headers["Member-Id"], request.values["information"]
            )
        }
    )


@server.route("/item_list_delete_item", methods=["POST"])
def item2():
    return jsonify(
        {
            "list": system.item_list_system.deleteItem(
                request.headers["Member-Id"], request.values["id"]
            )
        }
    )


@server.route("/item_list_get_list", methods=["POST"])
def item3():
    return jsonify(
        {"list": system.item_list_system.getItemList(request.headers["Member-Id"])}
    )


@server.route("/item_list_get_item", methods=["POST"])
def item4():
    return jsonify(
        {
            "info": system.item_list_system.getItemById(
                request.headers["Member-Id"], request.values["id"]
            )
        }
    )


@server.route("/bb_list_add_announcement", methods=["POST"])
def bb1():
    return jsonify(
        {
            "list": system.bulletin_board_system.addItem(
                request.headers["Member-Id"], request.values["information"]
            )
        }
    )


@server.route("/bb_list_delete_announcement", methods=["POST"])
def bb2():
    return jsonify(
        {
            "list": system.bulletin_board_system.deleteItem(
                request.headers["Member-Id"], request.values["id"]
            )
        }
    )


@server.route("/bb_list_get_list", methods=["POST"])
def bb3():
    return jsonify(
        {"list": system.bulletin_board_system.getItemList(request.headers["Member-Id"])}
    )


@server.route("/bb_list_get_announcement", methods=["POST"])
def bb4():
    return jsonify(
        {
            "info": system.bulletin_board_system.getItemById(
                request.headers["Member-Id"], request.values["id"]
            )
        }
    )


@server.route("/bb_list_get_pinned_id", methods=["POST"])
def bb5():
    return jsonify(
        {"id": system.bulletin_board_system.getPinnedId(request.headers["Member-Id"])}
    )


@server.route("/bb_list_pin_announcement", methods=["POST"])
def bb6():
    system.bulletin_board_system.setPinnedAnnouncement(
        request.headers["Member-Id"], request.values["id"]
    )
    return "success"


if __name__ == "__main__":
    server.run()
