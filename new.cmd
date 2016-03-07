@echo off
SET /p directory=Enter problem please:
mkdir %directory%
copy solution.py C:\Users\Yongle\leetcode\%directory%\solution.py
cd C:\Users\Yongle\leetcode\%directory%
subl solution.py