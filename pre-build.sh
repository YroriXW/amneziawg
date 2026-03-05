#!/bin/bash
set -e
PATCH_FILE="$(dirname "$0")/patches/blake2s.patch"
KVER_MAJOR=$(echo "$kernelver" | cut -d. -f1)
KVER_MINOR=$(echo "$kernelver" | cut -d. -f2)
need_patch() {
    [ "$KVER_MAJOR" -gt 6 ] && return 0
    [ "$KVER_MAJOR" -eq 6 ] && [ "$KVER_MINOR" -ge 18 ] && return 0
    return 1
}
if need_patch; then
    echo "amneziawg: kernel $kernelver >= 6.18, applying blake2s.patch"
    patch -p1 -N --batch --quiet < "$PATCH_FILE" && \
        echo "amneziawg: blake2s.patch applied successfully" || \
        echo "amneziawg: blake2s.patch already applied, skipping"
else
    echo "amneziawg: kernel $kernelver < 6.18, blake2s.patch not needed"
fi
