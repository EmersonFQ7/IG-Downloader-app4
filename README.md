# 🐳 Instagram Video Downloader - Docker Practice

Este proyecto es una aplicación web desarrollada con **Flask** y **yt-dlp** que permite descargar Reels y videos de Instagram. El objetivo es demostrar el uso de imágenes optimizadas y la persistencia de datos mediante volúmenes en Docker.

## 🚀 Guía de Inicio Rápido

Sigue estos pasos para clonar y ejecutar el proyecto en tu máquina local:

### 1. Clonar el repositorio
Abre una terminal y ejecuta:
```bash
git clone [https://github.com/EmersonFQ7/IG-Downloader-app4.git](https://github.com/EmersonFQ7/IG-Downloader-app4.git)
cd IG-Downloader-app4
2. Preparar el entorno de descargas
Crea la carpeta local donde se sincronizarán los videos descargados desde el contenedor:

PowerShell
mkdir descargas_ig
3. Construir la imagen (Build)
Puedes elegir entre tres niveles de optimización. Se recomienda la Opción C por ser la más ligera:

Opción A (Básica): docker build -t ig-v1 -f Dockerfile .

Opción B (Optimizada): docker build -t ig-v2 -f Dockerfile.optimizado .

Opción C (Profesional): docker build -t ig-v3 -f Dockerfile.multistage .

4. Ejecutar el contenedor (Run)
Lanza la aplicación vinculando el puerto 5000 y la carpeta de persistencia:

Nota: Si usas CMD, cambia ${PWD} por %cd%. En PowerShell funciona tal cual:

PowerShell
docker run -d -p 5000:5000 --name app-instagram -v ${PWD}/descargas_ig:/app/downloads ig-v3
5. Acceso a la aplicación
Abre tu navegador en: http://localhost:5000

Pega el enlace del video de Instagram.

Haz clic en Descargar.

El video se guardará automáticamente en tu carpeta local descargas_ig.