# ADR-003 — Next.js Standalone Runtime for Docker Deployment

## Context

Next.js può essere eseguito in diversi modi:

- modalità development (`next dev`)
- modalità server (`next start`)
- modalità standalone (`output: standalone`)

Nel contesto di container Docker è preferibile ridurre la dimensione dell'immagine e minimizzare le dipendenze runtime.

## Decision

Il frontend utilizza la modalità **Next.js standalone build**.

Il processo di build genera:

.next/standalone

che contiene un runtime Node minimale e un server.js autonomo.

Il container di produzione esegue direttamente:

node apps/frontend/server.js

## Consequences

Benefici:

- immagini Docker significativamente più piccole
- runtime isolato
- eliminazione di dipendenze di sviluppo
- build multi-stage più efficiente

Trade-off:

- struttura del filesystem leggermente più complessa
- necessità di copiare manualmente gli asset statici nel container runtime

Questa modalità è allineata alle best practice di deploy per applicazioni Next.js containerizzate.