
age = int(input("How old are you? (in a whole number of years)"))
maximum_heartrate = round(208 - (0.7 * age))
print("Due to your age, your maximum recommended heartrate is", maximum_heartrate, "BPM")
print("Your training zones are as follows:")
interval = round(0.9 * maximum_heartrate)
threshold = round(0.7 * maximum_heartrate)
aerobic = round(0.5 * maximum_heartrate)
##print("Interval Training - Anything above", interval, "BPM.")
##print("Threshold Training - Between", threshold, "and", interval, "BPM.")
##print("Aerobic Training - Between", aerobic, "and", threshold, "BPM.")
##print("Couch Potato - Anything below", aerobic, "BPM.")


training_heartrate = int(input("What is your training heartrate?"))
if training_heartrate >= interval:
    print("Your Training Zone is Interval Training")
elif training_heartrate < interval and training_heartrate >= threshold:
    print("Your Training Zone is Threshold Training")
elif training_heartrate < threshold and training_heartrate >= aerobic:
    print("Your Training Zone is Aerobic Training")
else:
    print("Your Training Zone is Couch Potato")
