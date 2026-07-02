list1 = [1, 4, 6, 8]
list2 = [2, 3, 5, 7, 9]

i = 0
j = 0
merged = []

while i < len(list1) and j < len(list2):
    if list1[i] <= list2[j]:
        merged.append(list1[i])
        i += 1
    else:
        merged.append(list2[j])
        j += 1

while i < len(list1):
    merged.append(list1[i])
    i += 1

while j < len(list2):
    merged.append(list2[j])
    j += 1

print("Merged List:", merged)