import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter

print("\n__________________________ PDF Splitter __________________________")
print("__________________________________________________________________")
print("__________________________________________________________________\n")
print("Paste the PDF document in the same folder as this program and rename it to 'sample.pdf'\nOnce rename is done, continue...\n")
input("To continue, press Enter ")

pdf = PdfFileReader("sample.pdf", "rb")
pgstart = int(input("Enter starting page No.: ")) - 1
pgend = int(input("Enter ending page No.: "))
print("Splitting Pages...")

for i in range(pgstart, pgend):
    writer = PdfFileWriter()
    writer.addPage(pdf.getPage(i))
    output = f"page {i+1}.pdf"
    with open("output/" + output, "wb") as out:
        writer.write(out)

print("\nPDF splittted Successfully\nOpen the output folder to view pages\n")
