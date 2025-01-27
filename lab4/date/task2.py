from datetime import datetime, timedelta
yesterday = datetime.today() - timedelta(days=1)
today = datetime.today()
tomorrow = datetime.today() + timedelta(days=1)
print(f"Yestarday was {yesterday}") 
print(f"Today is {today}")
print(f"Tomorrow will be {tomorrow}")