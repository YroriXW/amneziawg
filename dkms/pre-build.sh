#!/bin/bash
set -e
PATCH_FILE="$(dirname "$0")/patches/ipv6.patch"
KVER_MAJOR=$(echo "$kernelver" | cut -d. -f1)
KVER_MINOR=$(echo "$kernelver" | cut -d. -f2)

need_patch() {
    # Patch needed only on 7.1+
    [ "$KVER_MAJOR" -gt 7 ] || { [ "$KVER_MAJOR" -eq 7 ] && [ "$KVER_MINOR" -ge 1 ]; }
}

if need_patch; then
    echo "amneziawg: kernel $kernelver >= 7.1, applying ipv6.patch"
    patch -p1 -N --batch --quiet < "$PATCH_FILE" && \
        echo "amneziawg: ipv6.patch applied successfully" || \
        echo "amneziawg: ipv6.patch already applied, skipping"
else
    echo "amneziawg: kernel $kernelver does not need ipv6.patch"
fi
