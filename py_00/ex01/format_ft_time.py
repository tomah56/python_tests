from datetime import datetime
import time

simple_formatted_date = datetime.now().strftime("%b %d %Y")

# Get the current epoch time
current_epoch_time = int(time.time())


formatted_number = "{:,}".format(current_epoch_time)
science_formatted_number = "{:.2e}".format(current_epoch_time)

# Print the current epoch time
print("Seconds since January 1, 1970:", formatted_number, "or ", science_formatted_number,  " in scientific notation")
# print the base date as in subject
print(simple_formatted_date)