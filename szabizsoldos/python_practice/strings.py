from datetime import date, timedelta

today = date.today().strftime("%d.%m.%Y")
yesterday = (date.today() - timedelta(1)).strftime("%d.%m.%Y")

yesterday_message = "You have {unread} unread emails since {yesterday}".format(unread=32, yesterday=yesterday);
today_message = "You have {unread} unread emails {today}".format(unread=0, today=today);

print(yesterday_message)
print('-' * len(yesterday_message))
print(today_message)
print("{:>50}".format("text"))
