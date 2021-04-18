# Webscraping: consiste en navegar automáticamente una web y extraer de ella información.
print("Webscraping\n")


# Importaremos las librerías necesarias para este código
import requests
import bs4 #Beautifulsoup


# Primero debemos solicitar una página web para entrar. Si no se tiene respuesta en 2 segundos, se suspenderá la ejecución. En este caso usaremos requests, url, text
pag1 = requests.get("http://pythonscraping.com/pages/page3.html", timeout=2)


# Mostrar el link de la página a utilizar
print ("\nEstamos analizando la página web:\n", pag1.url, "\n")


print()
# Mostrar contenido del link
#print("El contenido de la página es:\n",pag1.text)


print("----------"*7)
print()


# Ahora, para ver qué más podemos hacer con esto, construiremos un objeto de beautifulsoup con la información que tenemos de la página web con el cuál haremos algunos ejercicios. Como segundo argumento, agregaremos el tipo de parser a utilizar.
sopa1 = bs4.BeautifulSoup(pag1.text,  'html.parser')

# Haremos cada ejercicio con funciones de BeautifulSoup, para presentar todo el contenido, como para extraer algunas partes en especial

# Todo el contenido de la página web. Usamos la función select para tomar una etiqueta específica, como queremos tomar el contenido de la página web, esta información se encuentra en la etiqueta 'body', por lo que la llamamos y además específicamos el índice en la etiqueta. 
print(sopa1.select('body')[0].text)

print()
print("----------"*7)
print()

# Ejercicios
print("\nHaremos algunas extracciones de contenido específicas\n")

print()
# Obtener solo el título de la página. En este caso, el título se encuentra en la etiqueta <h1>.
print("- Título de la página:\n")
print(sopa1.h1.text)

print()
print()
print()
# Dentro de la estructura html de esta página web, hay un tabla, la cuál se encuentra en la etiqueta table y la mostraremos a continuación.
print("- Tabla de la página web:\n")
print(sopa1.table.text)


# En las descripciones de los items, hay una frase en letra cursiva, vamos a mostrar la frase correspondiente al primer item. Utilizaremos select, buscaremos la etiqueta(span)n mencionaremos la clase en la que está almacenada esta frase (excitingNote) y diremos que es la primera que sale de esta clase poniendo la posición 0
print("- Frase en cursiva del item 1:\n")
print(sopa1.select('span[class=excitingNote]')[0].text)

print()
print()
print()
# Podemos sacar información solamente de fila 3 de la tabla de la página web, para esto usamos select, buscamos la etiqueta de 'tr' (filas de la tabla - table row), mencionando el id de tal fila y la posición 0 de ese id
print("- Item 3 de la tabla:\n")
print(sopa1.select('tr[id=gift3]')[0].text)


# También podemos obtener únicamente la parte final de la página conocida como 'footer' que representa un pie de página. Para encontrarlo, buscamos en las secciones de 'div' la correspondiente al id = 'footer'. Usamos select y además la posición 0 para que muestre lo que tenemos allí.
print("- Pie de página del sitio web:\n")
print(sopa1.select('div[id=footer]')[0].text)
