#!/bin/sh

set -e

PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python ./client.py --speculos --app ../target/riscv32imc-unknown-none-elf/release/demo "$@"
