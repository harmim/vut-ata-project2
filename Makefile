# Author: Dominik Harmim <harmim6@gmail.com>

PACK := proj2.zip
LOG := cart_log.txt
BAD_LOG := bad_log.txt
REQUESTS := requests.csv
MONITOR := cart_monitor.py
TEST := cartctl_test.py
AUTOMATA_DIR := automata
AUTOMATA = automaty.pdf


.PHONY: monitor
monitor: $(LOG)
	./$(MONITOR) < $<


.PHONY: bad
bad: $(BAD_LOG)
	./$(MONITOR) < $<


.PHONY: mklog
mklog: $(LOG)

$(LOG): $(REQUESTS)
	./$(TEST) $< > $@


.PHONY: pack
pack: $(PACK)

$(PACK): $(MONITOR) $(REQUESTS)
	cp $(AUTOMATA_DIR)/$(AUTOMATA) .
	zip -9 $@ $^ $(AUTOMATA)
	rm $(AUTOMATA)


.PHONY: clean
clean:
	rm -rf $(PACK) $(LOG) $(AUTOMATA) __pycache__/
