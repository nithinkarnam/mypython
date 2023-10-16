"""The environmental eco club has discovered a new Amoeba that grows in the order of a Fibonacci series every month. They are
exhibiting their amoeba in a national conference. They want to know the size of the amoeba at a particular time instant. If a
particular month’s index is given, write a program to displays the amoeba’s size……??? For Example, The size of the amoeba on
month 1, 2, 3, 4, 5, 6, ..will be 0, 1, 1, 2, 3, 5, 8 respectively. Input format: The first input containing an integer which denotes the
number of the month Output format: Print the amoeba size. Refer the sample output for formatting."""
n1=0
n2=1 
n=int(input())
for i in range(2,n):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3)
