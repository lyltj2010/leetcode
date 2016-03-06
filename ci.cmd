@echo off
SET /p comment=Enter commit please: 
git add -A && git commit -m "%comment%"
