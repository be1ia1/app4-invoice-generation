import glob
import os
import pandas as pd
from fpdf import FPDF

filepaths = glob.glob('invoices/*.xlsx')

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    # print(filepath)
    invoice_nr = (os.path.basename(filepath)).split('-')[0]
    invoice_date = (os.path.basename(filepath)).split('-')[1][:-5]
    empty_cell = df.shape[1] - 1
    total_row = ['' for x in range(empty_cell)]
    total_row.append(df['total_price'].sum())
    df.loc[len(df.index)] = total_row
    empty_cell = df.shape[1] - 1
    total_row = ['' for x in range(empty_cell)]
    total_row.append(df['total_price'].sum())
    df.loc[len(df.index)] = total_row
    column_names = ['Product ID', 'Product Name', 'Amount',
                    'Price per Unit', 'Total Price']
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font(family='Times', size=16, style='b')
    pdf.cell(w=50, h=8, ln=1, txt=f'Invoice nr. {invoice_nr}')
    pdf.cell(w=50, h=8, ln=1, txt=f'Date {invoice_date}')
    pdf.ln()

    top = pdf.y
    offset = pdf.x + 50
    cell_w = 50
    for name in column_names:
        pdf.multi_cell(cell_w, 12, name, border=1,align='L')
        pdf.y = top
        pdf.x = offset
        
    pdf.output(f'{invoice_nr}-{invoice_date}.pdf')