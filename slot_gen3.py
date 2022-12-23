from datetime import date
import datetime

input_start_datetime = '2022-12-14 21:00' # event start datetime in format yyyy-mm-dd HH:MM
input_slot_length =  30 # in min
input_num_slots = 4 # Number of slots
input_start_time_is_end_time = False
input_slot_open = ''

def get_timeslot_timestamps(event_datetime, slot_length, num_of_slots, start_time_is_end_time):
    result = []
    epoch = event_datetime.timestamp()
    
    if start_time_is_end_time:
        epoch = epoch - slot_length * 60 * num_of_slots
    
    result.append(epoch)
    for i in range(num_of_slots - 1):
        epoch = epoch + slot_length * 60
        result.append(epoch)
        
    return result
    
def get_discord_text(timeslots, open_str):
    return "\n".join("[{}] <t:{:.0f}:f> {}".format(index+1, slot, open_str) for index, slot in enumerate(timeslots))
    
dt_start = datetime.datetime.strptime(input_start_datetime, "%Y-%m-%d %H:%M")
slots = get_timeslot_timestamps(dt_start, input_slot_length, input_num_slots, input_start_time_is_end_time)

print(get_discord_text(slots, input_slot_open))