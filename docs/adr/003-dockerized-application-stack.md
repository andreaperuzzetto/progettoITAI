# ADR-002 — Dockerized Application Stack

## Context

Il progetto richiede l’esecuzione coordinata di più servizi:

- frontend Next.js
- backend FastAPI
- database PostgreSQL
- future integrazioni con servizi AI (OpenAI, Pinecone)

Durante lo sviluppo iniziale questi servizi venivano eseguiti localmente in ambienti separati, creando potenziali divergenze tra ambiente di sviluppo e ambiente di deploy.

Per garantire coerenza tra ambienti e semplificare il deployment, è necessario definire una strategia di containerizzazione.

## Decision

L'intero stack applicativo viene containerizzato tramite Docker.

Vengono definiti:

- un Dockerfile per il backend FastAPI
- un Dockerfile multi-stage per il frontend Next.js
- un file `docker-compose.yml` per orchestrare i servizi

Ogni servizio viene eseguito in un container isolato con networking gestito da Docker Compose.

## Consequences

Vantaggi:

- ambienti di sviluppo e produzione allineati
- build riproducibili
- isolamento dei servizi
- deploy semplificato su cloud o infrastrutture container-based

Svantaggi:

- aumento della complessità iniziale
- build più lente rispetto a esecuzioni locali non containerizzate

Questa scelta abilita inoltre future integrazioni con orchestratori come Kubernetes o piattaforme di deploy container-based.