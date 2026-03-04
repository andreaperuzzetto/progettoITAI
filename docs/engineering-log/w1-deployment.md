# W1 

Docker, Frontend Deployment e Cloud Infrastructure

Data: 4 Marzo 2026

---

## Obiettivo della giornata

La terza giornata di lavoro è stata dedicata alla finalizzazione dell'infrastruttura del progetto.

Se il Giorno 1 ha definito la struttura architetturale e il Giorno 2 ha integrato i servizi esterni, il Giorno 3 ha avuto come obiettivo il deployment reale dell'intero sistema.

L'obiettivo era rendere l'applicazione accessibile pubblicamente tramite un'architettura cloud completa.

---

## Containerizzazione

Il backend è stato containerizzato tramite Docker.

Il Dockerfile include:

- immagine python:3.11-slim
- installazione dipendenze tramite requirements.txt
- esecuzione uvicorn
- utente non-root per sicurezza

È stato inoltre implementato il supporto alla porta dinamica tramite variabile PORT per compatibilità con Render.

---

## Deployment Frontend

Il frontend Next.js è stato deployato su Vercel.

Il deploy è collegato direttamente al repository GitHub e avviene automaticamente ad ogni push sul branch main.

Il frontend è ora accessibile pubblicamente tramite dominio Vercel.

---

## Deployment Backend

Il backend è stato deployato su Render come Docker Web Service.

Il servizio è configurato con:

- build automatica da repository GitHub
- variabili ambiente
- health check endpoint
- porta dinamica tramite variabile PORT

Durante il deployment sono stati risolti diversi problemi infrastrutturali:

- gestione corretta del contesto Docker
- path del Dockerfile
- configurazione delle variabili ambiente
- binding della porta per il container

---

## Connessione Database

Il database PostgreSQL è ospitato su Supabase.

Durante l'integrazione è stato necessario utilizzare il transaction pooler per garantire compatibilità con l'ambiente Render.

Questo ha risolto problemi di connettività IPv6 presenti nella connessione diretta.

La connessione è stata verificata tramite endpoint di debug.

---

## Stato del sistema

Alla conclusione della giornata il sistema è completamente operativo.

Frontend:

deployato su Vercel

Backend:

deployato su Render

Database:

PostgreSQL gestito tramite Supabase

Il backend espone endpoint di health check che confermano la connessione al database.

---

## Risultato

Con il completamento del Giorno 3 la prima settimana di lavoro può considerarsi conclusa.

Il sistema possiede ora:

- infrastruttura cloud funzionante
- deploy automatico da repository
- configurazione centralizzata
- integrazione database stabile

Questo rappresenta una base solida per le fasi successive di sviluppo.

Le settimane successive potranno concentrarsi sulla modellazione del dominio e sull'implementazione della logica applicativa.