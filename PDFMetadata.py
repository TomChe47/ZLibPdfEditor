import pikepdf, os

inDir = "D:/Book/New"
outDir = "D:/Book/Old"

pdfFileNameList = os.listdir(inDir)
for pdfFileName in pdfFileNameList:
    fileDir = inDir + "/" + pdfFileName

    #Delete All Metadata
    pdf = pikepdf.open(fileDir)
    try:
        del pdf.Root.Metadata
        del pdf.docinfo
    except:
        print("Clearing Metadata Problem")
    print("Metadata Cleared!")

    #Get BookName and Author
    pdfFileName = pdfFileName.replace(") (z-lib.org).pdf", "")
    bookInfo = pdfFileName.split(' (')
    BookName = bookInfo[0]
    BookName = BookName.title()
    Author = bookInfo[1]
    Author = Author.replace(";",",")
    print(BookName)
    print(Author)

    with pdf.open_metadata() as meta:
        meta['dc:creator'] = Author

    #Set New BookName
    newFileName = outDir + "/" + BookName + ".pdf"
    print(newFileName)
    print("\n")
    pdf.save(newFileName, fix_metadata_version=False)

