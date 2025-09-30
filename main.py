from PIL import Image

myString = "HelloWorld"

def textToBinary(text):
    binary = ''.join(format(ord(i), '08b') for i in text)
    return binary

def encodeImage(imagePath, text):
    img = Image.open(imagePath)
    img = img.convert("RGB")
    pixels = list(img.getdata())

    copyList = pixels.copy()
    """for i in range(len(text)):
        for j in range(2):
            if int(text[i]):
                print("1")
                if (pixels[i][j] %  2) == 0:
                    print("odd", i, j)
                    copyList[i] = list(copyList[i])
                    copyList[i][j] += 1
            else:
                print("0")
                if (pixels[i][j] %  2) != 0:
                    print("even")
                    copyList[i] = list(copyList[i])
                    copyList[i][j] += 1"""
    
            

    
    
    
    
    
    #img.putpixel((i % img.width, i // img.width), (255, 255, 255)) 
    #img.save("encoded_image.png")


    print(text)
    print(pixels[:len(text)],"\n")
    print(copyList[:len(text)])
    """img = Image.open("./encoded_image.png")
    img = img.convert("RGB")
    pixels = list(img.getdata())"""
    
    


encodeImage("./image/sample_image.jpg",textToBinary(myString))