Realize los endpoints del CRUD desde /titulares/ y tambien los separe en diferentes url segun tipo del titular, en '/titulares-fisicos/' y '/titulares-juridicos/' , pudiendose desde cada url solo hacer requests sobre el tipo de titular especificado en la url, mientras que en /titulares/ se pueden realizar requests sobre los dos tipos de titulares.


TITULARES (/titulares/):

GET REQUEST (all entries):
 curl -H "Accept: application/json" -u guido:guido http://localhost:8000/titulares/

GET REQUEST (single entry):
 curl -H "Accept: application/json" -u guido:guido http://localhost:8000/titulares/1/

POST REQUEST(create):
 curl -X POST -d "tipo_titular=juridico&año_fundacion=2020&razon_social=TecsoCoop&cuit=20-2020-20" -u guido:guido http://localhost:8000/titulares/

PUT REQUEST (update):
 curl -X PUT -d "tipo_titular=juridico&año_fundacion=2020&razon_social=pepito&cuit=201020" -u guido:guido http://localhost:8000/titulares/7/

DELETE REQUEST (delete):
 curl -X DELETE -u guido:guido http://localhost:8000/titulares/7/



TITULARES JURIDICOS (/titulares-juridicos/):

GET REQUEST (all entries):
 curl -H "Accept: application/json" -u guido:guido http://localhost:8000/titulares-juridicos/

GET REQUEST (single entry):
  curl -H "Accept: application/json" -u guido:guido http://localhost:8000/titulares-juridicos/4/

POST REQUEST(create):
 curl -X POST -d "año_fundacion=2020&razon_social=KORN&cuit=20-7-3" -u guido:guido http://localhost:8000/titulares-juridicos/

PUT REQUEST (update):
 curl -X PUT -d "año_fundacion=2020&razon_social=pepito&cuit=20-7-3" -u guido:guido http://localhost:8000/titulares-juridicos/7/

DELETE REQUEST (delete):
 curl -X DELETE -u guido:guido http://localhost:8000/titulares-juridicos/7/




TITULARES FISICOS (/titulares-fisicos/):

GET REQUEST (all entries):
 curl -H "Accept: application/json" -u guido:guido http://localhost:8000/titulares-fisicos/

GET REQUEST (single entry):
  curl -H "Accept: application/json" -u guido:guido http://localhost:8000/titulares-fisicos/1/

POST REQUEST(create):
 curl -X POST -d "nombre=Guido&apellido=valada&dni=41907849&cuit=20-8-3" -u guido:guido http://localhost:8000/titulares-fisicos/

PUT REQUEST (update):
 curl -X PUT -d "nombre=pepe&apellido=perez&dni=41907849&cuit=20-8-2" -u guido:guido http://localhost:8000/titulares-fisicos/8/

DELETE REQUEST (delete):
 curl -X DELETE -u guido:guido http://localhost:8000/titulares-fisicos/8/

