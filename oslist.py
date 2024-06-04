import os
folders = os.listdir("Data")

# print(folders)

# for folder in folders:
#     print(folder)


os.chdir("/Users")
print(os.getcwd())

for folder in folders:
    print(folder)
    print(os.listdir(f"Data/{folder}"))

