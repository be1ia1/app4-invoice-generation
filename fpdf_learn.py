from fpdf import FPDF

headers = ['Product ID', 'Product Name', 'Amount',
           'Price per Unit', 'Total Price']
pdf = FPDF(orientation='P', unit='mm', format='A4')

pdf.add_page()
pdf.set_font('Arial','B',12)

# top = pdf.y
# offset = pdf.x + 50

# for header in headers:
# offset = pdf.x + 50
# print(top, offset)
# print(pdf.y, pdf.x)
top = pdf.y
offset = pdf.x 
cell_w = 35
i = 1
for header in headers:
    pdf.multi_cell(w=cell_w, h=10, txt=header, border=1, align='L')
# print(pdf.y, pdf.x)
    step = cell_w * i
    pdf.y = top
    pdf.x = offset + step
    i += 1
# print(pdf.y, pdf.x)
# pdf.multi_cell(w=cell_w, h=10, txt=headers[1], border=1, align='L')
# print(pdf.y, pdf.x)
# pdf.y = top
# pdf.x = offset + 100
# pdf.multi_cell(w=cell_w, h=10, txt=headers[2], border=1, align='L')
# pdf.multi_cell(w=50, h=10, txt=headers[1], border=1, align='L')
# print(pdf.y, pdf.x)
# print(top, offset)
# pdf.multi_cell(100,10,headers[1],1,0)

# pdf.multi_cell(100,10,'This cell needs to beside the other',1,0)

pdf.output('tuto1.pdf','F')

# webbrowser.open_new('tuto1.pdf')