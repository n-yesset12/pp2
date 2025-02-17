from datetime import datetime

def date_difference_in_seconds(date1, date2):
    """Calculates the difference between two dates in seconds."""
    diff = abs((date2 - date1).total_seconds())
    return int(diff)


date1 = datetime(2025, 2, 1, 12, 0, 0)  
date2 = datetime(2025, 2, 7, 14, 30, 0) 

print("Difference in seconds:", date_difference_in_seconds(date1, date2))