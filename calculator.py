def folder_size(folder):
    total = 0

    for item in folder:
        if type(item) == int:
            total += item
        else:
            total += folder_size(item)

    return total


folder = [100, 200, [50, 70], [80, [20, 30]], 150]

print("Total Folder Size =", folder_size(folder))