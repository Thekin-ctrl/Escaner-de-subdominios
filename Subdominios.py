import requests  # Para hacer solicitudes HTTP a los subdominios
from os import path  # Para verificar si el archivo de subdominios existe
import argparse  # Para manejar argumentos desde la línea de comandos
import sys  # Para manejar salidas del programa
from concurrent.futures import ThreadPoolExecutor  # Para usar múltiples hilos y acelerar el escaneo

# Configurar los argumentos que el usuario puede ingresar en la línea de comandos
parse = argparse.ArgumentParser(description="Escáner de subdominios en Python")
parse.add_argument("-t", "--target", help="Indicar el dominio objetivo", required=True)  # Argumento obligatorio
parse.add_argument("-o", "--output", help="Indicar el archivo para guardar los resultados", default=None)  # Archivo de salida opcional
parser = parse.parse_args()  # Obtener los argumentos proporcionados

# Definir encabezados con User-Agent para evitar bloqueos
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

# Función para verificar si un subdominio existe
def check_subdominio(subdominio, target, output_file):
    for protocolo in ["http", "https"]:  # Intentar con HTTP y HTTPS
        url = f"{protocolo}://{subdominio}.{target}"
        try:
            response = requests.get(url, headers=HEADERS, timeout=2)  # Hacer la petición con un tiempo límite de 2 segundos
            if response.status_code < 400:  # Si el código de respuesta es menor a 400, el subdominio existe
                result = f"(+) Subdominio encontrado: {url}"
                print(result)
                if output_file:  # Si se proporciona un archivo, guardar el resultado
                    with open(output_file, "a") as f:
                        f.write(result + "\n")
        except requests.ConnectionError:
            pass  # Si hay un error de conexión, el subdominio no existe o está caído

# Función principal
def main():
    output_file = parser.output  # Obtener el archivo de salida desde los argumentos

    if path.exists("Subdominios.txt"):  # Verificar si el archivo con subdominios existe
        with open("Subdominios.txt", "r") as file:  # Abrir el archivo en modo lectura
            wordlist = file.read().splitlines()  # Leer el archivo y dividirlo en líneas

        # Usar hilos para acelerar el escaneo de subdominios
        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(lambda sub: check_subdominio(sub, parser.target, output_file), wordlist)
    else:
        print("(-) El archivo 'Subdominios.txt' no existe.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\nPrograma interrumpido por el usuario")  # Salir si el usuario presiona Ctrl + C
