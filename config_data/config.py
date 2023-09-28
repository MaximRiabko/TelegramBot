# import os
# # from dotenv import load_dotenv, find_dotenv
# #
# # if not find_dotenv():
# #     exit("Переменные окружения не загружены т.к отсутствует файл .env")
# # else:
# #     load_dotenv()

# BOT_TOKEN = os.getenv("")
# RAPID_API_KEY = os.getenv("RAPID_API_KEY")

BOT_TOKEN = "6080375267:AAFVgZylGUKlhEUTkjIMSk1PxW2hPgDkDu4"
RAPID_API_KEY = "37eee72770msh5ee7b17a443bcbbp15aa68jsnff3c3f46501c"
DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("low", "Вывод самых дешёвых отелей"),
    ("high", "Вывод самых дорогих отелей"),
    ("custom", "Вывод показателей пользовательского диапазона"),
    ("history", "Вывод истории запросов")
)