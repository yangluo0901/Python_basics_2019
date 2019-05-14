import tushare

share_info = tushare.get_realtime_quotes("000591")
# share_info[["code", "name", "high", "low", "volume", "trade "]]
print(share_info)
