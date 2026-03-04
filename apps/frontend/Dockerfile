# ---- Base ----
FROM node:20-alpine AS base

RUN apk add --no-cache curl

WORKDIR /app
RUN npm install -g pnpm

# ---- Dependencies ----
FROM base AS deps
WORKDIR /app

COPY pnpm-workspace.yaml .
COPY pnpm-lock.yaml .
COPY package.json .

COPY apps/frontend/package.json apps/frontend/package.json

RUN pnpm install --frozen-lockfile

# ---- Build ----
FROM base AS builder
WORKDIR /app

COPY --from=deps /app/node_modules ./node_modules
COPY . .

RUN pnpm --filter frontend build

# ---- Production ----
FROM node:20-alpine AS runner
WORKDIR /app

ENV NODE_ENV=production

# crea utente non-root
RUN adduser -D appuser

# Copia standalone completo
COPY --from=builder /app/apps/frontend/.next/standalone ./

# Copia static
COPY --from=builder /app/apps/frontend/.next/static ./apps/frontend/.next/static
COPY --from=builder /app/apps/frontend/public ./apps/frontend/public

# cambia ownership dei file
RUN chown -R appuser:appuser /app

# usa utente non-root
USER appuser

EXPOSE 3000

CMD ["node", "apps/frontend/server.js"]