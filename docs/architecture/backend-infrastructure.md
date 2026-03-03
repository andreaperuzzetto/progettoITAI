# Backend Infrastructure — W1
Data: 2026-03-03

## Obiettivo della fase

Consolidare l’infrastruttura tecnica del backend, collegando database relazionale, servizi AI e vector storage, senza introdurre ancora logica di dominio o modelli applicativi.

L’obiettivo non è sviluppare feature, ma stabilizzare i layer fondamentali su cui si baserà l’intero sistema.

---

## Contesto architetturale

Il backend rappresenta il nucleo dell’Operational Intelligence Layer.

In questa fase sono stati cablati i tre pilastri fondamentali:

- Persistence Layer (PostgreSQL)
- Intelligence Layer (OpenAI)
- Vector Layer (Pinecone)

L’integrazione è stata realizzata mantenendo separazione delle responsabilità e modularità.

---

## Struttura backend

Il backend mantiene la seguente organizzazione:

app/
├── main.py  
├── api/  
├── core/  
├── db/  
└── services/  

Separazione dei layer:

- api → esposizione HTTP
- core → configurazione e logging
- db → engine e session management
- services → integrazione AI e servizi esterni

Questa struttura previene accoppiamento eccessivo e facilita estendibilità futura.

---

## Configurazione centralizzata

È stato implementato un sistema di configurazione tramite `pydantic-settings`.

Caratteristiche:

- caricamento da `.env`
- validazione variabili obbligatorie
- nessuna chiave hardcoded
- caching tramite `lru_cache`
- predisposizione multi-environment

Variabili attualmente gestite:

- database_url
- openai_api_key
- pinecone_api_key
- pinecone_environment
- pinecone_index_name

La configurazione rappresenta il punto unico di controllo delle dipendenze esterne.

---

## Persistence Layer — PostgreSQL

È stata attivata una connessione reale a PostgreSQL.

Implementazione:

- create_engine configurato
- SessionLocal tramite sessionmaker
- dependency injection get_db
- pool_pre_ping=True per robustezza

Endpoint tecnico di verifica:

/debug/db-check

Funzione: esegue SELECT 1 per validare la connessione.

Non ancora implementati:

- modelli ORM
- schema relazionale
- migration system (Alembic)

Questi elementi saranno introdotti nella fase Database Design.

---

## Intelligence Layer — OpenAI

È stato creato un service layer dedicato:

services/openai_client.py

Caratteristiche:

- client inizializzato tramite configurazione
- isolamento della logica AI dai router
- endpoint tecnico di test

Endpoint:

/debug/openai-check

In questa fase non è stato introdotto:

- prompt engineering avanzato
- structured output enforcement
- decision logging

L’obiettivo è esclusivamente infrastrutturale.

---

## Vector Layer — Pinecone

È stato inizializzato il client Pinecone tramite configurazione centralizzata.

Funzionalità attuale:

- connessione all’index configurato
- endpoint tecnico di verifica

Non ancora implementato:

- pipeline embedding
- chunking documentale
- retrieval API
- RAG engine

La memoria semantica è predisposta ma non ancora attiva.

---

## Endpoint di verifica infrastrutturale

Sono presenti endpoint tecnici temporanei:

- /debug/db-check
- /debug/openai-check
- /debug/pinecone-check

Scopo: validazione integrazione servizi esterni.

Non rappresentano feature applicative definitive.

---

## Stato del sistema

Alla chiusura della fase infrastrutturale:

- Config centralizzata operativa
- PostgreSQL connesso
- SQLAlchemy session management attivo
- Service layer AI isolato
- Client Pinecone predisposto
- Architettura modulare stabile

Il sistema è infrastrutturalmente completo e pronto per:

- modellazione database
- introduzione ORM
- pipeline AI strutturate
- RAG engine
- logica di business

La base tecnica è stabile e riduce la necessità di refactoring strutturale nelle fasi successive.