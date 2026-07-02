blacklist = ["abc123", "xyz789", "spam007", "hello111"]
sender = "spam007"

found = False

for i in blacklist:
    if i == sender:
        found = True
        break

if found:
    print("Spam Detected")
else:
    print("Not Spam")