#!/usr/bin/env bash
# Serves this deck on http://localhost:8619 so embedded videos play inline, then opens it in your browser.
cd "$(dirname "$0")"
( sleep 1; (xdg-open "http://localhost:8619/index.html" || open "http://localhost:8619/index.html" || explorer.exe "http://localhost:8619/index.html") >/dev/null 2>&1 ) &
exec python3 -m http.server 8619
