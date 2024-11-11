import os
import shutil

# Calcular base_path
base_path = os.path.join(os.path.expanduser("~"), "Documents", "none", "multimedia/2023-10")

# Configuración del criterio de ordenamiento (puede ser 'day' o 'month')
criteria = 'day'  # Cambia a 'day' si deseas organizar por días

# Variables para estadísticas
total_files_found = 0
total_files_moved = 0
directories_created = {}  # Para almacenar los directorios creados y contar los archivos dentro de cada uno
invalid_files = []  # Lista para almacenar archivos no válidos

# Lista de extensiones permitidas (puede ser modificada)
ALLOWED_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.mp4', '.mov', '.avi', '.dng', '.raw')

# Función para extraer la fecha de creación del archivo desde el nombre
def get_creation_date_from_filename(filename):
    try:
        # Verificamos si el nombre del archivo contiene al menos un guion bajo
        parts = filename.split('_')
        if len(parts) >= 2 and len(parts[1]) >= 8:  # La segunda parte debe contener al menos 8 caracteres
            # Tomamos solo los primeros 8 caracteres de la segunda parte para la fecha (YYYYMMDD)
            date_str = parts[1][:8]
            # Convertimos la fecha en el formato YYYY-MM-DD
            formatted_date = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:]}"
            return formatted_date
        else:
            return None
    except Exception as e:
        print(f"Error processing filename {filename}: {e}")
        return None

# Función para mover los archivos a la carpeta correspondiente
def move_files_by_creation_date(criteria='day'):
    global total_files_found, total_files_moved

    # Recorremos los archivos en el directorio base
    for root, dirs, files in os.walk(base_path):
        for file in files:
            # Verificamos si el archivo tiene una extensión permitida
            if file.lower().endswith(ALLOWED_EXTENSIONS):
                filepath = os.path.join(root, file)
                total_files_found += 1  # Contamos el archivo encontrado

                # Obtener la fecha de creación desde el nombre del archivo
                creation_date = get_creation_date_from_filename(file)

                # Si la fecha no es válida, añadimos el archivo a la lista de archivos no válidos
                if not creation_date:
                    invalid_files.append(filepath)
                    continue

                # Crear el nombre de la carpeta en función del criterio
                if criteria == 'day':
                    target_dir = os.path.join(base_path, creation_date)  # Carpeta por día
                elif criteria == 'month':
                    target_dir = os.path.join(base_path, creation_date[:7])  # Carpeta por mes (YYYY-MM)
                else:
                    print("Criterio no válido. Use 'day' o 'month'.")
                    return

                # Crear la carpeta si no existe
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
                    directories_created[target_dir] = 0  # Inicializamos el contador de archivos en la carpeta creada

                # Definir la nueva ruta del archivo
                target_file = os.path.join(target_dir, file)

                # Mover el archivo si no está ya en la carpeta correspondiente
                if filepath != target_file:
                    try:
                        shutil.move(filepath, target_file)
                        total_files_moved += 1  # Contamos el archivo movido
                        directories_created[target_dir] += 1  # Incrementamos el contador de archivos en la carpeta
                        #print(f"Moved {file} to {target_file}")
                    except Exception as e:
                        print(f"Error moving {file}: {e}")

# Función para mostrar la estadística del árbol de directorios
def show_directory_statistics():
    print("\nDirectory structure and file counts:")
    for directory, count in directories_created.items():
        print(f"{directory}: {count} files")

# Función para guardar los archivos no válidos en un archivo de texto
def save_invalid_files():
    if invalid_files:
        with open('invalid_files.txt', 'w') as f:
            for filepath in invalid_files:
                f.write(f"{filepath}\n")
        print(f"\n{len(invalid_files)} invalid files were found and saved to 'invalid_files.txt'.")
    else:
        print("\nNo invalid files found.")



# Llamar a la función para mover los archivos con el criterio elegido
move_files_by_creation_date(criteria)

# Mostrar estadísticas
show_directory_statistics()

# Mostrar resumen de archivos encontrados y movidos
print("\nSummary:")
print(f"Total files found: {total_files_found}")
print(f"Total files moved: {total_files_moved}")

# Guardar los archivos no válidos
save_invalid_files()