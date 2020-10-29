# MCOC2020-P3
  
# Informe sobre replicación de tesis de Contreras usando diferencias finitas 

# Introducción.
Los hormigones masivos se caracterizan por ser hormigones de gran volumen y se pueden encontrar en casi todas las obras construidas. Un factor de interés en este proyecto es la generación de calor que produce la hidratación del cemente, llegando a tener en el hormigón masivo distintos valores de temperaturas en el tiempo, llegando a durar días incluso.
El modelo a usar en esta entrega se basa en lo siguiente

![imagen](/ec1.PNG)

En el caso de este proyecto se usará una barra de 1 metro con condiciones de borde como se presentan a continuación
 
![imagen](/cond_borde.PNG)


# Resultados.

 Al plantear un código que imprimiera gráficos para distintas posiciones x en distintos intervalos de tiempo se obtienen los siguientes gráficos:
 
 ![imagen](/x=0.104.png)
 
 

![imagen](/x=0.208.png)
  
  
![imagen](/x=0.416.png)


Como se puede ver, el método es convergente para cualquier variación de tiempo dado.
