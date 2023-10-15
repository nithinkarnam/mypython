'''A microwave oven manufacturer recommends that when heating two items, add 50% to the heating time, and when heating three
items double the heating time. Heating more than three items at once is not recommended. Write a python program to find out the
recommended heating time. Input format: The first input containing an integer which denotes the number of items The second input
containing the floating point number which denotes the single item heating time. Output format: Print the recommended heating time
in floating point with 2 decimal places. If the number of items is more than three, print "Number of items is more" Refer the sample
output for formatting'''
items=int(input())
heat=float(input())
if(items==2):
  heat=heat+0.5*heat
  print("{:.2f}".format(heat))
elif(items==3):
  heat=heat*2
  print("{:.2f}".format(heat))
elif(items>3):
  print("danger not recomonded")
else:
  print("error")
  
