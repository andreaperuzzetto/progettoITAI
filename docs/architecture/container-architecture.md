# Container Architecture

## Overview

L'applicazione è organizzata come un sistema multi-servizio containerizzato.

Ogni componente principale dell'architettura viene eseguito all'interno di un container dedicato orchestrato tramite Docker Compose.

## Services

### Frontend

Tecnologia:

Next.js

Responsabilità:

- rendering dell'interfaccia utente
- comunicazione con il backend API
- gestione delle pagine e delle interazioni client

Runtime:

Node.js standalone server generato da Next.js.

Porta esposta:

3000

---

### Backend

Tecnologia:

FastAPI

Responsabilità:

- gestione API
- integrazione con servizi AI
- accesso al database
- orchestrazione logica applicativa

Porta esposta:

8000

---

## Container Orchestration

L'orchestrazione dei servizi avviene tramite Docker Compose.

Il file `docker-compose.yml` definisce:

- build delle immagini
- networking tra servizi
- healthcheck
- limiti di risorse

I container comunicano tramite la rete interna di Docker.

## Runtime Architecture

Frontend → Backend → External Services

Frontend comunica con il backend tramite HTTP.

Il backend fungerà da punto centrale per:

- integrazione OpenAI
- gestione embeddings
- accesso a Pinecone
- pipeline RAG.

## Health Monitoring

Entrambi i servizi espongono healthcheck per permettere a Docker di monitorare lo stato dei container.

Backend:

/health

Frontend:

HTTP check sulla root application.

Questo consente di individuare rapidamente failure dei servizi durante runtime.