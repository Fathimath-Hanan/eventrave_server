from PyPDF2 import PdfWriter, PdfReader
import io
import os

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor



class CertificateGenerator:
    
    @staticmethod
    def generate(data: dict, certemplate: str, horz: int, vert: int, fontname: str, fontsize: int, fontcolor: str):
        """
        Generate certificate for participants based on the provided data and template.

        Args:
            data (dict): A dictionary containing participant information.
            certemplate (str): The path to the certificate template file.
            horz (int): The horizontal position of the text on the certificate.
            vert (int): The vertical position of the text on the certificate.
            fontname (str): The name of the font to be used.
            fontsize (int): The size of the font.
            fontcolor (str): The color of the font in hexadecimal format.

        Returns:
            destination (str): The path to the generated certificate file.
        """
        path = "media/certificates"
        #create the certificate directory
        os.makedirs(path, exist_ok=True)

        # # register the necessary font
        pdfmetrics.registerFont(TTFont('myFont', fontname))

        # provide the excel file that contains the participant names (in column 'Name')

        name = data['name']
        event = data['event']
        position = data['position']
        id = str(data['id'])
        

        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)

        # the registered font is used, provide font size
        can.setFont("myFont", fontsize)

        # the font colour is set
        can.setFillColor(HexColor(fontcolor))

        # provide the text location in pixels
        can.drawCentredString(horz, vert, name + " - " + event + " - " + position)

        can.save()
        packet.seek(0)
        new_pdf = PdfReader(packet)

        # provide the certificate template
        existing_pdf = PdfReader(open(certemplate, "rb"))

        output = PdfWriter()
        page = existing_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)
        destination = path + os.sep + name + id + ".pdf"
        outputStream = open(destination, "wb")
        output.write(outputStream)
        outputStream.close()
        print("created " + name + id + ".pdf")
            
        return str(destination).replace("media/", "")


# CertificateGenerator.generate(data=[
#     {
#         "name": "Hanan"
#     },
#     {
#         "name": "Jane Doe"
#     }
# ],certemplate= "cert.pdf",horz= 420, vert=270,fontname= "certfont.ttf",fontsize= 50, 
#                               fontcolor="#000000")
