# file = open("file.txt","w")
# file.write("Hello World\n")
# file.write("This is another line\n")
# file.close()

# lines = ["Line 1: Karachi\n","Line 2: Lahore\n","Line 3: Islamabad\n"]
# file= open("file.txt","a")
# file.writelines(lines)
# file.close()

file = open("file.txt","r")
# file = open("file.txt","rb")
# print(file.tell()) # tell current position (file pointer)
# content = file.read() # read all file content
# print(file.tell())
# print(file.seek(0))
# content = file.readline() # read first line
# print(content.decode("utf-8")) # decode bytes to string
# print(file.tell())
# print(file.seek(-5,1))
# content = file.readlines() # read all lines in a list
# print(file.tell())
# print(content)
file.seek(0)

# examples
# file.seek(5, 0)  # Start se 5 bytes aage jao
# file.seek(2, 1)  # Current position se 2 bytes aage
# file.seek(-3, 2) # End se 3 bytes peechay

# loop through files
# lines= file.readlines()
# for line in lines:
#     print(line.strip())

# print(file.tell()) # 87
# file.seek(0)

# # direct loop
# for line in file:
#     print(line.strip())


# try:
#     with open("unique.txt","x") as file:
#         file.write("Created Exclusively!")
#         print("File Created Successfully!")
# except FileExistsError:
#     print("File already Exists")

# ex 1 (copy file)

def copy_file(source_path,destination_path):    
    try:
        with open(source_path,"r") as source_file, open(destination_path,"w") as destination_file:
            for line in source_file:
                destination_file.write(line)
            print(f"File {source_path} copied to {destination_path  } successfully!")
    except FileNotFoundError:
        print(f"Error: Source file '{source_path} not found'")
    except Exception as e:
        print("an error occured: ",e)

copy_file("file.txt","file_copy.txt")

# ex 2 (copy image)

def copy_image(source_path,destination_path):    
    try:
        with open(source_path,"rb") as source_file:
            with open(destination_path,"wb") as destination_file:
                while True:
                    chunk = source_file.read(1024) # read in chhunk
                    if not chunk:
                        break
                    destination_file.write(chunk)
            print(f"Image copied successfully from {source_path} to {destination_path}!")
    except FileNotFoundError:
        print(f"Error: Source file '{source_path} not found'")
    except Exception as e:
        print("an error occured: ",e)

copy_image("./images/4.3.png","./images/4.3_copy.png")