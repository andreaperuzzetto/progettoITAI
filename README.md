# progettoITAI

AI Business Automation SaaS verticale per IT Service Providers.

## Vision

progettoITAI è un Operational Intelligence Layer che trasforma informazioni destrutturate in decisioni operative strutturate attraverso AI e logiche di business.

## Tech Stack

Frontend:
- Next.js 14
- TailwindCSS

Backend:
- FastAPI
- SQLAlchemy 2.x

Database:
- PostgreSQL (Supabase - planned)

AI Layer:
- OpenAI (planned)
- Pinecone (planned)

## Project Structure

apps/
  frontend/
  backend/

docs/
  engineering-log/
  architecture/
  adr/

## Local Setup

Frontend:
pnpm dev:frontend

Backend:
cd apps/backend
source venv/bin/activate
uvicorn app.main:app --reload