# ParkOS Smart Parking

ParkOS is a responsive, installable PWA demo with a no-build vanilla JavaScript interface. The three workspaces share a browser-local state store: driver reservations, simulated entry/exit and settlement, and the admin lot/session console. The PWA caches its app shell and stores demo data in local storage.

## Run the PWA

From `frontend`, run `python -m http.server 8080` and open `http://localhost:8080`. This serves the single-file PWA without a build step or JavaScript package install. The install prompt requires HTTPS or localhost. Browser storage is local to the browser profile; use its site data controls to reset the demo. If you have Node.js and npm, `npm install` followed by `npm run start` also runs the Vite development server.

## Run the service stack

Copy `.env.example` to `.env`, set a private `HMAC_SECRET` and database password, then run `docker compose up --build`. The API health endpoint is `http://localhost:8000/health`; the PWA is at `http://localhost:5173`.

## Demo behavior and deployment limits

- Checkout methods, exit settlement, cameras, sensors and barrier operations are simulations. No real payment credentials are requested and no physical gate is controlled.
- Passes are HMAC-signed with a key stored in this browser profile so the demo can validate a QR scan locally. This is a demo-only trust boundary; a deployed system must sign and verify passes on the backend and use a managed secret.
- The FastAPI, PostgreSQL, Redis and edge folders provide architecture foundations and reusable domain helpers. Driver/admin/gate HTTP APIs, authentication, production persistence wiring, real payment-provider webhooks, ANPR, camera models and hardware drivers still need deployment-specific implementation before public or real-lot use.
- The shell works offline after its first visit. QR rendering uses a CDN when online and falls back to the booking ID when the QR library is unavailable.

## Project map

- `frontend/index.html` — complete single-file PWA experience.
- `frontend/manifest.webmanifest`, `frontend/sw.js`, `frontend/icons/` — install metadata, offline shell and app icon.
- `backend/` — FastAPI entrypoint, domain services, schemas and container.
- `database/` — PostgreSQL migrations and demo lot seed.
- `edge-vision/` — offline SQLite event queue and sensing/hardware adapter seams.
