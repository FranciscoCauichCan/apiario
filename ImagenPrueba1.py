#importar la libreria opencv
import cv2
import math

#cargar imagen a usar
imagen=cv2.imread('Liturgia.jpg',1)

#cantidad en que se va a recortar una imagen
numero=int(input("Indique el numero en el que quiere recortar la imagen:"))

#conocer tamaño y canales de imagen
(alto,ancho,canales)=imagen.shape
#print('Alto={}, Ancho={}, Canales={}'.format(alto,ancho,canales))

#recortar la imagen en el numero requerido en raiz cuadradas 4, 9, 16...
if((math.sqrt(numero))-(round(math.sqrt(numero)))==0.0):
    corteAlto=round(alto/math.sqrt(numero))
    corteAncho=round(ancho/math.sqrt(numero))
    nuevoAlto=0
    nuevoAncho=0
    contador=0
    while contador<round(math.sqrt(numero)):
        contador2=0
        while contador2<round(math.sqrt(numero)):
            recorte=imagen[nuevoAlto:(nuevoAlto+corteAlto),nuevoAncho:(nuevoAncho+corteAncho)]
            cv2.imshow('Prueba',recorte)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            nuevoAncho+=corteAncho
            contador2+=1
        nuevoAlto+=corteAlto
        nuevoAncho=0
        contador+=1
else:
    print()

"""while contador<numero:
    recorte=imagen[nuevoAlto:(nuevoAlto+corteAlto),nuevoAncho:(nuevoAncho+corteAncho)]
    cv2.imshow('Prueba',recorte)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    nuevoAlto+=corteAlto
    nuevoAncho+=corteAncho
    contador+=1"""

"""recorte=imagen[0:0,50:178]
cv2.imshow('Prueba',recorte)
cv2.waitKey(0)
cv2.destroyAllWindows()


#extraer componentes r, g, b de un solo pixel
(b,g,r)=imagen[275,433]
print('R={}, G={}, B={}'.format(r,g,b))"""

"""#extraer pixeles marcados
recorte=imagen[0:0,178:609]

#mostrar la imagen
cv2.imshow('Prueba',recorte)

#guardar la imagen
cv2.imwrite('Liturgia gris.jpg',imagen)

#tiempo de espera
cv2.waitKey(0)

#cerrar ventanas
cv2.destroyAllWindows()"""