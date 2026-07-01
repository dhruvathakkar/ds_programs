size=5
vehicle=['None']*size
add_vehicle=input("Enter the vehicle you want to add: ")
for i in range(len(vehicle)):
    if vehicle[i]=='None':
        vehicle[i]=add_vehicle
        print("Vehicle added at index",i)
        break
    elif i==len(vehicle)-1: 
        print("Vehicle list is full")