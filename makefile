default:
	@echo -e 'Commands:\n make save\n\tSaves changes\n\n make reset\n\tResets changes\n\n make setupbins\n\tSets the exectubles in ~/.local/bin'

setupbins:
	@echo Not implemented.

save: ~/.local/pipx/venvs/rainbowstream/lib64/python3.8/site-packages/rainbowstream/rainbow.py

~/.local/pipx/venvs/rainbowstream/lib64/python3.8/site-packages/rainbowstream/rainbow.py: ./rainbow.py
	cp ./rainbow.py ~/.local/pipx/venvs/rainbowstream/lib64/python3.8/site-packages/rainbowstream/rainbow.py

reset: ./rainbow.py

./rainbow.py: ~/.local/pipx/venvs/rainbowstream/lib64/python3.8/site-packages/rainbowstream/rainbow.py
	cp ~/.local/pipx/venvs/rainbowstream/lib64/python3.8/site-packages/rainbowstream/rainbow.py ./rainbow.py
