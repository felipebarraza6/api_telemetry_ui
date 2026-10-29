# api_telemetry_ui

## Descripción
UI y landing de telemetría (legado).

## Arquitectura
Carpetas principales: `api/`, `conf/`, `ikolu_app/`, `landing/`, `media/`.
Contenedores definidos en Dockerfile/compose del repo.

## Setup local
1. Clonar el repo y copiar `.env.example` a `.env` (no versionar `.env`).
2. Completar las variables con valores de desarrollo (pedirlos a Felipe; nunca por chat ni en commits).
3. Instalar dependencias (`pip install -r requirements.txt` / `npm ci`) y levantar el servicio.

## Variables de entorno
Solo nombres; valores en el servidor o en GitHub Secrets:
- (sin variables detectadas)

## Deploy
- Deploy **manual**; nada va a `production` sin aprobación de Felipe.
- No usar `down`, `--volumes` ni `prune` en servidores de producción.

## Runbook
- Revisar logs del contenedor/servicio antes de reiniciar; avisar antes de reiniciar servicios productivos.
- Ante un secreto filtrado: rotar, actualizar el servidor y ver `SECURITY.md`.
- Ante errores de CI: un solo re-run por PR.

---

## Documentación previa

CRM SMARTHYDRO

Desarrollado con: DRF, docker, nginx