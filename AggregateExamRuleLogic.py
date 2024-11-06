from statistics import mean

while True:
    # Ask for Maths Marks
    print("What's Maths Marks?")
    Math_M = int(input())
    
    # Check if Math marks are less than 40
    if Math_M < 40:
        print("You failed in Maths.")
        continue  # Ask again for Maths marks
    
    # Ask for Bio Marks
    print("What's Bio Marks?")
    Bio_M = int(input())
    
    # Check if Bio marks are less than 40
    if Bio_M < 40:
        print("You failed in Bio.")
        continue  # Ask again for Bio marks
    
    # Ask for Physics Marks
    print("What's Physics Marks?")
    Physics_M = int(input())
    
    # Check if Physics marks are less than 40
    if Physics_M < 40:
        print("You failed in Physics.")
        continue  # Ask again for Physics marks
    
    # If all subjects are passed individually, calculate the aggregate
    MarkList = [Math_M, Bio_M, Physics_M]
    
    # Check the aggregate marks (average of all subjects)
    if mean(MarkList) > 50:
        print("You passed the exam with an average of {:.2f}.".format(mean(MarkList)))
        break  # Exit the loop since the student has passed both individually and in aggregate
    else:
        print("Your aggregate marks are less than 50. Please try again.")
        continue  # Ask for marks again, since the aggregate is below 50
