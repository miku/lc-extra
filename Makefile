Commands.pdf: Commands.md
	pandoc --template eisvogel -f markdown -t latex -o $@ $<

.PHONY: clean
clean:
	rm -f Commands.pdf

