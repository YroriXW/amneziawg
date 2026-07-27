#!/bin/bash
set -e

KVER="${1:-$kernelver}"

if [ -z "$KVER" ]; then
    echo "amneziawg: Error - kernelver is not set"
    exit 1
fi

KVER_CLEAN=$(echo "$KVER" | grep -oE '^[0-9]+(\.[0-9]+)*')

KVER_MAJOR=$(echo "$KVER_CLEAN" | cut -d. -f1)
KVER_MINOR=$(echo "$KVER_CLEAN" | cut -d. -f2)
KVER_PATCH=$(echo "$KVER_CLEAN" | cut -d. -f3)

KVER_MAJOR=${KVER_MAJOR:-0}
KVER_MINOR=${KVER_MINOR:-0}
KVER_PATCH=${KVER_PATCH:-0}

apply_patch() {
    local patch_file="$1"
    local patch_name="$(basename "$patch_file")"

    if [ ! -f "$patch_file" ]; then
        echo "amneziawg: ERROR - patch file $patch_name not found!"
        exit 1
    fi

    if patch -p1 -R --dry-run --silent < "$patch_file" >/dev/null 2>&1; then
        echo "amneziawg: $patch_name already applied, skipping."
    else
        echo "amneziawg: applying $patch_name..."
        patch -p1 --batch --quiet < "$patch_file"
        echo "amneziawg: $patch_name applied successfully."
    fi
}

if [ "$KVER_MAJOR" -gt 7 ] || { [ "$KVER_MAJOR" -eq 7 ] && [ "$KVER_MINOR" -ge 1 ]; }; then
    echo "amneziawg: kernel $KVER >= 7.1, checking ipv6.patch"
    apply_patch "$(dirname "$0")/patches/ipv6.patch"
else
    echo "amneziawg: kernel $KVER < 7.1, does not need ipv6.patch"
fi

if [ "$KVER_MAJOR" -gt 7 ] || \
   { [ "$KVER_MAJOR" -eq 7 ] && [ "$KVER_MINOR" -gt 1 ]; } || \
   { [ "$KVER_MAJOR" -eq 7 ] && [ "$KVER_MINOR" -eq 1 ] && [ "$KVER_PATCH" -ge 5 ]; }; then
    echo "amneziawg: kernel $KVER >= 7.1.5, checking socketfix.patch"
    apply_patch "$(dirname "$0")/patches/socketfix.patch"
else
    echo "amneziawg: kernel $KVER < 7.1.5, skipping socketfix.patch"
fi
