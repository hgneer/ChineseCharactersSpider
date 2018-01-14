from PIL import Image
import os

def main():
    path = os.curdir+"//Pictures_of_ChineseCharacter"
    files = os.listdir(path)
    number = 0
    for file in files:
        picture = Image.open(path+"//"+file)
        lists = file.split('.')
        picture_1 = picture.convert("1")
        picture_1.save(os.curdir+"//Pictures_Converted"+"//"+file)
        number += 1
        print(file,number)

if __name__ == '__main__':
    main()
