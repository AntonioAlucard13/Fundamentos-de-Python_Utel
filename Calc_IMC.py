#### Calculo del Índice de Masa Corporal - Mostrando la clasificación del Peso. Al final debe de mostrarse el Valor del IMC y su clasificación correspondiente utilizando la formula: IMC = PESO / ALTURA²

## Si el IMC < 18.5 su clasificación es "Bajo de peso".
## Si el IMC > 18.6 e IMC < 24.9 su clasificación es "Peso ideal".
## Si el IMC > 25 e IMC < 29.9 su clasificación es "Peso levemente elevado"
## Si el IMC > 30 e IMC < 34.9 su clasificación es "Peso Elevado - Obesidad Grado 1"
## Si el IMC > 35 e IMC < 39.9 su clasificación es "Peso Elevado - Obesidad Grado 2"
## Si el IMC > 40 e IMC < 49.9 su clasificación es "Peso Elevado - Obesidad Grado 3".
## Si el IMC > 50 su clasificación es "Peso Elevado - Obesidad Grado 4".

from cgitb import text

# NOMBRE # APELLIDO PATERNO Y MATERNO

nombre = str(input('Escribe tu Nombre Completo: '))
while not nombre:
    print('El Nombre es Invalido, ingresa nuevamente tus datos...')
    nombre = str(input('Escribe tu Nombre Completo: '))

apellidop = str(input('Escribe tu Apellido Paterno: '))
while not apellidop.isalpha():
    print('El Apellido Paterno es Invalido, ingresa nuevamente tus datos...')
    apellidop = str(input('Escribe tu Apellido Paterno: '))

apellidom = str(input('Escribe tu Apellido Materno: '))
while not apellidom.isalpha():
    print('El Apellido Materno es Invalido, ingresa nuevamente tus datos...')
    apellidom = str(input('Escribe tu Apellido Materno: '))

# EDAD

edad = str(input('Escribe tu edad:'))
while not edad.isdigit():
    print('Valor incorrecto, solo ingrese número entero...')
    edad = str(input('Escribe tu edad:'))

# PESO

peso = float(input("Digíte su peso en Kilogramos: "))
while not peso:
    print('Valor incorrecto, digíte nuevamente su peso en Kilogramos...')
    peso = float(input("Digíte su peso en Kilogramos: "))

# ALTURA

altura = float(input("Digíte su Estatura en metros:"))
while not altura:
    print('Valor incorrecto, digíte nuevamente su Estatura en metros...')
    altura = float(input("Digíte su Estatura en metros:"))

# OPERACIONES

IMC = peso / altura **2

if IMC <= 18.5 :
    print("Bajo de Peso.")
elif IMC >= 18.6 and IMC <= 24.9 :
    print ("Peso ideal.")
elif IMC >= 25 and IMC <= 29.9 :
    print ("Peso Levemente elevado!.")
elif IMC >= 30 and IMC <= 34.9 :
    print ("Peso Elevado - Obesidad Grado 1! - Bajo Riesgo: Puedes desarrollar a corto plazo patologías graves como la diabetes, la hipertensión, las complicaciones cardiovasculares, especialmente la cardiopatía isquémica, e incluso algunos tipos de cáncer, como los gastrointestinales.")
elif IMC >= 35 and IMC <= 39.9 :
    print ("Peso Elevado - Obesidad Grado 2 - Riesgo Moderado: Puedes desarrollar afecciones graves como: Problemas cardíacos y accidentes cerebrovasculares.!!")
elif IMC >= 40 and IMC <= 49.9 :
    print ("Peso Elevado - Obesidad Grado 3 - Riesgo Alto: Puedes tener afecciones frecuentemente como hipertensión arterial, diabetes mellitus, cardiopatía coronaria, insuficiencia respiratoria y dislipidemia; además de lo anterior, pueden padecer limitaciones físicas para realizar actividades debido a problemas osteoarticulares derivados de la obesidad extrema!!!")
else :
    print ("Peso Elevado - Obesidad Grado 4 - Riesgo Extremo: Puedes presentar ataques cardíacos debido a enfermedad cardíaca coronaria, insuficiencia cardíaca y accidente cerebrovascular. Problemas óseos y articulares!!!")
print()
print('Gracias por utilizar la Cálculadora de IMC, hasta luego!')
