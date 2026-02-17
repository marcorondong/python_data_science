PYTHON = python3
POST_PROCESS = | cat -e

EX00 = ex00/Hello.py
EX01 = ex01/format_ft_time.py
EX02A = ex02/tester.py
EX02B = ex02/find_ft_type.py
EX03A = ex03/tester.py
EX03B = ex03/NULL_not_found.py
EX04 = ex04/whatis.py

SEPARATOR = \n========== $@ ==========\n

#------------------------------------ CODE ------------------------------------#
.PHONY: all ex00 ex01 ex02 ex03 ex04

all: ex00 ex01 ex02 ex03 ex04 clean

ex00:
	@printf "$(SEPARATOR)"
	$(PYTHON) $(EX00) $(POST_PROCESS)

ex01:
	@printf "$(SEPARATOR)"
	$(PYTHON) $(EX01) $(POST_PROCESS)

ex02:
	@printf "$(SEPARATOR)"
	$(PYTHON) $(EX02A) $(POST_PROCESS)
	@printf "$(SEPARATOR)"
	$(PYTHON) $(EX02B) $(POST_PROCESS)

ex03:
	@printf "$(SEPARATOR)"
	$(PYTHON) $(EX03A) $(POST_PROCESS)
	@printf "$(SEPARATOR)"
	$(PYTHON) $(EX03B) $(POST_PROCESS)

ex04:
	@printf "$(SEPARATOR)"
	$(PYTHON) $(EX04) 14
	$(PYTHON) $(EX04) -5
	$(PYTHON) $(EX04)
	$(PYTHON) $(EX04) 0
	$(PYTHON) $(EX04) Hi!
	$(PYTHON) $(EX04) 13 5

clean:
	@echo "Cleaning Python cache files..."
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@echo "Done."