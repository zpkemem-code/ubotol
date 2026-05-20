import os

from dotenv import load_dotenv

load_dotenv(".env")

DEVS = [8948668149]



API_ID = int(os.getenv("API_ID", "36794114"))

API_HASH = os.getenv("API_HASH", "dd9955a94f1fa9a7a7b39f461e638774")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8808350999:AAF6vp_7ZiHMRdKdYUr54K0vHsr4QH_Jb4c")

OWNER_ID = int(os.getenv("OWNER_ID", "8948668149"))

USER_ID = list(map(int, os.getenv("USER_ID", "6696975845 1838348402 6696975845 6051457085 6527347171").split()))

LOG_UBOT = int(os.getenv("LOG_UBOT", "-1003992265929"))

LOG_SELLER = int(os.getenv("LOG_SELLER", "-1003992265929"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002075041230 -1002164901876 -1002166018703 -1001473548283 -1001390552926 -1001672802736 -1001917973794 -1002433894643").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "10"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "sk-b76-2Xm3NudxolduxgQnvFQTmbSjF0MQEVXtP4EfmMT3BlbkFJfk1LYV_1GUrcanMhuvhafaJ2dLs4yYwsgH5aBtaI8A",
).split()

MONGO_URL = os.getenv(
    "MONGO_URL", "mongodb+srv://biduan:biduan@cluster0.3uiosr7.mongodb.net/?appName=Cluster0")
