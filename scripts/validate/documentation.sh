#!/usr/bin/env bash
set -euo pipefail

provider_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
export GIT_OPTIONAL_LOCKS=0
export PYTHONDONTWRITEBYTECODE=1
exec "${PYTHON:-python3}" "$provider_root/validators/documentation/validate.py" "$@" </dev/null
