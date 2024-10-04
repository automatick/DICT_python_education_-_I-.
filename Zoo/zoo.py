import re

#stage 1
print("""
I love animals!
Let's check out the animals...
The deer looks fine.
The lion looks healthy.
""")

# stage 2
print(r"""
The camel habitat...
    _______\\__
   (_. _ ._  _/
    '-' \__. /
         /  /
        /  /    .--.  .--.
       (  (    / '' \/ '' \   "
        \  \_.'            \   )
        ||               _  './
         |\   \     ___.'\  /
           '-./   .'    \ |/
              \| /       )|\
               |/       // \\
               |\    __//   \\__
              //\\  /__/     \__|
          .--_/  \_--.
         /__/      \__\
Look at that!
""")
#3 stage
with open("arts.txt", "r") as f:
    fstr = f.read()
    pattern = r'index:(\d+)/name:([a-zA-Z]+)\n((?:.|\n)+?)(?=index|$)'
    matches = re.findall(pattern, fstr)

indexes = dict()
for match in matches:
    indexes[match[0]] = [match[1], match[2]]

print("Please enter the number of the habitat you would like to view.")
index = input("-> ")
name = indexes[index][0]
art = indexes[index][1]
print(f"Showing the {name} habitat...\n{art}")