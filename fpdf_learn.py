from fpdf import FPDF
import pandas as pd

df = pd.read_excel('invoices/10001-2023.1.18.xlsx')

df = df.rename(columns={'product_id': 'Product ID', 'product_name': 'Product Name',
                        'amount_purchased': 'Amount', 'price_per_unit': 'Price per Unit',
                        'total_price': 'Total Price'})

empty_cells = df.shape[1] - 1
total_row = ['' for x in range(empty_cells)]
total_row.append(df['Total Price'].sum())
df.loc[len(df.index)] = total_row

pdf = FPDF(orientation='P', unit='mm', format='A4')

pdf.add_page()

top = pdf.y
offset = pdf.x 

# Table Header
pdf.set_font('Arial', 'B', 12)
for header in df:
    cell_w = 70 if header == 'Product Name' else 30
    pdf.multi_cell(w=cell_w, h=10, txt=header, border=1, align='L')
    pdf.y = top
    offset += cell_w
    pdf.x = offset

# Table content
pdf.set_font('Arial', '', 10)
for row in df.values[:2]:
    pdf.y += 10 
    pdf.x = 10
    top = pdf.y
    offset = pdf.x 
    for item in row:
        cell_w = 70 if len(str(item)) >= 8 else 30
        pdf.multi_cell(w=cell_w, h=10, txt=str(item), border=1, align='L')
        pdf.y = top
        offset += cell_w
        pdf.x = offset

# Table footer
pdf.y += 10 
pdf.x = 10
top = pdf.y
offset = pdf.x 
for index, row in enumerate(df.values[2]):
    cell_w = 70 if index == 1 else 30
    pdf.multi_cell(w=cell_w, h=10, txt=str(row), border=1, align='L')
    pdf.y = top
    offset += cell_w
    pdf.x = offset

pdf.output('tuto1.pdf','F')
