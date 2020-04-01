guest22 = open("guest33.txt","w")
initial_guests=["Amy","mooli","Joe","goori"]
for i in initial_guests:
    guest22.write(i+'\t')
guest22.close()


new_guests = ["Sam", "Danielle", "Jacob"]

with open("guest33.txt","a") as guestHi:
    for i in new_guests:
        guestHi.write(i + "\t")

guestHi.close()