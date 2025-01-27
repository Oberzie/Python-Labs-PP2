from datetime import datetime
d1 = datetime.today()  
d2 = datetime(2025, 1, 27, 12, 25, 0)  # Jan 27 2025 at 12:25:00

difference = d1 - d2
difference_in_seconds = difference.total_seconds()

print("Difference in seconds:", difference_in_seconds)
