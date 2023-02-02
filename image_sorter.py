# imports
import fileinput
import shutil
import os

# DataFolder paths
resource_dir = "resources/"
image_sets_folder = resource_dir + "image_sets/"
images_folder = resource_dir + "images/"

# Get the list of all files and directories
dir_list = os.listdir(image_sets_folder)


def get_files_lines():
    for file in dir_list:
        count = 0
        for line in fileinput.input(files=image_sets_folder + file):
            if line.split(" ")[0] and line.split(" ")[0].strip(" \n"):
                count += 1
                print("Nya: " + line.split(" ")[1].strip(" \n"))
                print("L: " + line)
                if not line.split(" ")[len(line.split(" ")) - 1].strip(" \n") == '-1':
                    if not os.path.exists(resource_dir + file.split("_")[0]):
                        os.mkdir(resource_dir + file.split("_")[0])
                    if not os.path.exists(resource_dir +
                                          file.split("_")[0] + "/" + line.split(" ")[0].strip(" \n") + ".png"):
                        if os.path.exists(images_folder + line.split(" ")[0].strip(" \n") + ".png"):
                            shutil.move(images_folder + line.split(" ")[0].strip(" \n") + ".png",
                                        resource_dir + file.split("_")[0])
                            print("File Name: " + file)
                            print("Line " + str(count) + ": " + line.split(" ")[0].strip(" \n"))


if __name__ == '__main__':
    get_files_lines()
