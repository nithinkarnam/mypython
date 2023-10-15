'''Ask the customer's age and for the time on a 24-hour clock (where noon is 12.00 and 4:30 PM is 16.30). The show timings are
10.15, 13.30, 18.00 and 22.00. The normal adult ticket price is $8.00, however, the adult matinee price is $5.00. Adults are those
over 13 years. The normal children's ticket price is $4.00, however, the children's matinee price is $2.00. Write a python program
that determines the price of a movie ticket Input format: The first input containing an integer which denotes the age The second input
containing the floating point number which denotes the show timing. Output format: Print the price of a movie ticket. Refer the
sample output for formatting'''

age=int(input())
showtime=float(input())
natp=8.00
amp=5.00
nctp=4.00
cmp=2.00
if(age>13 and showtime>=12.00):
  print("{:.2f}".format(amp))
elif(age>13 and showtime<12.00):
  print("{:.2f}".format(natp))
elif(age<13 and showtime<12.00):
  print("{:.2f}".format(nctp))
elif(age<13 and showtime>=12.00):
  print("{:.2f}".format(cmp))
else:
  print("error")
