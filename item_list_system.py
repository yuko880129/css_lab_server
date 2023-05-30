import pandas as pd


# 需要增加判斷 token 是否合法的 flow cotrol
class ItemListSyetem:
    def __init__(self):
        self.item_list = pd.read_csv("./item_list.csv")
        self.newest_id = self.item_list.iloc[-1]["id"] + 1

    def addItem(self, token: str, information: list):
        # 由於還沒有實作 token 的 name，因此先以 token 代替，之後需補齊
        self.item_list = pd.concat(
            (
                self.item_list,
                pd.DataFrame(
                    [
                        [
                            token,
                            information[0],
                            information[1],
                            self.newest_id,
                            information[2],
                            information[3],
                        ]
                    ],
                    columns=["name", "date", "item_name", "id", "price", "reason"],
                ),
            ),
            ignore_index=True,
        )
        self.newest_id += 1
        return self.getItemList("1111")

    def deleteItem(self, token: str, id: int):
        index = self.getItemIndex("1111", id)
        self.item_list = self.item_list.drop(index, axis=0)
        return self.getItemList("1111")

    def getItemIndex(self, token: str, id: int):
        return self.item_list[self.item_list["id"] == id].index[0]

    def getItemList(self, token: str):
        return list(self.item_list["id"])


# test = ItemListSyetem()

# test.addItem("1111", ["Ray", "2023/05/30", "衛生紙", 600, "沒衛生紙了"])
# print(test.getItemList("1111"))

# test.deleteItem("1111", 1)
# print(test.getItemList("1111"))
