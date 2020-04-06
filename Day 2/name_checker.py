
def name_checker(list_of_names):
    for name in list_of_names:
        if ' ' not in name:
            yield name


list_of_names = ["Alex Bloom", "Yaakov", "Emma", "Ruthy Lewis", "David"]
people_missing_last_name = name_checker(list_of_names)
for person in people_missing_last_name:
    print(person)
