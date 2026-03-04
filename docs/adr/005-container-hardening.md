# ADR-004 — Container Hardening Strategy

## Context

I container Docker, se eseguiti con configurazioni di default, possono introdurre alcuni rischi operativi:

- esecuzione come utente root
- consumo illimitato di risorse
- immagini di grandi dimensioni
- inclusione di file non necessari nel build context

Per migliorare sicurezza e stabilità è necessario applicare alcune pratiche di hardening.

## Decision

Vengono introdotte le seguenti misure:

1. Esecuzione dei container con utente non-root
2. Utilizzo di immagini base minimali (`python:slim`, `node:alpine`)
3. Introduzione di `.dockerignore`
4. Implementazione di healthcheck sui servizi
5. Definizione di limiti di CPU e memoria in `docker-compose`

## Consequences

Benefici:

- miglior isolamento dei processi
- maggiore sicurezza del runtime
- riduzione del consumo di risorse
- build più veloci

Trade-off:

- configurazione leggermente più articolata
- necessità di gestire ownership dei file nei container

Queste misure rendono l'ambiente più vicino a uno scenario di produzione reale.