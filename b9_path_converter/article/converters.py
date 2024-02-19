from django.urls import converters,register_converter

class CategoryConverter():
	regex = r'\w+|(\w+\+\w+)+'

	def to_python(self,value):
		# Turn python+django+flask to ['python','django','flask'] 
		result = value.split("+")
		return result

	def to_url(self, value):
		# Turn ['python','django','flask'] to python+django+flask
		if isinstance(value,list):
			result = "+".join(value)
			return result
		else:
			raise RuntimeError("The type of the parameter should be list")



register_converter(CategoryConverter,'categ')