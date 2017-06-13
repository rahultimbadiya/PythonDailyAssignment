def ReadFromFile():
    fr = open("test.txt","r")
    content = fr.read()
    print(content)

def WriteToFile():
    fw = open("test.txt","w")
    fw.write("This is a test file")
    fw.close()

WriteToFile()
ReadFromFile()