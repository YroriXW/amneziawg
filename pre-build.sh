#!/bin/bash
set -e
PATCH_FILE="$(dirname "$0")/patches/blake2s.patch"
KVER_MAJOR=$(echo "$kernelver" | cut -d. -f1)
KVER_MINOR=$(echo "$kernelver" | cut -d. -f2)

need_patch() {
    # Only potentially needed on 6.18+
    [ "$KVER_MAJOR" -gt 6 ] || { [ "$KVER_MAJOR" -eq 6 ] && [ "$KVER_MINOR" -ge 18 ]; } || return 1
    # Check actual API: patch is needed only if kernel uses blake2s_ctx (new API).
    # Kernels like xanmod that stayed on blake2s_state (old API) don't need it.
    grep -q 'struct blake2s_ctx' \
        "/lib/modules/${kernelver}/build/include/crypto/blake2s.h" 2>/dev/null
}

if need_patch; then
    echo "amneziawg: kernel $kernelver >= 6.18 with new blake2s API, applying blake2s.patch"
    patch -p1 -N --batch --quiet < "$PATCH_FILE" && \
        echo "amneziawg: blake2s.patch applied successfully" || \
        echo "amneziawg: blake2s.patch already applied, skipping"
else
    echo "amneziawg: kernel $kernelver does not need blake2s.patch"
fi
