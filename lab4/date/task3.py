from datetime import datetime
now = datetime.now()

no_micro = now.replace(microsecond=0)
print("Datetime without microseconds: ", no_micro)