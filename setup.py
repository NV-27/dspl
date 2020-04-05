from setuptools import setup, find_packages

requirements = [
    'astroid==2.3.3',
    'attrs==19.3.0',
    'backcall==0.1.0',
    'bayesian-optimization==1.0.1',
    'bcrypt==3.1.7',
    'bleach==3.1.4',
    'catboost==0.18.1',
    'cffi==1.13.2',
    'cloudpickle==1.2.1',
    'cryptography==2.8',
    'cycler==0.10.0',
    'dask==2.3.0',
    'decorator==4.4.1',
    'defusedxml==0.6.0',
    'entrypoints==0.3',
    'et-xmlfile==1.0.1',
    'fsspec==0.4.2',
    'future==0.18.2',
    'graphviz==0.13.2',
    'importlib-metadata==1.4.0',
    'ipykernel==5.1.3',
    'ipython==7.11.1',
    'ipython-genutils==0.2.0',
    'ipywidgets==7.5.1',
    'isort==4.3.21',
    'jdcal==1.4.1',
    'jedi==0.15.2',
    'Jinja2==2.10.3',
    'joblib==0.14.1',
    'jsonschema==3.2.0',
    'jupyter==1.0.0',
    'jupyter-client==5.3.4',
    'jupyter-console==6.0.0',
    'jupyter-core==4.6.1',
    'kiwisolver==1.1.0',
    'lazy-object-proxy==1.4.3',
    'lightgbm==2.3.0',
    'MarkupSafe==1.1.1',
    'matplotlib==3.1.2',
    'mccabe==0.6.1',
    'mistune==0.8.4',
    'more-itertools==8.1.0',
    'nbconvert==5.6.1',
    'nbformat==5.0.3',
    'notebook==5.7.8',
    'numpy==1.17.4',
    'openpyxl==3.0.0',
    'pandas==0.25.3',
    'pandocfilters==1.4.2',
    'paramiko==2.7.1',
    'parso==0.5.2',
    'pexpect==4.7.0',
    'pickleshare==0.7.5',
    'plotly==4.4.1',
    'prometheus-client==0.7.1',
    'prompt-toolkit==2.0.10',
    'ptyprocess==0.6.0',
    'pyarrow==0.14.1',
    'PyContracts==1.8.12',
    'pycparser==2.19',
    'pycryptodome==3.9.4',
    'Pygments==2.5.2',
    'pylint==2.4.4',
    'PyNaCl==1.3.0',
    'pyparsing==2.4.6',
    'pyrsistent==0.15.7',
    'python-dateutil==2.8.1',
    'pytz==2019.3',
    'pyzmq==18.1.1',
    'qtconsole==4.6.0',
    'retrying==1.3.3',
    'scikit-learn==0.22.1',
    'scipy==1.4.1',
    'seaborn==0.9.0',
    'Send2Trash==1.5.0',
    'shap==0.31.0',
    'six==1.14.0',
    'sklearn==0.0',
    'teradata==15.10.0.21',
    'teradatasql==16.20.0.59',
    'terminado==0.8.3',
    'testpath==0.4.4',
    'toolz==0.10.0',
    'tornado==6.0.3',
    'tqdm==4.41.1',
    'traitlets==4.3.3',
    'typed-ast==1.4.1',
    'wcwidth==0.1.8',
    'webencodings==0.5.1',
    'widgetsnbextension==3.5.1',
    'wrapt==1.11.2',
    'xgboost==0.90',
    'XlsxWriter==1.2.6',
    'zipp==1.0.0']

setup(
    name="dspl",
    packages=["dspl"],
    version="0.0.11",
    include_package_data=True,
    install_requires=requirements,
    author="Nikita Varganov",
    author_email="nikita.varganov.ml@gmail.com",
    license="MIT",
    description="Library for using in DS-Platform",
    url="https://github.com/NV-27/dspl",
    download_url="https://github.com/NV-27/dspl/archive/0.0.11.tar.gz",
    keywords=["dspl", "ds_platform", "ds_template"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent"
    ]
)