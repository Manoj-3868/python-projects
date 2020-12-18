import pyttsx3
import PyPDF2
book = open('18CS51.pdf','rb')
pdfReader =PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker =pyttsx3.init()
for num in range(0,pages):
    pa = pdfReader.getPage(num)
    text = pa.extractText()
    speaker.say(text)
    speaker.runAndWait()