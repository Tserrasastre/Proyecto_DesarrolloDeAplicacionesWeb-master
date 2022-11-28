import json



#Guardamos la informacion de html.content en html_file y lo abrimos como index.html
def Html_py(items):
    #título
    html_content = f"""
     <!DOCTYPE html>
    <html>
    <head>
        <title>Rent Bike Mallorca</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="../css/newcss.css" type="text/css"/>
    </head>
    
    <body>
        <svg viewbox="0 0 100 20">
        <defs>
        <linearGradient id="gradient" x1="0" x2="0" y1="0" y2="1">
        <stop offset="5%" stop-color="#326384"/>
        <stop offset="95%" stop-color="#123752"/>
        </linearGradient>
        <pattern id="wave" x="0" y="0" width="120" height="20" patternUnits="userSpaceOnUse">
        <path id="wavePath" d="M-40 9 Q-30 7 -20 9 T0 9 T20 9 T40 9 T60 9 T80 9 T100 9 T120 9 V20 H-40z" mask="url(#mask)" fill="url(#gradient)"> 
        <animateTransform
            attributeName="transform"
            begin="0s"
            dur="1.5s"
            type="translate"
            from="0,0"
            to="40,0"
            repeatCount="indefinite" />
        </path>
        </pattern>
        </defs>
        <text text-anchor="middle" x="50" y="15" font-size="17" fill="url(#wave)"  fill-opacity="0.6">RENT BIKE</text>
        <text text-anchor="middle" x="50" y="15" font-size="17" fill="url(#gradient)" fill-opacity="0.1">RENT BIKE</text>
        </svg>
    """
    #recoremos los json 
    for item in items:

        html_content +="""
        <div id="contenedor">
            <a id="link" href="PaginasIndividuales/{serial}.html">
                <div class="A">
                    <div class=""> 
                        <img class="img" src="https://contents.mediadecathlon.com/p2091636/k$cc0790528e1a07724f38362c6dc52705/sq/bicicleta-de-montaa-29-aluminio-ntt-sport-60-rojo.jpg?format=auto&f=800x0">
                        <p id="divText">{brand}: {model}</p>
                    </div>
                </div>
            </a>
        </div>
    </body>
    </html>""".format(model = item.get('model'),brand = item.get('brand'),serial = item.get('serial'))
            

    escribirHTML("index",html_content)

def CrearPaginasIndividuales(items):
    for item in items:

        html_content = f"""
     <!DOCTYPE html>
    <html>
    <head>
        <title>Rent Bike Mallorca</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="../../css/newcss.css" type="text/css"/>
    </head>
    
    <body>
        <svg viewbox="0 0 100 20">
        <defs>
        <linearGradient id="gradient" x1="0" x2="0" y1="0" y2="1">
        <stop offset="5%" stop-color="#326384"/>
        <stop offset="95%" stop-color="#123752"/>
        </linearGradient>
        <pattern id="wave" x="0" y="0" width="120" height="20" patternUnits="userSpaceOnUse">
        <path id="wavePath" d="M-40 9 Q-30 7 -20 9 T0 9 T20 9 T40 9 T60 9 T80 9 T100 9 T120 9 V20 H-40z" mask="url(#mask)" fill="url(#gradient)"> 
        <animateTransform
            attributeName="transform"
            begin="0s"
            dur="1.5s"
            type="translate"
            from="0,0"
            to="40,0"
            repeatCount="indefinite" />
        </path>
        </pattern>
        </defs>
        <text text-anchor="middle" x="50" y="15" font-size="17" fill="url(#wave)"  fill-opacity="0.6">RENT BIKE</text>
        <text text-anchor="middle" x="50" y="15" font-size="17" fill="url(#gradient)" fill-opacity="0.1">RENT BIKE</text>
        </svg>

        <div id="contenedor">
            <a id="link" href="../PaginasTablas/{item.get('serial')}.html">
                <div class="A">
                    <div class=""> 
                        <img class="img" src="https://contents.mediadecathlon.com/p2091636/k$cc0790528e1a07724f38362c6dc52705/sq/bicicleta-de-montaa-29-aluminio-ntt-sport-60-rojo.jpg?format=auto&f=800x0">
                        <p id="divText">{item.get('brand')}:{item.get('model')}</p>
                    </div>
                </div>
            </a>
        </div>
    </body>
    </html>"""


    escribirHTML("PaginasIndividuales/" + item.get('serial'), html_content) 
        
def TablaHtml(element):
    # element = items[0]
    aux = """
    <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta lang="en">
                <title>BIKER'S CLUB</title>
            </head>
            <body>
                <section id="bicicletas_carretera">
                    <h1> Professional Road Bikes</h1>
                    <p>
                        <table class="default">
                            <colgroup>
                                <col span="1" style="background-color: #79b8db">
                            </colgroup>
    """

    for k, v in element.items():
        aux += """
                        <tr>
                            <td><b>%s</b></td>
                            <td>%s</td>
                        </tr>
        """ % (k, v)

    aux += """
        </table>
                    <img src="https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dwfdcff3fc/images/full/full_2022_/2022/full_2022_ultimate-cf-sl-7-disc_3072_gy-bk_P5.png" alt="foto Ultimate CF SL 7 Disc" height="100px" weight="px">
                </p>
            </section>
        </body>
    </html>
    """
    escribirHTML("PaginasTablas/"+ element.get('serial'),aux)

def escribirHTML(nombre, contenido):
    
    with open("html/" + nombre + ".html", "w+") as html_file:
        html_file.write(contenido)
        print ("HTML file " + nombre + " created successfully")

#Guardamos el diccionario como una variable
#recorremos el diccionario para extraer el valor de una 'Key' y la guardamos en una variable.
def cargarDatos(ruta='DataBase/AllBikes.json'):
    with open(ruta) as contenido:
        jsondoc = json.load(contenido)
        mainkey = jsondoc.get('documents')
        return mainkey


if __name__== '__main__':
    from ApiMongoDB import ApiMongoDB
    ApiMongoDB()
    
    items = cargarDatos()
    
    Html_py(items)

    CrearPaginasIndividuales(items)
    
    for item in items:
        TablaHtml(item)
    # TablaHtml(items)

    







                

