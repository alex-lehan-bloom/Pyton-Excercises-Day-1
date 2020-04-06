import os


def directories(path):
    for root, folders, files in os.walk(path):
        for file in files:
            print(os.path.join(root, file))

path = 'C:\\Users\\lehan\\OneDrive\\Documents\\ITC\\Course\Week 7'
directories(path)





