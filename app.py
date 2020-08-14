from flask import Flask,render_template,send_from_directory,jsonify

app = Flask(__name__)

'''
Aplicacion para generar arboles de habilidad automáticamente y poder estudiar resumenes de las habilidades de youtube 

Pasos para app:
1) Fetch de youtube los mejores 20 tutoriales de un --topico--
2) Entender el estado del usuario
	- Aqui se sustituiria con un login para guardar un perfil que se actualzia conforme el uso de la app 
	  pero por ahora solamente te pregunta
2) Genera un arbol de conocimiento del tópico hasta primeros principios:
	Consideraciones técnicas:
	- Google Knowledge Graph Search API
	- Wikidata
	- Rankbrain
	- Google x Freebase
	- https://cayley.io/
3) Por cada nodo en el arbol de conocimiento, generar una transcripción automática
	- https://github.com/hathix/youtube-transcriber
4) Con el resumen puedes generar micro tests automáticos

Data Objective:
- 
- 

Testing:
A) Programación, Música, 

Global Scope Questions:
- Será posible acercars automáticamente al curriculo universitario automáticamente?

'''



@app.route('/')
def index():
	return render_template('index.html')

@app.route("/search", methods=["POST"])
def search():	
	'''
		- Genera un dicionario con los formularios que se obtienen en el request con las llaves iguales al nombre del formulairo pero en mayuscula para guardarse en la bd:
		{'Nombre':nombre,...}
		- El formulario está hecho para tener dentro la información previa del usuario 
	'''
	if request.method == "POST":
		try: 

			data = {}
			form = request.form


			for field in form: 
				try:
					if request.form[field] not in ['Ingresa Valor...','','Elegir categoría primero...']:  # Solo subir si no está vacio el formulario
						data[field[0].upper()+field[1:]] = request.form[field]
				except Exception as e:return str(e)#;print(str(request.form[field]))

			return(jsonify(data))
		except:return('Search Error')


##STATIC
@app.route('/js/<path:path>')
def send_js(path):
	return send_from_directory('static/js', path)
@app.route('/images/<path:path>')
def send_img(path):
	return send_from_directory('static/images', path)
@app.route('/css/<path:path>')
def send_css(path):
	return send_from_directory('static/css', path)
@app.route('/fonts/<path:path>')
def send_fonts(path):
	return send_from_directory('static/fonts', path)
@app.route('/favicons/<path:path>')
def send_icons(path):
	return send_from_directory('static/favicons', path)




# if __name__ == "__main__":
# 	app.run(debug=True)