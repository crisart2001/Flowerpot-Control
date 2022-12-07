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
- Switches

### 1.1 Activar_linea
- Esta función se encarga de encender una línea de riego, a través de una solicitud a la base de datos.


##### Encabezado de la función.

```Python
def activar_linea(numero_linea):
```

##### Parámetros

Este módulo no tiene parámetros

##### Entradas

- `clk_pi`: Clock
- `rst_pi`: Reset
- `PS2_Data_pi`: Data PS2
- `PS2_clk_pi`: Clock PS2
- `miso_pi`: MISO
- `sw_pi` : Switch

##### Salidas

- `locked_po`: Locked
- `tx_po`: Tansmission
- `cs_ctrl_po`: Chip Select
- `sck_po`: SCK
- `display_po`: Control para 7 segmentos
- `display_select_po`: Selector de display 7 segementos
- `rgb_po`: RGB
- `leds_po`: LEDs



##### Criterios de diseño
Este módulo es el módulo rpincipal en el cual se llaman al módulo del procesador y un módulo de programa externo

