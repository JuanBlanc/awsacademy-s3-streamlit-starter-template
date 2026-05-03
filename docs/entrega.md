# Entrega (GitHub) · RA2 SBD

## Qué entregar
1. Enlace a tu **repositorio fork** en GitHub.
2. Un **tag** llamado `v1.0-entrega` apuntando al commit final.
3. `docs/evidencias.md` completado.
4. La URL final del dashboard (en evidencias): `http://IP_PUBLICA_EC2:8501`

## Cómo crear el tag
Desde tu repositorio (en local):

```bash
git tag v1.0-entrega
git push origin v1.0-entrega
```

## Qué se corrige
Se corregirá **la versión marcada** por el tag `v1.0-entrega`.

## Normas
- No se aceptan entregas con secretos en el repositorio.
- Si detectas que subiste algo sensible:
  - elimina el archivo,
  - rota/renueva credenciales en AWS,
  - reescribe historial (si sabes hacerlo) o crea repo nuevo y avisa al profesor.
