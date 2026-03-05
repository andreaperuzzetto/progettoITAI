# progettoITAI

AI Business Automation SaaS verticale per IT Service Providers.

progettoITAI è un sistema di **Operational Intelligence** progettato per trasformare informazioni destrutturate — email tecniche, richieste di preventivo, documentazione progettuale — in decisioni operative strutturate attraverso modelli linguistici, logiche di business e sistemi di scoring.

Il sistema combina **AI generativa, retrieval semantico e automazione decisionale** per supportare i processi commerciali e operativi nelle aziende IT.

---

# Vision

Le aziende IT lavorano quotidianamente con grandi quantità di informazioni destrutturate:

- email tecniche
- richieste di preventivo
- documentazione progettuale
- specifiche tecniche
- comunicazioni cliente

Il valore è presente ma spesso nascosto nel linguaggio naturale.

progettoITAI introduce uno **strato di Operational Intelligence** che analizza queste informazioni, le struttura e supporta le decisioni operative.

---

# Tech Stack

### Frontend
![Next.js](https://img.shields.io/badge/Next.js-14-black)
![React](https://img.shields.io/badge/React-18-blue)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-Framework-38B2AC)
![shadcn/ui](https://img.shields.io/badge/shadcn-ui-black)

### Backend
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![Pydantic](https://img.shields.io/badge/Pydantic-Validation-E92063)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI_Server-499848)

### Database
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791)
![Supabase](https://img.shields.io/badge/Supabase-Managed_DB-3ECF8E)

### AI Layer
![OpenAI](https://img.shields.io/badge/OpenAI-LLM_API-412991)

### Vector Database
![Pinecone](https://img.shields.io/badge/Pinecone-Vector_DB-4B6FFF)

### Infrastructure
![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED)
![Vercel](https://img.shields.io/badge/Vercel-Frontend_Deploy-black)
![Render](https://img.shields.io/badge/Render-Backend_Deploy-46E3B7)

---

# Architecture Overview

Il sistema è organizzato in più livelli:

```
Frontend (Next.js)
        ↓
Backend API (FastAPI)
        ↓
PostgreSQL Database
        ↓
AI Layer (OpenAI)
        ↓
Vector Memory (Pinecone)
```

Questa architettura separa chiaramente:

- interfaccia utente
- logica applicativa
- persistenza dati
- capacità AI
- memoria semantica

---

# Repository Structure

```
progettoITAI

apps
  frontend
  backend

docs
  architecture
  engineering-log
  adr

docker
docker-compose.yml
```

---

# Development Status

Il progetto segue una roadmap di **16 settimane**.

Attualmente è completata:

**Week 1 — Infrastructure Foundations**

Deliverable principali:

- monorepo configurato
- frontend Next.js operativo
- backend FastAPI configurato
- connessione PostgreSQL funzionante
- integrazione OpenAI predisposta
- integrazione Pinecone predisposta
- container Docker funzionanti
- primo deploy cloud

---

# Local Setup

Prerequisiti

- Node.js 20+
- pnpm
- Python 3.11+

Frontend

```bash
pnpm dev:frontend
```

Backend

```bash
cd apps/backend
source venv/bin/activate
uvicorn app.main:app --reload
```

---

# Documentation

La documentazione tecnica completa è disponibile nella cartella:

```
docs/
```

- `architecture/` → design del sistema
- `engineering-log/` → cronologia sviluppo
- `adr/` → architectural decision records