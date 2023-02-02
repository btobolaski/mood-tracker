result: staticfiles flake.lock flake.nix
	nix build
staticfiles: poetry.lock pyproject.toml tracker mood_tracker
	python manage.py collectstatic
	git add staticfiles
