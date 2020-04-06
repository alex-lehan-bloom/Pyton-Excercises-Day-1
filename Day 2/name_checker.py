

def name_checker(list_of_names):
    for name in list_of_names:
        if name.isspace() == True:
            yield name

    # peeps_missing_last_name = (name if name.isspace() == True else "nothing" for name in list_of_names)
    # print(list_of_names)
    # for name in peeps_missing_last_name:
    #     print(name)


list_of_names = ["Alex Bloom", "Yaakov", "Emma", "Ruthy Lewis", "David"]
people_missing_last_name = name_checker(list_of_names)
print(people_missing_last_name)
for person in people_missing_last_name:
    print(person)
