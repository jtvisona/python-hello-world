from datetime import datetime

today = datetime(2022, 9, 26)
birthday = datetime(2022, 11, 21)
wait_time = birthday - today
print( type( wait_time ) )
days = wait_time.days
print("There are", days, "days until your birthday!")

#dictionary view object: dict_keys, dict_values, dict_items