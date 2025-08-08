import os
import ctypes
import subprocess
import sys

def es_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def extraer_variables_entorno():
    variables = os.environ
    archivo_salida = "credenciales.txt"
    
    with open(archivo_salida, "w", encoding="utf-8") as f:
        f.write("VARIABLES DE ENTORNO DETECTADAS:\n\n")
        for clave, valor in variables.items():
            f.write(f"{clave} = {valor}\n")
    
    print(f"[✔] Se ha creado el archivo: {archivo_salida}")

def main():
    if not es_admin():
        print("[!] Requiere permisos de administrador. Reintentando...")
        # Reejecuta el script con privilegios de administrador
        script = os.path.abspath(sys.argv[0])
        params = " ".join([f'"{arg}"' for arg in sys.argv[1:]])
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, f'"{script}" {params}', None, 1
        )
        sys.exit()

    print("[+] Ejecutando como administrador.")
    extraer_variables_entorno()
    input("\nPresiona Enter para cerrar la ventana...")

if __name__ == "__main__":
    main()
