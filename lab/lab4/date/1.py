from datetime import datetime, timedelta

current_date = datetime.today()

new_date = current_date - timedelta(days=5)

print(new_date.strftime("%Y-%m-%d"))