<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:F5A65B,100:E85D8A&height=160&section=header&text=Budgy&fontSize=40&fontColor=fff&animation=twinkling&fontAlignY=35&desc=SaaS%20multi-tenant%20de%20gestion%20des%20dépenses&descAlignY=58&descSize=16" width="100%"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Production-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Multi--tenant-django--tenants-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Madagascar-🇲🇬-red?style=for-the-badge" />
</p>

---

## 📖 À propos

**Budgy** est une application SaaS multi-tenant construite avec Django, où chaque organisation dispose de son propre schéma PostgreSQL isolé (via `django-tenants`), accessible via un sous-domaine dédié (`monentreprise.budgy.artjatie.com`).

Le projet met l'accent sur une **expérience utilisateur fluide et rapide** grâce à HTMX (navigation sans rechargement complet, formulaires et filtres en AJAX léger), sans la complexité d'un frontend JavaScript séparé (React/Vue).

---

## ✨ Fonctionnalités

- 🏢 **Multi-tenant réel** — isolation des données par schéma PostgreSQL (`django-tenants`), routage automatique par sous-domaine via Traefik v3
- 📊 **Dashboard Résumé** — KPIs du mois (total, variation vs mois dernier, catégorie principale), graphiques interactifs (répartition par catégorie, évolution sur 6 mois) avec Chart.js
- 💰 **Gestion des dépenses** — création/modification/suppression en modals, recherche en temps réel, filtres par catégorie et période
- ⚡ **Navigation HTMX** — `hx-boost` avec swap ciblé du contenu principal + extension `head-support` pour un chargement de page quasi instantané, sans rechargement complet
- 📱 **Responsive mobile-first** — sidebar rétractable sur desktop, barre de navigation basse dédiée sur mobile
- 🎨 **Design system glassmorphism** maison — typographie Josefin Sans, iconographie Phosphor Icons, variables CSS centralisées
- 🔐 **Authentification par tenant** — inscription et connexion isolées par organisation
- 🚀 **CI/CD automatisé** — GitHub Actions, migrations automatiques au déploiement, conteneurisation complète

---

## 🏗️ Stack technique

| Couche | Technologie |
|---|---|
| Backend | Django · django-tenants · Gunicorn |
| Frontend | HTMX · Chart.js · CSS custom (glassmorphism) |
| Base de données | PostgreSQL (isolation par schéma) |
| Infrastructure | Docker Compose · Traefik v3 · Whitenoise |
| CI/CD | GitHub Actions (build, migrations, déploiement) |

### Architecture

```
┌─────────────┐       ┌──────────────┐       ┌─────────────────┐
│   Traefik   │──────▶│  Django app  │──────▶│  PostgreSQL      │
│  (routage   │       │  (Gunicorn +  │       │  multi-schema    │
│  sous-domaine)│      │  Whitenoise) │       │  (django-tenants)│
└─────────────┘       └──────────────┘       └─────────────────┘
                              │
                              ▼
                     ┌──────────────────┐
                     │  Templates HTMX  │
                     │  + Chart.js      │
                     └──────────────────┘
```

---

## 📂 Structure du projet

```
backend/
├── budgy/          # Configuration Django (settings, urls, asgi/wsgi)
├── core/            # Dashboard, authentification, layout partagé
├── depenses/         # Module de gestion des dépenses (CRUD, filtres)
├── tenants/          # Gestion multi-tenant (inscription, login par organisation)
└── docker-compose.yml
```

---

## 🗺️ Roadmap

- [ ] Module **Budget** — définition d'objectifs de dépenses par catégorie
- [ ] Module **Récurrentes** — automatisation des dépenses périodiques
- [ ] Module **Planning** — vue calendrier des dépenses à venir
- [ ] Module **Équipe** — gestion collaborative multi-utilisateurs par tenant
- [ ] Export PDF/Excel des rapports mensuels

---

## 👤 Auteur

**DEV-JAPHET** — Développeur Full-Stack, Madagascar
Spécialisé Next.js · Django · FastAPI · DevOps · Odoo

- 🌐 [Portfolio](https://japhet.medevstack.com)
- 💼 [LinkedIn](https://linkedin.com/in/japhet-bezanaka-dev)
- 🐙 [GitHub](https://github.com/Gitjaphet)

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:F5A65B,100:E85D8A&height=100&section=footer" width="100%"/>
</p>
