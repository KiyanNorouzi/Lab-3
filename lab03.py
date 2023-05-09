#####
##### Ф.И: Ноурузи Мехди
##### ИСУ: 317306
##### группа: R3135
#####Номер варианта: 6
#####

# Define the inventory list
inventory = {
    "в": ["Винтовка", 3, 25],
    "п": ["Пистолет", 2, 15],
    "б": ["Боекомплект", 2, 15],
    "а": ["Аптечка", 2, 20],
    "и": ["Ингалятор", 1, 5],
    "н": ["Нож", 1, 15],
    "т": ["Топор", 3, 20],
    "о": ["Оберег", 1, 25],
    "ф": ["Фляжка", 1, 15],
    "д": ["Антидот", 1, 10],
    "к": ["Еда", 2, 20],
    "р": ["Арбалет", 2, 20]
}

# Define Tom's backpack size and requirements
backpack_size = 3
infected = True
needs_inhaler = False
needs_antidote = True
required_points = 15

# Define the current backpack and survival points
backpack = [['-' for j in range(backpack_size)] for i in range(backpack_size)]
current_points = 0

# Define a function to add an item to the backpack
def add_item_to_backpack(item_designation):
    global current_points
    item = inventory[item_designation]
    item_name = item[0]
    item_size = item[1]
    item_points = item[2]
    for i in range(backpack_size):
        for j in range(backpack_size):
            if backpack[i][j] == '-':
                if item_size <= backpack_size - i and item_size <= backpack_size - j:
                    backpack[i][j] = item_designation
                    current_points += item_points
                    return True
    return False

# Add required items to the backpack
if infected and needs_inhaler:
    add_item_to_backpack('и')
if infected and needs_antidote:
    add_item_to_backpack('д')
add_item_to_backpack('а')

# Add other items to the backpack until it's full or no more items can be added
while True:
    item_added = False
    for item_designation in inventory.keys():
        if add_item_to_backpack(item_designation):
            item_added = True
    if not item_added:
        break

# Check if Tom will survive and print the backpack
if current_points >= required_points:
    print("Tom will survive!")
else:
    print("Tom will not survive!")
for i in range(backpack_size):
    for j in range(backpack_size):
        print("[{}]".format(backpack[i][j]), end="")
    print()
print("Total points:", current_points)