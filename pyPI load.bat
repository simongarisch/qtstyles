rem call activate py27
call activate py36

rem make sure we are up to date
python -m pip install --user --upgrade setuptools wheel
python -m pip install --upgrade twine

rem now build
python setup.py sdist bdist_wheel

rem and push
python -m twine upload dist/*

pause