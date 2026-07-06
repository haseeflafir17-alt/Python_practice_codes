marks = []
n = int(input("How many marks do you want to enter? "))

for i in range(n):
    marks.append(int(input(f"Enter mark {i+1}: ")))

print(f"Marks: {marks}")

high = max(marks)
low = min(marks)
total = sum(marks)
avg = total/n
print(f"Highest: {high}")
print(f"Lowest: {low}")
print(f"Total: {total}")
print(f"Average: {avg:.2f}")


search =int(input("Enter a marks to search: "))
if search in marks:
    print(f"First found at index: {marks.index(search)}")
    print(f"Occurrences: {marks.count(search)}")
else:
    print(f"Mark {search} is not found")