## Table of Contents

- [Deployment Options¶](#deployment-options)
  - [Overview¶](#overview)
  - [Self-Hosted Enterprise¶](#self-hosted-enterprise)
  - [Self-Hosted Lite¶](#self-hosted-lite)
  - [Cloud SaaS¶](#cloud-saas)
  - [Bring Your Own Cloud¶](#bring-your-own-cloud)
  - [Related¶](#related)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

Deployment Options

Initializing search

GitHub

  * Home 
  * Tutorials 
  * How-to Guides 
  * Conceptual Guides 
  * Reference 

GitHub

  * Home 
  * Tutorials 
  * How-to Guides 
  * Conceptual Guides 

Conceptual Guides

    * LangGraph  LangGraph 
      * LangGraph 
      * Why LangGraph? 
      * LangGraph Glossary 
      * Agent architectures 
      * Multi-agent Systems 
      * Human-in-the-loop 
      * Persistence 
      * Memory 
      * Streaming 
      * FAQ 
    * LangGraph Platform  LangGraph Platform 
      * LangGraph Platform 
      * High Level  High Level 
        * High Level 
        * LangGraph Platform 
        * Deployment Options  Deployment Options  Table of contents 
          * Overview 
          * Self-Hosted Enterprise 
          * Self-Hosted Lite 
          * Cloud SaaS 
          * Bring Your Own Cloud 
          * Related 
        * LangGraph Platform Plans 
        * Template Applications 
      * Components 
      * LangGraph Server 
      * Deployment Options 
  * Reference 

Table of contents

  * Overview 
  * Self-Hosted Enterprise 
  * Self-Hosted Lite 
  * Cloud SaaS 
  * Bring Your Own Cloud 
  * Related 

  1. Home 
  2. Conceptual Guides 
  3. LangGraph Platform 
  4. High Level 

# Deployment Options¶

Prerequisites

  * LangGraph Platform
  * LangGraph Server
  * LangGraph Platform Plans

## Overview¶

There are 4 main options for deploying with the LangGraph Platform:

  1. **Self-Hosted Lite** : Available for all plans.

  2. **Self-Hosted Enterprise** : Available for the **Enterprise** plan.

  3. **Cloud SaaS** : Available for **Plus** and **Enterprise** plans.

  4. **Bring Your Own Cloud** : Available only for **Enterprise** plans and **only on AWS**.

Please see the LangGraph Platform Plans for more information on the different
plans.

The guide below will explain the differences between the deployment options.

## Self-Hosted Enterprise¶

Important

The Self-Hosted Enterprise version is only available for the **Enterprise**
plan.

With a Self-Hosted Enterprise deployment, you are responsible for managing the
infrastructure, including setting up and maintaining required databases and
Redis instances.

You’ll build a Docker image using the LangGraph CLI, which can then be
deployed on your own infrastructure.

For more information, please see:

  * Self-Hosted conceptual guide
  * Self-Hosted Deployment how-to guide

## Self-Hosted Lite¶

Important

The Self-Hosted Lite version is available for all plans.

The Self-Hosted Lite deployment option is a free (up to 1 million nodes
executed), limited version of LangGraph Platform that you can run locally or
in a self-hosted manner.

With a Self-Hosted Lite deployment, you are responsible for managing the
infrastructure, including setting up and maintaining required databases and
Redis instances.

You’ll build a Docker image using the LangGraph CLI, which can then be
deployed on your own infrastructure.

For more information, please see:

  * Self-Hosted conceptual guide
  * Self-Hosted deployment how-to guide

## Cloud SaaS¶

Important

The Cloud SaaS version of LangGraph Platform is only available for **Plus**
and **Enterprise** plans.

The Cloud SaaS version of LangGraph Platform is hosted as part of LangSmith.

The Cloud SaaS version of LangGraph Platform provides a simple way to deploy
and manage your LangGraph applications.

This deployment option provides an integration with GitHub, allowing you to
deploy code from any of your repositories on GitHub.

For more information, please see:

  * Cloud SaaS Conceptual Guide
  * How to deploy to Cloud SaaS

## Bring Your Own Cloud¶

Important

The Bring Your Own Cloud version of LangGraph Platform is only available for
**Enterprise** plans.

This combines the best of both worlds for Cloud and Self-Hosted. We manage the
infrastructure, so you don't have to, but the infrastructure all runs within
your cloud. This is currently only available on AWS.

For more information please see:

  * Bring Your Own Cloud Conceptual Guide

## Related¶

For more information, please see:

  * LangGraph Platform plans
  * LangGraph Platform pricing
  * Deployment how-to guides

## Comments

Back to top

Previous

LangGraph Platform

Next

LangGraph Platform Plans

Made with  Material for MkDocs Insiders