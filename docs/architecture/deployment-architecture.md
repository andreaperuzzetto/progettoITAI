# Deployment Architecture

## Overview

Il sistema è distribuito su tre piattaforme principali:

- Vercel
- Render
- Supabase

Questa separazione permette di mantenere l'architettura semplice ma scalabile.

## System Diagram

Client  
↓  
Vercel (Next.js Frontend)

↓ HTTP API

Render (FastAPI Backend)

↓ SQL

Supabase (PostgreSQL)

↓ External Services

OpenAI  
Pinecone

## Frontend

Il frontend è una applicazione Next.js 14 deployata su Vercel.

Caratteristiche:

- build automatica da GitHub
- CDN globale
- gestione automatica HTTPS
- deploy preview per ogni commit

Il frontend comunica esclusivamente con il backend tramite API HTTP.

## Backend

Il backend è una applicazione FastAPI containerizzata tramite Docker.

Il servizio è deployato su Render come Docker Web Service.

Il container:

- espone la porta tramite variabile PORT
- avvia uvicorn
- utilizza utente non-root
- carica configurazione tramite environment variables

Il backend gestisce:

- routing API
- accesso al database
- integrazione OpenAI
- integrazione Pinecone

## Database

Il database è fornito da Supabase.

Viene utilizzato PostgreSQL con connection pooling.

La connessione avviene tramite transaction pooler per garantire compatibilità con ambienti cloud e containerizzati.

## Configuration

La configurazione applicativa è centralizzata tramite pydantic-settings.

Le variabili ambiente includono:

- DATABASE_URL
- OPENAI_API_KEY
- PINECONE_API_KEY
- PINECONE_ENVIRONMENT
- PINECONE_INDEX_NAME

Questo approccio evita configurazioni hardcoded e permette deploy multi-environment.

## Health Monitoring

Il backend espone endpoint di monitoraggio:

/health

Questo endpoint verifica:

- stato applicazione
- connessione database
- ambiente di esecuzione

Questo consente monitoraggio semplice e integrazione futura con sistemi di observability.