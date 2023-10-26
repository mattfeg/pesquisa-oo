#!/bin/bash

# Encerra todos os agentes SSH ativos
pkill ssh-agent

# Inicia um novo agente SSH
eval "$(ssh-agent -s)"
