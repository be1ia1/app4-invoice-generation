from fpdf import FPDF

headers = ['product_id', 'product_name'] #,'amount_purchased','price_per_unit','total_price']

pdf = FPDF(orientation='P', unit='mm', format='A4')

pdf.add_page()
pdf.set_font('Arial','B',16)

top = pdf.y
offset = pdf.x + 50

for header in headers:
# offset = pdf.x + 50
# print(top, offset)
    pdf.multi_cell(50,10,header,1,0)
    pdf.y = top
    pdf.x = offset 
# print(top, offset)
# pdf.multi_cell(100,10,headers[1],1,0)

# pdf.multi_cell(100,10,'This cell needs to beside the other',1,0)

pdf.output('tuto1.pdf','F')

# webbrowser.open_new('tuto1.pdf')