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

PATCH_FILE="$(dirname "$0")/patches/socketfix.patch"

# DKMS passes kernel version in $kernelver
KVER="$kernelver"

KVER_BASE="${KVER%%-*}"

KVER_MAJOR=$(echo "$KVER_BASE" | cut -d. -f1)
KVER_MINOR=$(echo "$KVER_BASE" | cut -d. -f2)
KVER_PATCH=$(echo "$KVER_BASE" | cut -d. -f3)

# Safety defaults
KVER_PATCH=${KVER_PATCH:-0}

need_patch() {
    # Patch needed only on >= 7.1.5
    [ "$KVER_MAJOR" -gt 7 ] || \
    { [ "$KVER_MAJOR" -eq 7 ] && [ "$KVER_MINOR" -gt 1 ]; } || \
    { [ "$KVER_MAJOR" -eq 7 ] && [ "$KVER_MINOR" -eq 1 ] && [ "$KVER_PATCH" -ge 5 ]; }
}

if need_patch; then
    echo "amneziawg: kernel $KVER >= 7.1.5, applying socketfix.patch"

    if patch -p1 -N --batch --quiet < "$PATCH_FILE"; then
        echo "amneziawg: socketfix.patch applied successfully"
    else
        echo "amneziawg: socketfix.patch already applied or not needed, skipping"
    fi
else
    echo "amneziawg: kernel $KVER < 7.1.5, skipping socketfix.patch"
fi
