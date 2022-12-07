# Control ON-OFF según parámetros para riego dependiendo del tratamiento de suelo

## 1. Programa

Se crearon funciones para la recolección de los datos dependiendo del tratamiento para el control del riego:

- Activar_linea
- Desactivar_linea
- Manejo_outliers
- Lectura_0F_con_promedios
- Lectura_1F_con_promedios
- Lectura_2F_con_promedios
- Lectura_bc_con_promedios  
- Lectura_bccom_con_promedios
- Analisis_de_condiciones

### Parámetros

- url: es la dirección por la cual se realizan las operaciones por medio del API.
- valores: lista para guardado de valores operado en distintas secciones del programa.
- valores1: lista para guardado de valores operado en distintas secciones del programa.
- baja_humedad: representa el límite inferior de valor de humedad, si se encuentra por debajo de este valor se activará la línea.
- alta_humedad: representa el límite superior de valor de humedad, si se encuentra por encima de este valor se desactivará la línea.
- sleep_time: representa el tiempo que se esperará para volver a revisar los datos y decidir si se activan o no ciertas líneas.
- delay_time: es un retardo después del encendido de una línea.


### 1.1 Activar_linea

- Esta función se encarga de encender una línea de riego, a través de una solicitud a la base de datos.


##### Encabezado de la función.

```Python
def activar_linea(numero_linea):
```

##### Entradas

- `numero_linea`: representa el número de línea que se activará.

##### Salidas

- `requests.get(url+command)`: ejecuta la solicitud al servidor de encendido del número de línea establecido.

### 1.2 Desctivar_linea

- Esta función se encarga de apagar una línea de riego, a través de una solicitud a la base de datos.


##### Encabezado de la función.

```Python
def desactivar_linea(numero_linea):
```

##### Entradas

- `numero_linea`: representa el número de línea que se desactivará.

##### Salidas

- `requests.get(url+command)`: ejecuta la solicitud al servidor de apagado del número de línea establecido.

### 1.3 Manejo_outliers

- Esta función se encarga de detectar un valor outlier para no ser considerado al momento de promediar los datos y decidir si se debe o no encender una línea de tratameinto. Tome en cuenta que son necesarios tres valores diferentes de "None" para poder identificar un outlier.


##### Encabezado de la función.

```Python
 def manejo_outliers(x,y,z,cm1,cm2,cm3):
```

##### Entradas

- `x`: representa el primer valor de una maceta.
- `y`: representa el segundo valor de una maceta.
- `z`: representa el tercer valor de una maceta.
- `cm1`: representa el número de la primera maceta.
- `cm2`: representa el número de la segunda maceta.
- `cm3`: representa el número de la tercera maceta.


##### Salidas

- `lista`: devuelve los valores que entraron si alguno representaba un outlier se regresa ese valor como un "None".


### 1.4 Lectura_0F_con_promedios

- Esta función se encarga de recolectar los datos de las macetas con tratamiento 0F y promediarlos.


##### Encabezado de la función.

```Python
 def lectura_0F_con_promedios():
```

##### Entradas

- Últimos datos de humedad de las macetas 23,24,25 Caja I sensor(es) ABC(1,2,3).
- Últimos datos de humedad de las macetas 33,34,35 Caja K sensor(es) CBA(3,2,1).
- Últimos datos de humedad de las macetas 45,46,47 Caja M sensor(es) A(1) y Caja N sensor(es) ED(5,4).


##### Salidas

- `prom_prom`: devuelve el valor del promedio de los promedios de los 3 grupos de 3 macetas.

### 1.5 Lectura_1F_con_promedios

- Esta función se encarga de recolectar los datos de las macetas con tratamiento 1F y promediarlos.

##### Encabezado de la función.

```Python
 def lectura_1F_con_promedios():
```

##### Entradas

- Últimos datos de humedad de las macetas 26,27,28 Caja I sensor(es) E(5) y Caja J sensor(es) ED(5,4).
- Últimos datos de humedad de las macetas 41,42,43 Caja L sensor(es) CBA(3,2,1).
- Últimos datos de humedad de las macetas 53,54,55 Caja O sensor(es) CBA(3,2,1).

##### Salidas

- `prom_prom`: devuelve el valor del promedio de los promedios de los 3 grupos de 3 macetas.

### 1.6 Lectura_2F_con_promedios

- Esta función se encarga de recolectar los datos de las macetas con tratamiento 2F y promediarlos.

##### Encabezado de la función.

```Python
 def lectura_2F_con_promedios():
```

##### Entradas

- Últimos datos de humedad de las macetas 37,38,39 Caja M sensor(es) DE(4,5) y Caja J sensor(es) C(3).
- Últimos datos de humedad de las macetas 50,51,52 Caja N sensor(es) A(1) y Caja O sensor(es) ED(5,4).

##### Salidas

- `prom_prom`: devuelve el valor del promedio de los promedios de los 2 grupos de 3 macetas.

### 1.7 Lectura_bc_con_promedios

- Esta función se encarga de recolectar los datos de las macetas con tratamiento BC y promediarlos.

##### Encabezado de la función.

```Python
def lectura_bc_con_promedios():
```

##### Entradas

- Últimos datos de humedad de las macetas 17,22,36,40,49 Caja I sensor(es) D(4), Caja K sensor(es) E(5), Caja M sensor(es) C(3), Caja L sensor(es) D(4) y Caja N sensor(es) B(2).

##### Salidas

- `prom_prom`: devuelve el valor del promedio de las 5 macetas.

### 1.8 Lectura_bccom_con_promedios

- Esta función se encarga de recolectar los datos de las macetas con tratamiento BC+COM y promediarlos.

##### Encabezado de la función.

```Python
def lectura_bccom_con_promedios():
```

##### Entradas

- Últimos datos de humedad de las macetas 32,44,48 Caja K sensor(es) D(4), Caja M sensor(es) B(2) y Caja N sensor(es) C(3).

##### Salidas

- `prom_prom`: devuelve el valor del promedio de las 3 macetas.

### 1.9 Analisis_de_condiciones

- Esta función se encarga de recolectar los datos y compararlos con los parámetros para tomar las deciones sobre si se encienden las líneas o no.


##### Encabezado de la función.

```Python
 def analisis_de_condiciones():
```

##### Entradas

- `baja humedad`: representa el límite inferior de valor de humedad, si se encuentra por debajo de este valor se activará la línea.
- `alta humedad`: representa el límite superior de valor de humedad, si se encuentra por encima de este valor se desactivará la línea.


##### Salidas

- `numero_linea`: representa la línea a encender.

