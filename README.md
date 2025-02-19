# **Escáner de Subdominios**

Este es un **escáner de subdominios** simple y eficiente desarrollado en **Python**. Utiliza **múltiples hilos** para escanear rápidamente subdominios de un dominio objetivo. El programa busca subdominios en un archivo de texto llamado `Subdominios.txt` y muestra los resultados en la consola, con la opción de guardarlos en un archivo.

## **Archivos Requeridos**

Asegúrate de que los siguientes archivos estén en la misma ruta que el script Python:

1. **`subdomain_scanner.py`**: El archivo principal del script que ejecuta el escaneo de subdominios.
2. **`Subdominios.txt`**: Un archivo de texto que contiene una lista de subdominios a verificar. Cada subdominio debe estar en una línea separada. Por ejemplo:

    ```
    www
    mail
    blog
    api
    ```

## **Características**

- **Escaneo rápido** utilizando múltiples hilos.
- Verifica si los **subdominios existen** en el dominio objetivo.
- **Opción para guardar los resultados** en un archivo de texto.
- Soporta tanto **HTTP** como **HTTPS**.

## **Requisitos**

Asegúrate de tener instalado **Python 3** y las siguientes dependencias:

- **`requests`**: para hacer las solicitudes HTTP.
- **`argparse`**: para gestionar los argumentos desde la línea de comandos.
- **`concurrent.futures`**: para manejar la ejecución en múltiples hilos.

Puedes instalar las dependencias utilizando **pip**:

```bash
pip install requests
```

## **Uso**

Para ejecutar el escáner, utilice la siguiente sintaxis en la línea de comandos:

- **Escanear subdominios sin guardar los resultados**:

```bash
python subdomain_scanner.py -t example.com
```

- **Escanear subdominios y guardar los resultados en un archivo**:

```bash
python subdomain_scanner.py -t example.com -o resultados.txt
```

### **Explicación de los Argumentos**:

- `-t` o `--target`: El dominio objetivo que deseas escanear (por ejemplo, `example.com`).
- `-o` o `--output`: Archivo donde se guardarán los resultados encontrados. Si no se especifica, los resultados no se guardarán en un archivo.

El programa intentará acceder a los subdominios usando los protocolos **`http`** y **`https`** y mostrará aquellos que respondan con un código de estado menor a 400. Los resultados también se guardarán en el archivo de salida si se especifica uno.

## **Notas**

- Si no se encuentra el archivo **`Subdominios.txt`**, el programa mostrará un mensaje indicando que el archivo no existe.
- El escaneo utiliza **múltiples hilos** para aumentar la velocidad de búsqueda.
- Si el programa es interrumpido por el usuario (Ctrl + C), se detendrá de manera segura.
