<div align="center">

# 💰 Budgy

<svg width="1200" height="300" viewBox="0 0 1200 300" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F5A65B"/>
      <stop offset="100%" stop-color="#E85D8A"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="300" fill="url(#bg)"/>
  <path d="M0,255 C280,215 520,285 800,245 C960,222 1080,255 1200,235 L1200,300 L0,300 Z" fill="rgba(255,255,255,0.14)"/>
  <text x="60" y="145" font-family="Georgia, 'Times New Roman', serif" font-style="italic" font-size="58" font-weight="700" fill="#ffffff">Budgy</text>
  <text x="60" y="188" font-family="Arial, sans-serif" font-size="22" fill="rgba(255,255,255,0.9)">SaaS multi-tenant de gestion des dépenses</text>
</svg>

</div>

---

## 📖 À propos

**Budgy** est une application SaaS multi-tenant construite avec Django, où chaque organisation dispose de son propre schéma PostgreSQL isolé (via `django-tenants`), accessible via un sous-domaine dédié (`monentreprise.budgy.artjatie.com`).

Le projet met l'accent sur une **expérience utilisateur fluide et rapide** grâce à HTMX (navigation sans rechargement complet, formulaires et filtres en AJAX léger), sans la complexité d'un frontend JavaScript séparé (React/Vue).

## ✨ Fonctionnalités

- **Multi-tenant réel** — isolation des données par schéma PostgreSQL (`django-tenants`), routage automatique par sous-domaine via Traefik v3
- **Dashboard Résumé** — KPIs du mois (total, variation vs mois dernier, catégorie principale), graphiques interactifs (répartition par catégorie, évolution sur 6 mois) avec Chart.js
- **Gestion des dépenses** — création/modification/suppression en modals, recherche en temps réel, filtres par catégorie et période
- **Navigation HTMX** — `hx-boost` avec swap ciblé du contenu principal + extension `head-support` pour un chargement de page quasi instantané, sans rechargement complet
- **Responsive mobile-first** — sidebar rétractable sur desktop, barre de navigation basse dédiée sur mobile
- **Design system glassmorphism** maison — typographie Josefin Sans, iconographie Phosphor Icons, variables CSS centralisées
- **Authentification par tenant** — inscription et connexion isolées par organisation
- **CI/CD automatisé** — GitHub Actions, migrations automatiques au déploiement, conteneurisation complète


## 🏗️ Architecture technique

```
┌─────────────┐       ┌──────────────┐       ┌─────────────────┐
│   Traefik   │──────▶│  Django app  │──────▶│  PostgreSQL      │
│  (routage   │       │  (Gunicorn + │       │  multi-schema    │
│  sous-domaine)│      │  Whitenoise) │       │  (django-tenants)│
└─────────────┘       └──────────────┘       └─────────────────┘
                              │
                              ▼
                     ┌──────────────────┐
                     │  Templates HTMX  │
                     │  + Chart.js      │
                     └──────────────────┘
```

| Couche | Technologies |
|---|---|
| **Backend** | Django, django-tenants, Gunicorn |
| **Frontend** | HTMX, Chart.js, CSS custom (glassmorphism) |
| **Base de données** | PostgreSQL (isolation par schéma) |
| **Infrastructure** | Docker Compose, Traefik v3, Whitenoise |
| **CI/CD** | GitHub Actions (build, migrations, déploiement) |

## 📂 Structure du projet

```
backend/
├── budgy/          # Configuration Django (settings, urls, asgi/wsgi)
├── core/            # Dashboard, authentification, layout partagé
├── depenses/         # Module de gestion des dépenses (CRUD, filtres)
├── tenants/          # Gestion multi-tenant (inscription, login par organisation)
└── docker-compose.yml
```

## 🗺️ Roadmap

- [ ] Module **Budget** — définition d'objectifs de dépenses par catégorie
- [ ] Module **Récurrentes** — automatisation des dépenses périodiques
- [ ] Module **Planning** — vue calendrier des dépenses à venir
- [ ] Module **Équipe** — gestion collaborative multi-utilisateurs par tenant
- [ ] Export PDF/Excel des rapports mensuels

## 👤 Auteur

**DEV-JAPHET** — Développeur Full-Stack, Madagascar
Spécialisé Next.js · Django · FastAPI · DevOps . Odoo

- 🌐 [Portfolio](https://japhet.medevstack.com)
- 💼 [LinkedIn](https://linkedin.com/in/japhet-bezanaka-dev)
- 🐙 [GitHub](https://github.com/Gitjaphet)

---

<div align="center">
<sub>Construit avec ☕ et Django à Madagascar 🇲🇬</sub>
</div>
