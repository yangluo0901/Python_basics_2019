import tushare


class Share:
    def __init__(self, code):
        self.code = code
        self.name = ""
        self.high = ""
        self.low = ""
        self.volume = ""
        self.trade = ""
        self.update()

    def update(self):
        share_info = tushare.get_realtime_quotes(self.code)
        share_info[["code", "name", "high", "low", "volume", "price"]]
        self.name = share_info.loc[0][0]
        self.high = share_info.loc[0][4]
        self.low = share_info.loc[0][5]
        self.volume = share_info.loc[0][8]
        self.trade = share_info.loc[0][3]

