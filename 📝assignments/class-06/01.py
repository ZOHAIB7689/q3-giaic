# File Handling
# w: Write mode. Opens the file for writing. Creates the file if it doesn't exist, or overwrites it if it does.

file = open("new_file.txt", "w")

# writing to Files
# to write to a file, open it in write ("w") or append ("a") mode
# write(string): Writed the given string to the file.


file.write("Hello, World! \n ")
file.write("This is a new file. \n")
file.close()


# writelined(list): Writed a list of strings to the file

lines = ["Line 1:Karachi\n", "Line 2: Lahore\n", "Line 3: Islamabad\n", "Line 4: Peshawar\n"]
file = open("new_file.txt", "w")
file.writelines(lines)
file.close()



# Now let start reading the file what we have created earlier.
file = open("new_file.txt", "r") 
line = file.readlines()
print(line)


#Move pointer back to start
file.seek(0)
print(f"Position after seek(0): {file.tell()}") #Output: Position after seek(0): 0


#readlines(): Reads all lines into a list.
file.seek(0)

lines = file.readlines()
for line in lines:
    print(line)

file = open("new_file.txt", "r")
for line in file:
    print(line.strip())


# It's crucial to close files after you're finished with them. This releases system resources and ensures that data is properly written to the disk. The close() method is used for this:
file.close()

# Exclusic creation (x mode)

try:
    with open('unique.txt', 'x')as file:
        file.write("Created Exclusively")
        print("File created succesfully!")
except FileExistsError:
    print("File already exists. Choose a different name.")


    
# The with Statement (Context Manager):
with open("new_file.txt", "r") as file:
    content = file.read()
    print(content)




def copy_file(source_path, destination_path):
    try:
        with open(source_path, "r") as source_file, open(destination_path, "w") as dest_file:
            for line in source_file:
                dest_file.write(line)
        print(f"File '{source_path}' copied to '{destination_path}' successfully.")
    except FileNotFoundError:
        print(f"Error: Source file '{source_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

copy_file("unique.txt", "unique_copy.txt")

# Binary mode (Ussed eith other modes(eg., "rb", "wb". with binary files))

def copy_image(source_path, destination):
    try:
        with open(source_path, "rb") as source_file:
            with open(destination, "wb") as destination_file:
                while True:
                    chunk = source_file.read(1024)
                    if not chunk:
                        break
                    destination_file.write(chunk)
        print(f"Image copied from '{source_path}' to '{destination}' successfully.")
    except FileNotFoundError:
        print(f"Error: Source file '{source_path}' not found.")

copy_image("Apollo11.jpg", "Copy_Apollo11.jpg")


#Full example of operations demo
# Create and write to a file
with open('demo.txt', 'w') as file:
    file.write('Python File Handling\n')
    file.write('Line 1\nLine 2\n')

# Read and print content
with open('demo.txt', 'r') as file:
    print("Content:")
    print(file.read())

# Append a new line
with open('demo.txt', 'a') as file:
    file.write('Appended line\n')

# Read lines using seek
with open('demo.txt', 'r+') as file:
    file.seek(0)
    print("First line:", file.readline())