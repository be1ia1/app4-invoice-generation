import glob
import pandas as pd
from fpdf import FPDF

filepaths = glob.glob('invoices/*.xlsx')

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    invoice_nr = (filepath.split('/')[1]).split('-')[0]
    invoice_date = (filepath.split('/')[1]).split('-')[1][:-5]
    empty_cell = df.shape[1] - 1
    total_row = ['' for x in range(empty_cell)]
    total_row.append(df['total_price'].sum())
    df.loc[len(df.index)] = total_row
    empty_cell = df.shape[1] - 1
    total_row = ['' for x in range(empty_cell)]
    total_row.append(df['total_price'].sum())
    df.loc[len(df.index)] = total_row
    column_names = [(x.replace('_', ' ')).title() for x in df.columns.values]
    print(column_names)
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font(family='Times', size=16, style='b')
    pdf.cell(w=50, h=8, ln=1, txt=f'Invoice nr. {invoice_nr}')
    pdf.cell(w=50, h=8, ln=1, txt=f'Date {invoice_date}')
    pdf.ln()
    # for row in df
    pdf.output(f'{invoice_nr}-{invoice_date}.pdf')