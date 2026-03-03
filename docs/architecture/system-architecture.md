# System Architecture — progettoITAI

## Visione generale

progettoITAI è concepito come un Operational Intelligence Layer per IT Service Providers.  
L’architettura separa chiaramente frontend, backend, data layer e integrazioni AI.

---

## Layer applicativi

Frontend  
Next.js 14 con App Router, responsabile della presentazione e interazione utente.

Backend  
FastAPI, responsabile della logica applicativa, orchestrazione AI e gestione dati.

Data Layer  
PostgreSQL (Supabase) per dati strutturati.  
Pinecone per storage vettoriale e retrieval semantico.

AI Layer  
OpenAI per classificazione, generazione e embedding.

---

## Struttura backend

Il backend è organizzato nei seguenti moduli:

- api → routing e definizione endpoint  
- core → configurazione e logging  
- db → engine, sessioni e modelli  
- services → logica applicativa e AI orchestration  

Questa separazione consente estendibilità e testabilità.

---

## Data Flow (versione attuale)

Client → Frontend → Backend → Database  

L’integrazione con AI e vector database sarà introdotta nelle fasi successive.

---

## Deployment Model (target)

Frontend: Vercel  
Backend: Railway / Render / Fly.io  
Database: Supabase  

L’architettura è progettata per supportare una futura configurazione multi-tenant.
