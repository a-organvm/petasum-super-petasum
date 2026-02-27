#!/bin/bash

# Simulating the vulnerable run step:
# LABELS="${{ join(github.event.issue.labels.*.name, ',') }}"

# Attack payload: Close the quote, run a command, comment out the rest
# Note: In bash, if the variable is inside double quotes, it's harder to break out unless the value contains "
# But GitHub interpolation happens BEFORE bash sees it.

MALICIOUS_INPUT='test", "another"; echo "INJECTED COMMAND EXECUTED"; #'

# This is what the script looks like after GitHub interpolation
GENERATED_SCRIPT="LABELS=\"$MALICIOUS_INPUT\""

echo "--- Generated Script ---"
echo "$GENERATED_SCRIPT"
echo "--- Execution Output ---"

eval "$GENERATED_SCRIPT"
