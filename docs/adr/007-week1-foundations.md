# ADR 007 — Week 1 Infrastructure Foundations

Status: Accepted  
Date: 2026-03-05

---

# Context

Il progetto richiede integrazione tra:

- frontend web
- backend API
- database relazionale
- modelli linguistici
- vector database

Era quindi necessario definire una architettura iniziale coerente e scalabile.

---

# Decision

Sono state adottate le seguenti tecnologie e scelte architetturali:

- monorepo per frontend e backend
- Next.js per il frontend
- FastAPI per il backend
- PostgreSQL come database principale
- Supabase per la gestione del database
- OpenAI per il layer AI
- Pinecone come vector database
- containerizzazione tramite Docker
- deploy separato frontend/backend

---

# Alternatives Considered

Sono state considerate alcune alternative architetturali.

**Backend framework alternativi**

- Django
- Flask

FastAPI è stato scelto per:

- performance elevate
- supporto asincrono
- integrazione semplice con librerie AI

**Vector database alternativi**

- Weaviate
- Chroma

Pinecone è stato scelto per la maturità del servizio e la semplicità di integrazione.

---

# Consequences

L'infrastruttura risultante consente:

- sviluppo modulare
- separazione delle responsabilità
- integrazione AI scalabile
- containerizzazione dell'ambiente
- deploy indipendente dei servizi

Questa architettura costituisce la base su cui verranno implementate le funzionalità applicative nelle settimane successive.