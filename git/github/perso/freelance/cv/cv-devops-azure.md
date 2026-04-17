# Daba TALL

Ingénieure DevOps Azure | 9 ans dans le DevOps et l'infrastructure cloud
daba.tall@outlook.com

---

## Profil

Ingénieure DevOps spécialisée Azure, j'interviens sur l'ensemble du cycle de vie de l'infrastructure cloud : architecture IaC Terraform, déploiement et exploitation de plateformes conteneurisées, sécurité réseau, CI/CD et monitoring. Parcours construit sur des environnements de production grands comptes (énergie, finance, banque, industrie).

---

## Compétences techniques

Infrastructure as Code : Terraform (modules réutilisables, Building Blocks pattern, multi-environnement, drift detection, state management, targeted apply), provider azapi

Azure Compute : Container Apps (workload profiles, autoscaling, sidecars OpenTelemetry), AKS (Kubernetes, Helm charts, scaling), App Service (staging slots, blue-green), Container Registry

Azure Networking : Front Door Premium (CDN, WAF Prevention, Private Link, custom domains, certificats managés), NSG, subnets, private endpoints, service endpoints

Azure Data : MySQL Flexible Server (HA SameZone, geo-replicas), PostgreSQL Flexible Server (AD auth, managed identity), Redis Premium, Azure AI Search

Azure Security : Key Vault (RBAC, access policies), managed identities (system et user-assigned), OIDC GitHub Actions, WAF, TLS 1.2, soft delete, network isolation

CI/CD : GitHub Actions (workflows multi-env, matrix builds, OIDC auth, conditional deployments, backup pre-deploy, sync prod-to-dev), Azure DevOps, GitLab CI

Conteneurisation : Docker (multi-stage, images custom PHP 8.4), Helm charts, OpenTelemetry Collector, Dynatrace OneAgent, Trivy (scan de vulnérabilités)

Monitoring : Application Insights, Log Analytics, OpenTelemetry (OTLP HTTP/gRPC), Dynatrace, alertes métier, KQL

Backup/DR : MySQL dump automatisé, snapshots NFS, Recovery Services Vault, Backup Vault, GZRS, workflows de restauration

Langages et outils : Bash, Python, PHP/Symfony, Azure CLI, GitHub CLI, Git, Linux

---

## Expérience

### Ingénieure DevOps Azure - TotalEnergies TGITS (août 2024 - aujourd'hui)

Conception et exploitation de l'infrastructure Azure pour une plateforme multi-tenant hébergeant 5 portails en production (Drupal PHP 8.4, BFF Node.js/Symfony, front React TypeScript). 4 environnements (dev, qa, test, prod).

Architecture IaC : 400+ fichiers Terraform, 33 modules réutilisables (13 Building Blocks + 20 modules Azure), framework BASK. Drift detection automatisée hebdomadaire.

Migration Container Apps : migration App Service vers Azure Container Apps avec zéro-downtime. Workload profiles D4/D16, autoscaling 1-25 replicas, sidecars OpenTelemetry.

Architecture réseau : Front Door Premium avec Private Link vers Container Apps, WAF Prevention mode, certificats managés, custom domains. NSG avec segmentation stricte prod/non-prod, private endpoints systématiques.

Bases de données HA : MySQL Flexible Server avec HA SameZone et géo-replica northeurope. PostgreSQL Flexible Server avec authentification Active Directory et managed identity. Redis Premium pour cache session.

CI/CD : 6+ workflows GitHub Actions par repo. OIDC Azure (zéro secret statique), matrix builds multi-env, targeted apply, backup pré-déploiement, sync automatisé prod vers non-prod. Intégration Trivy pour le scan de vulnérabilités des images Docker.

Monitoring : Application Insights avec alertes métier, Log Analytics, OpenTelemetry Collector sidecar, Dynatrace OneAgent injection.

Backup/DR : stratégie multi-couches (dump MySQL quotidien, snapshots NFS, Recovery Services Vault, Backup Vault rétention 30 jours, storage GZRS). Plan de reprise d'activité validé en sandbox (reconstruction complète de la plateforme en région paire).

Documentation architecture pour Design Authority : analyse managed identity vs access keys, flux d'authentification PKCE, matrices de flux réseau.

Environnement technique : Terraform 1.9.8, AzureRM 3.85+, azapi 2.8, Azure Container Apps, App Service, Front Door Premium, MySQL Flexible, PostgreSQL Flexible, Redis Premium, GitHub Actions, Docker, Trivy, Application Insights, OpenTelemetry, Dynatrace

### Ingénieure DevOps Azure - BearingPoint (janvier 2024 - juin 2024)

Audit et remédiation d'une plateforme Azure pour une application de crédit en environnement finance.

Audit complet de l'infrastructure Azure existante et identification des écarts de sécurité et de performance. Conception et mise en place d'une topologie réseau hub and spoke avec peering VNet et isolation des environnements. Déploiement de services Azure Container Apps, Azure Functions et Azure Web App. Automatisation de l'infrastructure avec Terraform et pipelines Azure DevOps. Implémentation des recommandations cybersécurité : NSG, Key Vault, RBAC, chiffrement en transit et au repos. Mise en place du monitoring avec Azure Monitor et Application Insights.

Environnement technique : Terraform, Azure DevOps, Azure Container Apps, Azure Functions, NSG, Key Vault, RBAC, Azure Monitor

### Ingénieure DevOps Azure - OnePoint (2021 - 2023)

Ingénieure DevOps sur plusieurs projets clients Azure dans les secteurs banque, énergie et industrie.

Conception et déploiement d'infrastructures Kubernetes (AKS) pour des applications microservices. Automatisation des déploiements avec Terraform et Ansible sur des environnements multi-subscriptions. Construction et maintenance de pipelines CI/CD Azure DevOps. Administration de clusters AKS en production : Helm charts, Azure Container Registry, autoscaling, monitoring. Gestion des environnements Linux, scripting Python et Bash pour l'automatisation des opérations. Accompagnement des équipes de développement sur les pratiques DevOps et la conteneurisation.

Environnement technique : AKS, Kubernetes, Terraform, Ansible, Azure DevOps, Docker, Helm, Python, Linux

### Développeuse Full Stack / DevOps / Auditrice accessibilité - Océane Consulting, Paris (2019 - 2021)

Développeuse full stack, DevOps et auditrice en accessibilité numérique sur des projets clients.

Développement backend en PHP/Symfony pour des applications web clients. Mise en place et maintenance d'infrastructures Azure. Automatisation des déploiements et gestion des environnements avec Azure DevOps. Audits d'accessibilité numérique (RGAA) : analyse de conformité, rédaction de rapports d'audit et recommandations de remédiation.

Environnement technique : PHP, Symfony, Azure, Azure DevOps, Docker, Linux, Python, Bash, Git

### Développeuse Full Stack / DevOps - Kraliss, Paris (2017 - 2019)

Développeuse full stack et DevOps sur une application de portefeuille électronique (wallet fintech).

Développement backend de l'application en PHP/Symfony. Conception et gestion de la base de données MySQL. Mise en place de l'environnement d'hébergement et des déploiements. Administration système Linux et scripting d'automatisation.

Environnement technique : PHP, Symfony, MySQL, OVH, Linux, Git, Docker

---

## Formation

Master Informatique spécialité DevOps - Sorbonne Université, Paris

Bachelor Responsable de Projet Informatique - ETNA, Paris

BTS Développeuse Full Stack

---

## Langues

Français : natif

Anglais : opérationnel (documentation technique, échanges professionnels)

---

## Informations

Localisation : Île-de-France

Mobilité : remote, hybride, sur site
