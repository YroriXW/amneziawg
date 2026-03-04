#!/bin/sh

set -e

test_pubkey() {
    echo "Testing pubkey generation"
    expected_key="L+V9o0fNYkMVKNqsX7spBzD/9oSvxM/C7ZCZX1jLO3Q="
    generated_key="$(head -c 32 /dev/zero | base64 | src/wg pubkey)"
    test "$expected_key" = "$generated_key" || {
        echo "Expected and generated keys must be equal" >&2
        echo "expected_key=$expected_key" >&2
        echo "generated_key=$generated_key" >&2
        exit 1
    }
    echo "ok"
}

test_wg_command() {
    echo "Testing command $1"
    a="$(src/wg $1)"
    b="$(src/wg $1)"
    test -n "$a" && test -n "$b" || {
        echo "\"a\" and \"b\" must not be empty" >&2
        echo "a=$a" >&2
        echo "b=$b" >&2
        exit 1
    }
    test "$a" != "$b" || {
        echo "\"a\" and \"b\" must be different" >&2
        echo "a=$a" >&2
        echo "b=$b" >&2
        exit 1
    }
    echo "ok"
}

test_pubkey
test_wg_command genpsk
test_wg_command genkey
