from import_export.formats import base_formats
from django.http import HttpResponse
from configuracion import models as conf
from random import randint


def render_bancolombia(dataset):
	filler = ''.rjust(15, ' ')
	filler_end = ''.rjust(149, ' ')
	descripcion = 'pago1'.ljust(10, ' ')
	tipo_pago = '255'
	fecha_transaccion = '20150501'.rjust(8, '0')
	secuencia_envio = str(randint(10, 99))
	configuracion = conf.Configuracion.objects.all().first()
	numero_registros = str(len(dataset)).rjust(6, '0')
	sumatoria_debitos = '00000000000000000'
	sumatoria_creditos = 0
	tipo_registro = '6'

	for nomina in list(dataset):
		sumatoria_creditos += nomina[7]
	#end for
	sumatoria_creditos = str(sumatoria_creditos)
	sumatoria_creditos = sumatoria_creditos.rjust(15, '0') + '00'

	if configuracion:
		nit = configuracion.nit
		nit = nit.rjust(15, '0')

		cuenta = configuracion.numero_cuenta
		cuenta = cuenta.rjust(11, '0')

		tipo_cuenta = configuracion.tipo_cuenta
	#end if

	export_text = '1' + nit + 'I' + filler + tipo_pago + descripcion + fecha_transaccion + secuencia_envio + fecha_transaccion + numero_registros + sumatoria_debitos + sumatoria_creditos + cuenta + tipo_cuenta + filler_end

	for nomina in list(dataset):
		cedula = nomina[1].ljust(15, ' ')
		
		nombre = (nomina[2] + ' ' +  nomina[3]).ljust(30, ' ')

		export_text += '\n' + tipo_registro + cedula + nombre
	#end for

	return HttpResponse(export_text, content_type='text/plain')
#en def

class Bancolombia(base_formats.Format):

	def get_title(self):
		return 'bancolombia'
	# end def

	def create_dataset(self, in_stream):
		return list(in_stream)
	# end def

	def export_data(self, dataset, **kwargs):
		return render_bancolombia(dataset)
	# end def

	def is_binary(self):
		return True
	# end def

	def get_read_mode(self):
		return 'rb'
	# end def

	def get_extension(self):
		return "txt"
	# end def

	def get_content_type(self):
		return 'text/plain'
	# end def

	def can_import(self):
		return False
	# end def

	def can_export(self):
		return True
	# end def
# end class