from import_export.formats import base_formats
from django.http import HttpResponse
from configuracion import models as conf
from random import randint


def render_bancolombia(dataset):
	export_text = '1'
	filler = ''.rjust(15, ' ')
	descripcion = 'pago1'.ljust(10, ' ')
	tipo_pago = '255'
	fecha_transaccion = '20150501'.rjust(8, '0')
	secuencia_envio = str(randint(10, 99))
	configuracion = conf.Configuracion.objects.all().first()
	numero_registros = str(len(dataset)).rjust(6, '0')
	sumatoria_debitos = '00000000000000000'
	if configuracion:
		nit = configuracion.nit
		export_text += nit.rjust(15, '0') + 'I' + filler + tipo_pago + descripcion + fecha_transaccion + secuencia_envio + fecha_transaccion + numero_registros + sumatoria_debitos
	#end if
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