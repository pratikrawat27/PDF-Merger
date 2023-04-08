import PyPDF2 as pdf

pdffile = ["1.pdf","2.pdf"]
merger = pdf.PdfMerger()

for filename in pdffile:
    pdfFile = open(filename, 'rb')
    pdfReader = pdf.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write("merged.pdf")