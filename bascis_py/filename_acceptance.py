from distutils import extension


filename=input("Enter the filename")
new_filename=filename.split(".")
extension=new_filename[1]
print("Extension:",extension)