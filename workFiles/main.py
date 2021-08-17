import os

print(os.getcwd())
with open("new_file.txt", mode="w") as file:
    file.write("\nNew text.")

