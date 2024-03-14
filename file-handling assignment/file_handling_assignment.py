try:
    # Create a new text file named "my_file.txt" in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Write at least three lines of text to the file
        file.write("this is assignment on reading and writing files in python 1\n")
        file.write("and it is week 6 \n")
        file.write("we use read , write , seek functions in file handling\n")
        print("File created successfully.")
except PermissionError:
    print("Permission denied. Check file permissions.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File creation process completed.\n")


# File Appending
try:
    # Open "my_file.txt" in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text to the existing content
        file.write("this is additional lines for the my_file.txt 4\n")
        file.write("it is acutaly week 7 at plp\n")
        file.write("appending more data to the file\n")
    print("Data appended successfully.")
except PermissionError:
    print("Permission denied. Check file permissions.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File appending process completed.")