echo $PYTHONPATH
export PYTHONPATH=$(pwd)/src

echo $PYTHONPATH
python -m pytest tests
