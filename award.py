'''program requests user's output to determine time achieved in three events 
of triathlon and then calculates and displays the total time taken to complete
the triathlon. Depending on the specified criteria it also displays
the message on the award obtained, using if, elif, else control structure'''


time_swimming = int(input("Please enter the swimming time in minutes:"))
time_cycling = int(input("Please enter the cycling time in minutes:"))
time_running = int(input("Please enter the running time in minutes:"))
total_time = time_swimming + time_cycling + time_running 
print(f"The total time taken to complete the triathlon was {total_time} minutes")

if total_time <= 100:
    print("You have won Provincial Colours.")
elif total_time <= 105:
    print("You have won Provincial Half Colours")
elif total_time <= 110:
    print("You have won Provincial Scroll")
else:
    print("You have not qualified for an award.") 