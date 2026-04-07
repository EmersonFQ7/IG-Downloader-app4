# 🐳 Instagram Video Downloader - Docker Practice

Este proyecto permite descargar Reels y videos de Instagram mediante una interfaz web, utilizando contenedores Docker optimizados para minimizar el peso y garantizar la persistencia de los archivos.

---

## 🚀 Pasos para la Instalación y Uso

Sigue estos pasos en orden desde tu terminal (PowerShell o Bash):

### 1. Clonar el repositorio
Primero, obtén una copia local del proyecto:
```bash
git clone <URL_DE_TU_REPOSITORIO>
cd SEM4-EVA1
2. Preparar la carpeta de descargas
Crea el directorio donde se guardarán los videos físicamente en tu PC. Esto asegura que los archivos no se borren si detienes el contenedor:

En PowerShell:

PowerShell
mkdir descargas_ig
3. Construir la imagen (Build)
Elige una de las tres versiones disponibles según el nivel de optimización que desees probar (se recomienda la Opción C):

Opción A (Básica - Debian):

Bash
docker build -t ig-v1 -f Dockerfile .
Opción B (Optimizada - Alpine):

Bash
docker build -t ig-v2 -f Dockerfile.optimizado .
Opción C (Profesional - Multi-stage):

Bash
docker build -t ig-v3 -f Dockerfile.multistage .
4. Ejecutar el contenedor (Run)
Lanza la aplicación vinculando el puerto y la carpeta de descargas (ejemplo con la versión ig-v3):

Nota: Si usas CMD, cambia ${PWD} por %cd%. En PowerShell úsalo tal cual.

En PowerShell:

PowerShell
docker run -d -p 5000:5000 --name app-instagram -v ${PWD}/descargas_ig:/app/downloads ig-v3
🖥️ Cómo usar la aplicación
Abrir la Web: Una vez que el contenedor esté corriendo, abre tu navegador y entra a: http://localhost:5000

Pegar Link: Copia la URL de un video de Instagram y pégala en el cuadro de texto.

Descargar: Haz clic en el botón "Descargar".

Ver resultados: * El video aparecerá en la lista de la página web para descarga directa.

También lo encontrarás físicamente en la carpeta descargas_ig de tu PC.