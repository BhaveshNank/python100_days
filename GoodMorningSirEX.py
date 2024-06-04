import time

current_time = time.localtime()
current_hour = current_time.tm_hour

# 3:00 am to 11:59 am (noon) is considered morning
if (current_hour >= 3 and current_hour < 12):
    print("Good Morning")
# 12:00 pm to 5:00 pm is considered afternoon
elif (current_hour >= 12 and current_hour <= 17):
    print("Good Afternoon")
elif (current_hour >= 15 and current_hour < 21):
    print("Good Evening")
else: 
    print("Good Night")