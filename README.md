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

## Frontend
- Next.js 14
- React
- TailwindCSS
- shadcn/ui

## Backend
- FastAPI
- SQLAlchemy 2.x
- Pydantic / pydantic-settings
- Uvicorn

## Database
- PostgreSQL
- Supabase (managed PostgreSQL)

## AI Layer
- OpenAI API

## Vector Database
- Pinecone

## Infrastructure
- Docker
- Docker Compose
- Vercel (frontend deployment)
- Render (backend deployment)

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