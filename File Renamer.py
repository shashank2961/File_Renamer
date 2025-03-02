""" 
This program lets users rename multiple files in a folder. 
It offers 3 options: adding a prefix to the file names, adding a suffix, or numbering the files in order.
"""
import os

class FileRenamer:
    def __init__(self, folder_path):
        # Initialize the folder path
        self.folder_path = folder_path
        
        # Clean up the path in case it's enclosed in quotes
        if folder_path[0] == '"' and folder_path[-1] == '"':
            self.folder_path = folder_path[1:-1]
        
        # Verify the existence of the folder
        if not os.path.exists(self.folder_path):
            print("Invalid folder path, please try again")
            exit()

        # Get the list of files in the folder
        self.files = os.listdir(self.folder_path)
        print(f"\nThere are {len(self.files)} files in this directory.")


    def add_prefix(self, prefix):
        # Adds prefix to each file
        for file in self.files:
            old_file_path = os.path.join(self.folder_path, file)
            new_file_name = f"{prefix}_{file}"
            new_file_path = os.path.join(self.folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        print("Prefix added to files.")

    def add_suffix(self, suffix):
        # Adds suffix to each file
        for file in self.files:
            old_file_path = os.path.join(self.folder_path, file)
            new_file_name = f"{file}_{suffix}"
            new_file_path = os.path.join(self.folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        print("Suffix added to files.")

    def sequence_files(self):
        # Adds a sequential number to each file
        for counter, file in enumerate(self.files, start=1):
            old_file_path = os.path.join(self.folder_path, file)
            new_file_name = f"{file}_{counter:03}"
            new_file_path = os.path.join(self.folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        print("Files sequenced.")

    def rename_sequence_files(self, name):
        # Adds a sequential number to each file
        for counter, file in enumerate(self.files, start=1):
            old_file_path = os.path.join(self.folder_path, file)
            new_file_name = f"{name}_{counter:03}"
            new_file_path = os.path.join(self.folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
        print("Files sequenced.")

    def yesorno(self):
        option = input("If you wish to rename all your files with sequentiation numbers, type 'Y'.\nIf you wish to keep the same name for your files and just add numbers, type 'N'.\nInput (Y/N): ")
        try:
            if option == "Y":
                yesinput = input("Please enter the revised name for your files: ")
                return self.rename_sequence_files(yesinput)
            if option == "N":
                return self.sequence_files()
            if option != "Y" or option != "N":
                raise ValueError
        except ValueError:
            print("Invalid input, enter either Y/N (including the capitalization)")
            self.yesorno()
            

    
    def run(self):
        """Main function to run the renaming options"""
        print("\nPlease view the following options:\n1. Add a prefix to your files.\n2. Add a suffix to your files.\n3. Sequenciate your files.")
        
        # Ensures user's input is valid
        try:
            option = int(input("\nEnter your option: "))
            if option > 3 or option < 1:
                raise ValueError
        except ValueError:
            print("Please enter a valid option.")
            exit()
        
        # Handle each variation based on user input
        if option == 1:
            prefix = input("\nPlease enter your desired prefix: ")
            self.add_prefix(prefix)
        elif option == 2:
            suffix = input("\nPlease enter your desired suffix: ")
            self.add_suffix(suffix)
        elif option == 3:
            self.yesorno()
        
        print("Successfully edited your files!")



# Main Execution
if __name__ == "__main__":
    folder_path = input("Please enter folder path: ")
    renamer = FileRenamer(folder_path)
    renamer.run()