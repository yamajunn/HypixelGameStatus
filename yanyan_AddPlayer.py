import csv
from yanyan_GetStatus import bedwars_status

def add_player(name):
    with open('./player.csv', 'r',) as e:
        players = []
        data = e.read()
        data = data.split("\n")
        total_player = len(data)
        for i, item in enumerate(data):
            item_data = item.split(",")
            if i != 0 and i != len(data)-1:
                players.append(item_data[0])
    if not name in players:
        with open('./player.csv', 'a', newline="") as e:
            writer = csv.writer(e)
            status = bedwars_status(True, name)
            if status[0] != True:
                if total_player <= 25:
                    writer.writerow(status)
                    return f"Success! add {name}"
                else:
                    return f"Cannot add more than 25 people ({name})"
            elif status[0] == True:
                return f"{status[1]} ({name})"
            else:
                return f"Unknown Error ({name})"
    else:
        return f"{name} has already been added."
# print(add_player("Gokiton"))