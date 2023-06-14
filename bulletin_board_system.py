import pandas as pd


class BullentinBoardSyetem:
    def __init__(self):
        self.announcement_list = pd.read_csv("./db/announcement_list.csv")
        self.newest_id = self.announcement_list.iloc[-1]["id"] + 1

        try:
            self.pinned_id = self.announcement_list[
                self.announcement_list["pinned"] == 1
            ].index[0]
        except:
            self.pinned_id = -1

    def addItem(self, token: str, information: str):
        # 由於還沒有實作 token 的 name，因此先以 token 代替，之後需補齊
        information = information.split(",")
        self.announcement_list = pd.concat(
            (
                self.announcement_list,
                pd.DataFrame(
                    [
                        [
                            information[0],
                            information[1],
                            information[2],
                            self.newest_id,
                            0,
                        ]
                    ],
                    columns=["name", "time", "content", "id", "pinned"],
                ),
            ),
            ignore_index=True,
        )
        print(self.announcement_list)
        self.newest_id += 1
        return self.getItemList("1111")

    def deleteItem(self, token: str, id: str):
        index = self.getItemIndex(int(id))
        if self.announcement_list.at[index, "pinned"] == 1:
            self.pinned_id = -1
        self.announcement_list = self.announcement_list.drop(index, axis=0)
        print(self.announcement_list)
        return self.getItemList("1111")

    def getItemById(self, token: str, id: str):
        temp = self.announcement_list[
            self.announcement_list["id"] == int(id)
        ].values.tolist()[0]
        return temp[:3]

    def getItemIndex(self, id: int):
        return self.announcement_list[self.announcement_list["id"] == id].index[0]

    def getItemList(self, token: str):
        return list(self.announcement_list["id"])

    def getPinnedId(self, token: str):
        return str(self.pinned_id)

    def setPinnedAnnouncement(self, token: str, id: str):
        self.pinned_id = int(id)
        self.announcement_list["pinned"] = 0
        if int(id) != -1:
            index = self.announcement_list[
                self.announcement_list["id"] == int(id)
            ].index[0]
            self.announcement_list.at[index, "pinned"] = 1
        print(self.announcement_list)
