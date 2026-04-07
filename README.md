Instagram Video Downloader - Docker Practice
Este proyecto permite descargar Reels y videos de Instagram a través de una interfaz web, utilizando contenedores Docker optimizados.

🚀 Guía de Ejecución Paso a Paso
Sigue estas instrucciones en tu terminal (PowerShell o CMD):

1. Clonar el repositorio y entrar a la carpeta
PowerShell
git clone <URL_DE_TU_REPOSITORIO>
cd SEM4-EVA1
2. Preparar el entorno local
Crea la carpeta donde se sincronizarán los videos descargados desde el contenedor a tu PC:

PowerShell
mkdir descargas_ig
3. Construir la imagen (Build)
Elige una de las tres versiones disponibles para construir:

Versión Básica (Debian):
docker build -t ig-v1 -f Dockerfile .

Versión Optimizada (Alpine):
docker build -t ig-v2 -f Dockerfile.optimizado .

Versión Profesional (Multi-stage):
docker build -t ig-v3 -f Dockerfile.multistage .

4. Ejecutar el contenedor (Run)
Ejecuta la versión seleccionada (ejemplo con la v3).

Nota: Si usas CMD, cambia ${PWD} por %cd%. Si usas PowerShell, déjalo como está.

PowerShell
docker run -d -p 5000:5000 --name app-instagram -v ${PWD}/descargas_ig:/app/downloads ig-v3
5. Uso de la Aplicación
Abrir la interfaz: Ve a tu navegador y entra a http://localhost:5000.

Pegar Link: Copia la URL de un Reel o video de Instagram y pégala en el cuadro de texto.

Descargar: Haz clic en el botón "Descargar".

Ver resultados: * El video aparecerá en la lista de la página web para bajarlo al navegador.

También aparecerá automáticamente en tu carpeta local descargas_ig
