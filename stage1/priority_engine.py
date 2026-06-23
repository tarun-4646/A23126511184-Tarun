import json
from datetime import datetime

with open("stage1/notifications.json","r") as f:
    data = json.load(f)

notifications = data["notifications"]

priority_map = {
    "Placement":3,
    "Result":2,
    "Event":1
}

for n in notifications:

    n["priority"] = priority_map[n["Type"]]

    n["time"] = datetime.strptime(
        n["Timestamp"],
        "%Y-%m-%d %H:%M:%S"
    )

sorted_notifications = sorted(
    notifications,
    key=lambda x:(
        x["priority"],
        x["time"]
    ),
    reverse=True
)

top10 = sorted_notifications[:10]

print("\nTOP 10 PRIORITY NOTIFICATIONS\n")

for i,n in enumerate(top10,1):

    print(
        f"{i}. "
        f"{n['Type']} | "
        f"{n['Message']} | "
        f"{n['Timestamp']}"
    )