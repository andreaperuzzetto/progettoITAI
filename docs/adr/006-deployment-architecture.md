# ADR-005 — Deployment Architecture (Vercel + Render + Supabase)

## Context

Con la conclusione della prima settimana di lavoro è stato necessario definire una strategia di deployment reale per il sistema.

L'obiettivo non era solamente rendere l'applicazione eseguibile localmente, ma distribuire l'intera architettura su servizi cloud gestiti, riducendo al minimo la complessità operativa.

Il progetto è strutturato come monorepo con due componenti principali:

- frontend (Next.js)
- backend (FastAPI)

Il sistema richiede inoltre:

- database PostgreSQL
- servizi esterni per AI e vector storage

Era quindi necessario definire una piattaforma di deploy per ciascun componente.

## Decision

L'architettura di deploy adottata è la seguente:

Frontend  
→ Vercel

Backend  
→ Render (Docker Web Service)

Database  
→ Supabase (PostgreSQL)

Vector Database  
→ Pinecone

AI Provider  
→ OpenAI

## Rationale

Le motivazioni principali della scelta sono:

### Vercel

Perfetta integrazione con Next.js e deploy automatico da GitHub.

Permette:

- build automatiche
- preview deployment
- CDN globale

### Render

Supporta deploy Docker nativi per backend Python.

Offre:

- deploy automatico da repository Git
- gestione environment variables
- HTTPS automatico
- health checks

### Supabase

Fornisce PostgreSQL gestito con:

- connection pooling
- backup automatici
- dashboard SQL
- compatibilità totale con SQLAlchemy

### Pinecone

Servizio dedicato alla gestione di vector database per future pipeline RAG.

## Consequences

L'architettura risultante è la seguente:

Client  
→ Frontend (Vercel)

Frontend  
→ Backend API (Render)

Backend  
→ PostgreSQL (Supabase)

Backend  
→ OpenAI API

Backend  
→ Pinecone

Questo approccio permette:

- separazione chiara tra frontend e backend
- scalabilità indipendente dei servizi
- riduzione del carico infrastrutturale
- semplicità di deploy continuo tramite GitHub.

Questa decisione stabilizza l'infrastruttura del progetto per le fasi successive di sviluppo.