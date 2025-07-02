#Adding all divisible number depending on user input

start_range = int (input("Enter starting number: "))
end_range = int (input("Enter ending number: "))
multiple = int (input("multiple: "))
total = 0
for i in range (start_range , end_range +1):
    if i % multiple == 0:
        total += i
print (total)