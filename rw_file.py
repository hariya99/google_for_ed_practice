import os
print(os.getcwd())

curr_dir = os.getcwd()

def write_file():
    try:
        my_file = open('sample_file.txt', 'w')
        my_file.write('hi hi There There how are you\n')
        my_file.write('i am Good How Are you')
        my_file.close()
        print('data written successfully')
    except:
        ('Can not create a file in this directory')





def read_file():
    try:
        my_file = open('sample_file.txt', 'rU')
        for line in my_file:
            print(line)

    except:
        ('Can not create a file in this directory')

write_file()
read_file()
