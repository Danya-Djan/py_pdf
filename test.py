import fpdf
import os
import datetime
fpdf.set_global("SYSTEM_TTFONTS", os.path.join(os.path.dirname(__file__),'font'))

class CustomPDF(fpdf.FPDF):

	def __init__(self, group_number, fio, phone_number, *args, **kwargs):
		self.fio = fio
		self.group_number = group_number
		self.phone_number = phone_number
		super().__init__(*args, **kwargs)
 
	def header(self):
		self.add_font('DejaVuSerif', '', 'DejaVuSerif.ttf', uni=True)
		self.set_font('DejaVuSerif', '', 12)

		self.cell(100)
		self.cell(0, 5, 'Директору школы ФРКТ', ln=1)
		self.cell(100)
		self.cell(0, 5, 'Гаврилову Дмитрию Александровичу', ln=1)
		self.cell(100)
		self.cell(0, 5, f'от студента  {self.group_number} группы', ln=1)
		self.cell(100)
		self.cell(0, 5, f'{self.fio}', ln=1)
		self.cell(100)
		self.cell(0, 5, f'тел: {self.phone_number}', ln=1)
 
		self.ln(20)
 
 
def create_pdf(pdf_path, group_number, fio, phone_number):
	current_date = datetime.datetime.now()
	current_date_string = current_date.strftime('%d/%m/%Y')
	pdf = CustomPDF(group_number, fio, phone_number)
	# Создаем особое значение {nb}
	pdf.add_page()
	pdf.add_font('DejaVuSerif', '', 'DejaVuSerif.ttf', uni=True)
	pdf.set_font('DejaVuSerif', '', 12)
	pdf.cell(200, 10, txt="Заявление", ln=1, align="C")

	pdf.set_font('DejaVuSerif', '', 10)
	pdf.write(5, "Прошу оказать мне материальную помощь по причине покупки билетов домой.")
	pdf.ln(25)
	pdf.write(5, f"{current_date_string} _________________ / ______________")
	pdf.ln(5)
	pdf.write(5, "                        (подпись)      (расшифровка)")

	pdf.ln(25)
	pdf.write(5, "Решение стипендиальной комиссии: материальную помощь назначить / не назначать")
	pdf.ln(15)
	pdf.write(5, "«____» _______ 20__ г. _________________ / ______________")
	

	pdf.output(pdf_path)
 
if __name__ == '__main__':
	group_number = input("Введите номер группы: ")
	fio = input("Введите ФИО: ")
	phone_number = input("Введите номер телефона: ")
	create_pdf(f'{fio}.pdf', group_number, fio, phone_number)