# W1 — Infrastructure Foundations

Periodo: 3–5 Marzo 2026

# Context

La prima settimana di sviluppo è stata dedicata alla costruzione delle fondamenta infrastrutturali del progetto.

L'obiettivo principale era predisporre un ambiente tecnico stabile su cui sviluppare le funzionalità applicative previste dalla roadmap.

---

# Objectives

- definizione struttura repository
- configurazione frontend
- configurazione backend
- integrazione database PostgreSQL
- predisposizione servizi AI
- configurazione vector database
- containerizzazione applicazione
- primo deployment cloud

Questi obiettivi erano necessari per stabilire l'infrastruttura tecnica su cui costruire le funzionalità applicative nelle settimane successive.

---

# Repository Setup

Il progetto è stato organizzato come monorepo.

Struttura principale:

```
apps
 frontend
 backend

docs
 architecture
 engineering-log
 adr
```

La gestione dei package JavaScript utilizza **pnpm workspaces**.

---

# Backend Infrastructure

Il backend è stato sviluppato utilizzando FastAPI.

Struttura principale:

```
app
 api
 core
 db
 services
```

Questa suddivisione consente di isolare:

- endpoint HTTP
- configurazione applicazione
- accesso database
- logica applicativa

---

# Database Integration

Il sistema utilizza PostgreSQL.

Per semplificare la gestione infrastrutturale è stata utilizzata una istanza gestita tramite Supabase.

La connessione è stata verificata tramite endpoint di health check.

---

# AI Services Setup

Il backend è stato predisposto per l'integrazione con OpenAI.

Le funzionalità AI verranno implementate nelle settimane successive della roadmap.

---

# Vector Database Setup

È stato configurato Pinecone come vector database.

Questa componente verrà utilizzata per implementare pipeline Retrieval-Augmented Generation.

---

# Containerization

Frontend e backend sono stati containerizzati tramite Docker.

L'orchestrazione dei servizi è gestita tramite Docker Compose.

```
docker compose up
```

---

# Deployment

Il sistema è stato deployato con:

Frontend → Vercel  
Backend → Render

Questo consente test realistici in ambiente cloud.

---

# Outcome

Alla fine della settimana il sistema presenta:

- monorepo configurato
- frontend operativo
- backend configurato
- database connesso
- servizi AI predisposti
- vector database configurato
- container Docker funzionanti
- deployment cloud attivo