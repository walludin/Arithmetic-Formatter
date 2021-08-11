# This entrypoint file to be used in development. Start by reading README.md
from arithmetic import arithmetic_arranger
from unittest import main

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], False)
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
