def overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False


# Input from user
list1 = input("Enter first list elements separated by space: ").split()
list2 = input("Enter second list elements separated by space: ").split()

# Check overlapping
result = overlapping(list1, list2)

# Output
print("Overlapping:", result)
