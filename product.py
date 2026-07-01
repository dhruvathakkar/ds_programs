belt=['monitor',
    'keyboard',
    'mouse',
    'speaker',
    'microphone',
    'printer',
    'scanner',
    'projector']
for i in range(len(belt)):
    print(i,belt[i])
prod=input("Enter the product you want to search: ")
for i in range(len(belt)):
    if prod==belt[i]:
        print("Product found at index",i)
        break
    elif i==len(belt)-1:
        print("Product not found")
belt[2]='webcam'
for i in range(len(belt)):
    print(i,belt[i])

for i in range(len(belt)):
    if i==len(belt)-1:
        print("belt is full")
    elif belt[i]=='':
        print("belt is not full")

