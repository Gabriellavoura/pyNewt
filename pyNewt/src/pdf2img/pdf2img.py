import os
import fitz
from pathlib import Path

# Make temp directory
tmp_path = Path(__file__).parent / "tmp"
Path(tmp_path).mkdir(parents=True, exist_ok=True)


class Pdf2Img:

    def __init__(self, file_path, dpi=300):
        self.path = file_path
        self.dpi = dpi
        self.zoom = fitz.Matrix(self.dpi/72, self.dpi/72)

    # OpenPDF file
    def openPDF(self):
        self.doc = fitz.open(self.path)
        return self

    # Extract the image from pdf
    def extractPage(self):
        for page_index, page in enumerate(self.doc):
            pix = page.getPixmap()
            pix.writeImage(str(tmp_path) + '/' + "page-%i.png" % page.number)

    # Remove temp files
    def deleteTmpFiles(self):
        for file in tmp_path.glob('*'):
            if file.is_file():
                Path.unlink(file)
                print(file)
            else:
                deleteTmpFiles(file)
                Path.rmdir(file)


# if __name__ == "__main__":

#     file = "G:\\fun\\pyNewt\\pyNewt\\src\\pdf2img\\test.pdf"

#     test = Pdf2Img(file)
#     test.openPDF()
#     test.extractPage()
#     test.deleteTmpFiles()
