PYTHON = python3
POST_PROCESS = | cat -e

EX00 = ex00/Hello.py
EX01 = ex01/format_ft_time.py

#------------------------------------ CODE ------------------------------------#
.PHONY: all ex00 ex01

all: ex00 ex01

ex00:
	$(PYTHON) $(EX00) $(POST_PROCESS)

ex01:
	$(PYTHON) $(EX01) $(POST_PROCESS)
