DynamicFieldFlow is a library that allows to simulate neural dynamic architectures built using [DynamicFieldPy](https://github.com/danielsabinasz/DynamicFieldPy) by means of the [TensorFlow](https://www.tensorflow.org) framework, and to train the parameters of such architectures via backpropagation through time.

Please check out the Jupyter notebook
[getting_started.ipynb](getting_started.ipynb) or the [examples](examples) folder to get started.

Running examples
----------------

There are two common ways to run the examples in this repository:

1) Headless / CI-friendly (saves plots to disk)

	 - Activate your venv and run the example. The examples will save a PNG in the repository (and the file is ignored by Git):

		 ```bash
		 .venv/bin/python examples/field_2d.py
		 ls -lh field_2d.png
		 ```

2) Interactive (recommended for local development)

	 - Install Jupyter tooling and run the file in the VS Code Interactive Window, or install a GUI backend (for example PyQt5) to open native plot windows:

		 ```bash
		 # interactive inline in VS Code
		 .venv/bin/pip install jupyter ipykernel

		 # or, open native windows (requires a desktop/display)
		 .venv/bin/pip install pyqt5
		 MPLBACKEND=Qt5Agg .venv/bin/python examples/field_2d.py
		 ```

	 - In VS Code: select the `.venv` interpreter, open the example, and use "Run File in Interactive Window" to see inline plots.
