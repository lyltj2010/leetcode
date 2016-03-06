@echo off
SET /p directory=Enter problem please:
mkdir %directory% 
cd C:\Users\Yongle\leetcode\%directory%
call>solution.py
subl solution.py