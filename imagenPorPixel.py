#importar la libreria opencv y la libreria math, para el uso del redondeo para abajo que servirá más adelante
import cv2, math, tkinter, os
from tkinter import filedialog

#esto se hace solo para eliminar la ventanita de Tkinter 
root = tkinter.Tk()
root.withdraw() #ahora se cierra

#abre el explorador de archivos y guarda la seleccion en la variable
ruta_archivo = filedialog.askopenfilename()

#se crea una lista que contenga datos divididos por el punto para el formato
formato=ruta_archivo.split('.')

#se guarda el formato del archivo en una variable
formato_archivo=formato[len(formato)-1]


#comprobar si el archivo seleccionado es una imagen
if (formato_archivo=='jpg' or formato_archivo=='JPG' or formato_archivo=='PNG'or formato_archivo=='png' or formato_archivo=='JPEG' or formato_archivo=='jpeg'):
    
    #divide la ubicación para conseguir el nombre del archivo
    ruta_divida = ruta_archivo.split('/')

    #se divide el nombre para que no te tome el formato de imagen y solo sea el nombre
    dividir_nombre = ruta_divida[len(ruta_divida)-1].split('.')

    #se guarda el nombre del archivo en una variable
    nombre_archivo = dividir_nombre[len(dividir_nombre)-2]

    #cargar imagen a usar
    imagen=cv2.imread(ruta_archivo,1)
    
    #conocer tamaño y canales de imagen
    (alto,ancho,canales)=imagen.shape
    #print('La imagen contiene en pixeles Alto={}, Ancho={}'.format(alto,ancho))

    #cantidad en que se va a recortar una imagen
    nal=int(input("Indique el numero de pixeles de ALTO en el que quiere recortar la imagen:"))
    nan=int(input("Indique el numero de pixeles de ANCHO en el que quiere recortar la imagen:"))

    #verificar si es posible recortar la imagen de la forma en que desea el usuario
    if(alto>nal and ancho>nan):
        
        #si es posible entonces se hará el recorte de la imagen
        #Se crea un directorio donde se va a guardar los recortes que se harán en la ubicación donde se encuentra el archivo python
        os.makedirs('Recortes', exist_ok=True)

        #Se guarda en una variable la ubicación actual del archivo y se concatena con el nombre de la nueva carpeta
        guardar = os.getcwd()+'\Recortes'

        #Aquí se hace todo el recorte de las imágenes
        nuevoAlto=0
        nuevoAncho=0
        contador=0
        contadorI=1
        while contador<math.floor(alto/nal):
            contador2=0
            while contador2<math.floor(ancho/nan):
                recorte=imagen[nuevoAlto:(nuevoAlto+nal),nuevoAncho:(nuevoAncho+nan)]
                nombre=nombre_archivo+str(contadorI)+'.jpg'
                cv2.imwrite(os.path.join(guardar,nombre),recorte)
                cv2.destroyAllWindows()
                nuevoAncho+=nan
                contador2+=1
                contadorI+=1
            nuevoAlto+=nal
            nuevoAncho=0
            contador+=1

    else:
        print('Los pixeles dados exceden a los de la imagen, no es posible hacer el recorte')

else:
    print ('No es un archivo de imagen, imposible continuar')
