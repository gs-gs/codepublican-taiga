# Taiga Project Management for CodeOnTap Deployment

This repo contains the overrides and customisation required to deploy the Taiga Project Management tool using CodeOnTap to an AWS based environment. It will mostly contain deployment specific changes such as container images, secrets management etc.. This may change as the usage of Taiga expands.

## Taiga Software

The Docker images will are built based on the production installation process outlined in the [Taiga Documentation](https://taigaio.github.io/taiga-doc/dist/setup-production.html#_introduction).

For now we will be using a fixed versions of Taiga

- [taiga-back](https://github.com/taigaio/taiga-back) - Release: 4.2.12
- [taiga-front](https://github.com/taigaio/taiga-front) - Release: 4.2.13
