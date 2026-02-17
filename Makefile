PYTHON = python3
POST_PROCESS = | cat -e

EX00 = ex00/Hello.py
EX01 = ex01/format_ft_time.py
EX02A = ex02/tester.py
EX02B = ex02/find_ft_type.py
EX03A = ex03/tester.py
EX03B = ex03/NULL_not_found.py
EX04 = ex04/whatis.py
EX05 = ex05/building.py
EX06 = ex06/filterstring.py

EXERCISES = ex00 ex01 ex02 ex03 ex04 ex05 ex06 ex07 ex08 ex09
SEPARATOR = \n========== $@ ==========\n

#------------------------------------ CODE ------------------------------------#
.PHONY: all $(EXERCISES) clean check-doc

all: $(EXERCISES)

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

ex05:
	@printf "$(SEPARATOR)"
	$(PYTHON) $(EX05) "Python 3.0, released in 2008, was a major revision that is not completely backward compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
	$(PYTHON) $(EX05) wrong input

ex06:
	@printf "$(SEPARATOR)"
	$(PYTHON) $(EX06) 'Hello the World' 4
	$(PYTHON) $(EX06) 'Hello the World' 99
	$(PYTHON) $(EX06) 3 'Hello the World'
	$(PYTHON) $(EX06)

clean:
	@echo "Cleaning Python cache files..."
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@echo "Done."

check-doc:
	$(PYTHON) tools/check_docstrings.py .