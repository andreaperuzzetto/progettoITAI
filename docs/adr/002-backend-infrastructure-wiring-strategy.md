# ADR-002 — Backend Infrastructure Wiring Strategy

## Context

Durante la Settimana 1 è stata attivata l’infrastruttura tecnica del backend, includendo:

- PostgreSQL come database relazionale
- OpenAI come AI provider
- Pinecone come vector database

Era necessario integrare questi servizi mantenendo modularità e separazione delle responsabilità, evitando accoppiamento diretto tra layer applicativi e dipendenze esterne.

---

## Decision

1. Il database PostgreSQL viene utilizzato in locale per lo sviluppo, mantenendo compatibilità futura con Supabase.

2. L’integrazione con OpenAI è isolata nel layer `services`, evitando chiamate dirette nei router.

3. Il client Pinecone è inizializzato separatamente, mantenendo indipendenza dal database relazionale.

4. Tutte le configurazioni dei servizi esterni sono centralizzate tramite `pydantic-settings`.

---

## Alternatives Considered

- Connessione diretta a Supabase fin dall’inizio  
- Integrazione OpenAI direttamente nei router  
- Utilizzo di un unico modulo “external” per tutti i servizi  

L’utilizzo immediato di Supabase avrebbe introdotto dipendenza esterna prematura.  
L’integrazione AI nei router avrebbe aumentato accoppiamento e ridotto testabilità.  
Un modulo unico per tutti i servizi avrebbe ridotto chiarezza nella separazione dei layer.

---

## Consequences

Vantaggi:

- Separazione netta tra API layer e service layer  
- Possibilità di sostituire provider AI senza modificare i router  
- Compatibilità futura con ambienti cloud  
- Riduzione del rischio di refactoring strutturale  

Svantaggi:

- Maggiore numero di moduli fin dalle prime fasi  
- Necessità di mantenere coerenza tra configurazione e servizi  

La decisione stabilizza l’architettura per le fasi successive (Database Design, RAG Engine, Automation Layer).