@echo off
rem Serves this deck on http://localhost:8619 so embedded videos play inline, then opens it in your browser.
cd /d "%~dp0"
start "" "http://localhost:8619/index.html"
where py >nul 2>nul && (py -m http.server 8619 & goto :eof)
where python >nul 2>nul && (python -m http.server 8619 & goto :eof)
echo Python not found. Install Python, or open index.html directly (videos then open on YouTube).
pause
