# progettoITAI

AI Business Automation SaaS verticale per IT Service Providers.

progettoITAI è un sistema di **Operational Intelligence** progettato per trasformare informazioni destrutturate — email tecniche, richieste di preventivo, documentazione progettuale — in decisioni operative strutturate attraverso modelli linguistici, logiche di business e sistemi di scoring.

Il sistema combina **AI generativa, retrieval semantico e automazione decisionale** per supportare i processi commerciali e operativi nelle aziende IT.

---

# Stack

![Next.js](https://img.shields.io/badge/Next.js-14-black)
![React](https://img.shields.io/badge/React-18-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-LLM-orange)
![Pinecone](https://img.shields.io/badge/Pinecone-VectorDB-purple)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)
![Vercel](https://img.shields.io/badge/Vercel-Frontend%20Deploy-black)
![Render](https://img.shields.io/badge/Render-Backend%20Deploy-blue)

---

# Vision

Le aziende IT lavorano quotidianamente con grandi quantità di informazioni destrutturate:

- email tecniche
- richieste di preventivo
- documentazione progettuale
- specifiche tecniche
- comunicazioni cliente

Il valore è presente, ma spesso nascosto nel linguaggio naturale.

progettoITAI introduce uno **strato di Operational Intelligence** che:

1. analizza queste informazioni  
2. le trasforma in dati strutturati  
3. supporta le decisioni operative  

Il sistema non sostituisce l’operatore umano ma lo **aumenta**: l’AI propone classificazioni, stime e analisi, mentre la decisione finale rimane all’utente.

---

# Architecture Overview

L’architettura segue una struttura a layer progettata per separare responsabilità e facilitare l’evoluzione del sistema.

```
                ┌─────────────────────┐
                │      Frontend       │
                │     Next.js App     │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │      Backend        │
                │      FastAPI        │
                └──────────┬──────────┘
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼

 ┌──────────────┐   ┌───────────────┐   ┌───────────────┐
 │ PostgreSQL   │   │   OpenAI API  │   │   Pinecone    │
 │  Data Layer  │   │   AI Layer    │   │ Vector Memory │
 └──────────────┘   └───────────────┘   └───────────────┘
```

Il sistema integra tre livelli di conoscenza:

- **memoria strutturata** (database relazionale)
- **intelligenza generativa** (LLM)
- **memoria semantica** (vector database)

Questa combinazione permette la costruzione di pipeline RAG e sistemi decisionali AI assistiti.

---

# Repository Structure

Il progetto è organizzato come **monorepo**.

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

pnpm-workspace.yaml
package.json
.env.example
```

La struttura monorepo permette di mantenere frontend, backend e documentazione nello stesso contesto di sviluppo.

---

# Live Deployment

Frontend  
(Vercel)

Backend API  
(Render)

Il deployment separato consente:

- scalabilità indipendente dei servizi
- deploy semplificato
- isolamento delle responsabilità

---

# Development Roadmap

Il progetto segue una roadmap di sviluppo di **16 settimane**, organizzata in tre fasi principali.

### Phase 1 — MVP

- email ingestion
- AI classification engine
- document RAG pipeline
- proposal generator
- KPI dashboard

### Phase 2 — Automation Layer

- automation rules engine
- internal routing system
- deal scoring engine
- AI risk analysis

### Phase 3 — Enterprise Layer

- multi-tenant architecture
- role-based access control
- audit log & decision trace
- public API & CRM integration

---

# Local Setup

### Prerequisites

- Node.js 20+
- pnpm
- Python 3.11+
- Docker (optional)

---

## Frontend

```bash
pnpm dev:frontend
```

Frontend available at

```
http://localhost:3000
```

---

## Backend

```bash
cd apps/backend
source venv/bin/activate
uvicorn app.main:app --reload
```

Backend available at

```
http://localhost:8000
```

---

# Docker Setup

Run the entire system:

```bash
docker compose up --build
```

Services

Frontend  
```
http://localhost:3000
```

Backend  
```
http://localhost:8000
```

Health check

```
/health
```

---

# Documentation

Technical documentation is available in:

```
docs/
```

Includes:

- architecture documentation
- engineering development log
- ADR (architecture decision records)

---

# Current Status

The system is **infrastructurally complete but functionally minimal**.

Current capabilities:

- monorepo architecture
- Next.js frontend
- FastAPI backend
- PostgreSQL connection
- OpenAI integration ready
- Pinecone vector layer ready
- Docker containerization
- cloud deployment

Next development stages will introduce domain models, AI pipelines and business logic.

---

# Project Identity

progettoITAI can be described as an:

**Operational Intelligence Layer for IT Service Providers**

A system that receives unstructured information, structures it, evaluates it and turns it into actionable insights using a combination of **AI, decision logic and semantic memory**.