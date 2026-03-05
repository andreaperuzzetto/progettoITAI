# System Architecture

Questo documento descrive l'architettura tecnica del sistema progettoITAI.

L'architettura è progettata per separare chiaramente le responsabilità tra interfaccia utente, logica applicativa, persistenza dei dati e capacità AI, permettendo evoluzione modulare e scalabilità del sistema.

---

# Technology Stack

Il sistema progettoITAI utilizza il seguente stack tecnologico.

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

# Architectural Layers

Il sistema è organizzato in cinque layer principali.

```
             ┌──────────────┐
             │   Frontend   │
             │   Next.js    │
             └──────┬───────┘
                    │
                    ▼
             ┌──────────────┐
             │    Backend   │
             │    FastAPI   │
             └──────┬───────┘
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼

   PostgreSQL      OpenAI     Pinecone
   Data Layer      AI Layer   Vector DB
```