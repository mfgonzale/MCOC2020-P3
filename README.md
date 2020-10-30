# MCOC2020-P3
  
# Informe sobre replicación de tesis de Contreras usando diferencias finitas 

# Introducción.
Los hormigones masivos se caracterizan por ser hormigones de gran volumen y se pueden encontrar en casi todas las obras construidas. Un factor de interés en este proyecto es la generación de calor que produce la hidratación del cemente, llegando a tener en el hormigón masivo distintos valores de temperaturas en el tiempo, llegando a durar días incluso. Se estima la difusión de calor de forma unidireccional (en el eje x) y que se difunde de forma simétrica, por lo que se toman tres nodos dentro del molde. Para estimar los valores de temperatura en el tiempo se simulará la difusión térmica usando diferencias finitas. Además se usará la serie de Fourier planteada en la tesis de Contreras para analizar la convergencia de las curvas. Además se busca realizar la discretización de las condiciones de borde naturales.

El modelo a usar en esta entrega se basa en la ecuación de difusión, que se ve como sigue:

![imagen](/ec1.PNG)

En el caso de este proyecto se usará una barra de 1 metro con condiciones de borde como se presentan a continuación
 
![imagen](/cond_borde.PNG)


# Resultados.

 Al plantear un código que imprimiera gráficos para distintas mallas en tres posiciones, las cuales son x = 0.104(m), x = 0.208 (m) y x = 0.416 (m), en distintos intervalos de tiempo se obtienen los siguientes gráficos:
 
 ![imagen](/x=0.104.jpeg)
 

![imagen](/x=0.208.jpeg)
  
  
![imagen](/x=0.416.jpeg)

Para realizar la discretización de las condiciones de borde naturales se generaron los casos de la primera columna con la condición derivada inicial planteada. Luego se arregló la formula en el formato u[k, n-2] = u[k, n-1] - 5k. Entonces para realizar ese cálculo se invirtió el recorrido de la matriz de derecha a izquierda, es decir, de N a 0.

# Conclusión

Como se puede ver, el método es convergente para cualquier variación de tiempo dado pues se encuentran cercanas a la curva proporcionada por la serie de Fourier. La variación resulta muy pequeña entre todas las curvas, por lo que puede confirmarse que si convergen. 
