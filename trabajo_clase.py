#---------------------------------------------
#Script de python para probar en Git
#Autor: Mateo Jurado <rjuradoj@est.ups.edu.ec>
#Fecha: 04/05/2026
#Crea un programa que te pida nombre y edad 
#y genere una imagen
#---------------------------------------------
def main():
    nombre = input("¿Cuál es tu nombre?: ")
    apellido = input("¿Cuál es tu apellido?: ")
    edad = input("¿Cuál es tu edad?: ")
    edad = int(edad)
    
    print("\n--- DATOS DEL USUARIO ---")
    print("Hola", nombre, "gracias por ser parte de la community")
    print("Nombre: ", nombre)
    print("Apellido: ", apellido)
    print("Edad: ", edad)
    print("-------------------------\n")

    # Aquí metemos el dibujo
    print(r"""
,,,, 
             ,;) .';;;;',
 ;;,,_,-.-.,;;'_,|I\;;;/),,_
  `';;/:|:);{ ;;;|| \;/ /;;;\__
      L;/-';/ \;;\',/;\/;;;.') \
      .:`''` - \;;'.__/;;;/  . _'-._ 
    .'/   \     \;;;;;;/.'_7:.  '). \_
  .''/     | '._ );}{;//.'    '-:  '.,L
.'. /       \  ( |;;;/_/         \._./;\   _,
 . /        |\ ( /;;/_/             ';;;\,;;_,
. /         )__(/;;/_/                (;;'''''
 /        _;:':;;;;:';-._             );
/        /   \  `'`   --.'-._         \/
       .'     '.  ,'         '-,
      /    /   r--,..__       '.\
    .'    '  .'        '--._     ]
    (     :.(;>        _ .' '- ;/

    |      /:;(    ,_.';(   __.'
     '- -'"|;:/    (;;;;-'--'
           |;/      ;;(
 snd       ''      /;;|
                   \;;|
                    \/
""")

if __name__ == "__main__":
    main()
