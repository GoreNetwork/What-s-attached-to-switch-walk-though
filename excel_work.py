from openpyxl import Workbook
from openpyxl.compat import range
from openpyxl.utils import get_column_letter

def write_excel_data(row,column,value,sheet):
	tmp = str(get_column_letter(column))+str(row)
	sheet[tmp] = value
	return column+1

