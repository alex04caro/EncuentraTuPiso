# Analizador de precios

Este proyecto es una herramienta en Python diseñada para extraer datos de inmuebles desde la página web de Tecnocasa, calcular el precio promedio por metro cuadrado de cada barrio, y comparar los precios de los pisos encontrados con ese promedio, ordenándolos según su relación calidad-precio.

## Características

- **Extracción de datos**: Dumpea información de pisos desde el sitio web de Tecnocasa.
- **Filtrado**: Permite definir rangos de precios, metros cuadrados y habitaciones.
- **Análisis de precios**: Calcula el precio promedio por metro cuadrado en cada barrio.
- **Comparación**: Ordena los pisos según la diferencia con el precio promedio del barrio.
- **Visualización**: Muestra los pisos que están por debajo de la media con su diferencia en precio.

## Requisitos

- **Python 3.8+**
- Librerías requeridas:
  - `requests`
  - `beautifulsoup4`
  - `lxml`

Puedes instalar las dependencias ejecutando:

```bash
pip install requests beautifulsoup4 lxml
```

## Uso

1. Clona este repositorio o copia el script en tu entorno local.
2. Ejecuta el script:

```bash

python script.py

```
3. Introduce los filtros que desees al iniciar el programa:

   - **Rango de precios**: Ejemplo: `100000-300000`.
   - **Rango de metros cuadrados**: Ejemplo: `50-100`.
   - **Rango de habitaciones**: Ejemplo: `2-4`.

   El programa buscará y analizará los pisos en base a los filtros proporcionados.

### Ejemplo de Salida

El programa mostrará algo como esto:

```bash

Se encontraron un total de 20 pisos

De los cuales estos son los que mejor están de precio ordenados de mejor a peor:

--------------------------------------------------------------------------------------------------------------------
Localización = Centro
Precio = 250,000 €
Metros = 80 m²
Habitaciones = 2
URL: https://www.tecnocasa.es/detalle/1234
Está 10,000 € por debajo de la media
--------------------------------------------------------------------------------------------------------------------
```
---

## Estructura del Código

### Clases

- **Piso**: Representa un inmueble con los siguientes atributos:
  - `localización`: Ubicación del piso.
  - `precio`: Precio del inmueble.
  - `metros`: Superficie en metros cuadrados.
  - `habitaciones`: Número de habitaciones.
  - `url`: Enlace al anuncio.
  - `diferencia`: Diferencia de precio respecto al promedio del barrio.

### Funciones principales

- **`extraerDatosTecnocasa(tecnocasaURL)`**: Extrae información de los pisos desde el sitio web de Tecnocasa.
- **`ordenDiferencia(piso)`**: Define el criterio de ordenación basado en la diferencia de precio y los metros cuadrados.
- **`banner()`**: Imprime un banner decorativo en la consola.

### Lógica principal

1. Construye la URL de búsqueda según los filtros introducidos por el usuario.
2. Extrae los datos de los pisos disponibles en todas las páginas de resultados.
3. Calcula el precio promedio por metro cuadrado en cada barrio.
4. Ordena los pisos según su diferencia respecto a la media y los muestra.