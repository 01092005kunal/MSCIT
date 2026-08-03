# ---------- Build Stage ----------
FROM node:18-alpine AS builder

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

# ---------- Production Stage ----------
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install --omit=dev

COPY --from=builder /app .

EXPOSE 8081

CMD ["node","server.js"]