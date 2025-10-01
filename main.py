from PIL import Image

myString = "Hello World"

def textToBinary(text):
    text += "/"
    binary = ''.join(format(ord(i), '08b') for i in text)
    return binary

def encodeImage(imagePath, text):
    img = Image.open(imagePath).convert("RGB")
    pixels = list(img.getdata())
    copyList = pixels.copy()
    current_pixel = 0
    i = 0

    while i != len(text):
        for j in range(3):
            if int(text[i]):
                if (pixels[current_pixel][j] %  2) == 0:
                    copyList[current_pixel] = list(copyList[current_pixel])
                    copyList[current_pixel][j] += 1 
            else:
                if (pixels[current_pixel][j] %  2) != 0:
                    copyList[current_pixel] = list(copyList[current_pixel])
                    copyList[current_pixel][j] += 1 
            i+=1
            if i==len(text):break
        img.putpixel((current_pixel % img.width, current_pixel // img.width), tuple(copyList[current_pixel]))
        current_pixel += 1

    img.save("encoded_image.png")


def decodeImage (path) :
    EightBitlist = []
    message = ""
    pixels = list(Image.open(path).convert("RGB").getdata())
    eightBitString = ""

    for i in range(len(pixels)):
        for j in range(3):
            if (pixels[i][j] % 2) != 0:
                eightBitString += "1"
            else: eightBitString += "0"
            if len(eightBitString) == 8: 
                EightBitlist.append(eightBitString)
                eightBitString = ""

    for i in range(len(EightBitlist)):
        currentChar = chr(int(EightBitlist[i], 2))
        if currentChar == "/": 
            print(message)
            break
        message += currentChar
        

encodeImage("./image/sample_image.jpg",textToBinary(myString))
decodeImage("./encoded_image.png")
