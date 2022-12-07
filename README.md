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

### 3.2 Módulo top_multicycle_processor
- Es el módulo encargado de llamar y llevar la sincronía de los demás módulos


##### Encabezado del módulo.

```Python
module top_multicycle_processor(
    
    input   logic               clk_pi,
                                rst_pi,
                                PS2Data_pi,
                                PS2Clk_pi,
                                miso_pi,
                    [15 : 0]    sw_pi,                
    output  logic               locked_po,
                                tx_po,
                                cs_ctrl_po,
                                sck_po,
                    [6 : 0]     display_po,
                    [7 : 0]     display_select_po,           
                    [2 : 0]     rgb_po,
                    [15 : 0]    leds_po                
    );
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

