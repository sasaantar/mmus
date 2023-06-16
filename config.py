from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID","19485334"))
API_HASH = getenv("API_HASH","0a9bb0ec8c2dac715c54b9a3cb4c5606")

BOT_TOKEN = getenv("BOT_TOKEN", "5518762082:AAGtV3KFfgKvPTO24EqjAjXzyOIHyNcqvQQ")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID","5385770251"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "AQBPFkQzOhynSQax4RxI7kb99-_mMs9MAVkSFM1kGJi3EDbn6UY-Am1fyOsLvU-06NFT3MURXZyowkGV7vtV5raNWBAjcmuxaVIs0LCdg13BDc7r4cC4pezu6nwdG4-dYlyN4CcS_Q54eyG5XCMjUuVkaA5SRmE8-kvr_wEna8VJD67IsmlXIoT3zLFiYlbR17eMvkdGHkut06_bn5bsf01zJUt2xyILnCmn4GUTThmQbKKOG7kEB2Q3I_NZpKY92lJyIXEiB8yX8RBLrtZrVm8GthwcMRG0Rv0PVuRMgcKN5PnxMe5FQnJYq5LJo7cluA208TH9WenNhDCh8jTCdiBhAAAAAWh_MnAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/dkdkdodohh")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/s_q_i")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5385770251 6020169916").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
