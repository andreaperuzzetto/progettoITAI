# ADR-001 — Use pnpm Workspaces

## Context

Il progetto richiede la gestione di frontend (Next.js) e backend (FastAPI) all’interno dello stesso repository.  
È necessario mantenere coerenza strutturale senza introdurre complessità prematura.

---

## Decision

È stato adottato pnpm workspaces come sistema di gestione del monorepo.

---

## Alternatives Considered

- Turborepo  
- Nx  
- Repository separati  

Turborepo e Nx introducono maggiore complessità rispetto alle necessità iniziali del progetto.  
Repository separati avrebbero aumentato frammentazione e perdita di visibilità unificata.

---

## Consequences

Vantaggi:
- Struttura semplice e coerente  
- Gestione centralizzata degli script frontend  
- Possibilità futura di introdurre package condivisi  

Svantaggi:
- Il backend Python non è gestito direttamente dal workspace  
- Possibile necessità futura di tool più avanzati in caso di crescita significativa