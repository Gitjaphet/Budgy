<div align="center">

# 💰 Budgy

**SaaS multi-tenant de gestion de dépenses**, pensé pour les particuliers et les petites équipes qui veulent suivre leur budget sans friction.

[🌐 Démo en ligne](https://budgy.artjatie.com) · [Signaler un bug](https://github.com/Gitjaphet/Budgy/issues)

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

- 🌐 [Portfolio](https://japhet-dev-portfolio.vercel.app/)
- 💼 [LinkedIn](https://linkedin.com/in/japhet-bezanaka-dev)
- 🐙 [GitHub](https://github.com/Gitjaphet)

---

<div align="center">
<sub>Construit avec ☕ et Django à Madagascar 🇲🇬</sub>
</div>
