# data-vis-dashboard

## Preparing the local virtual environment

1. Install pipenv:

    ```bash
    pip install pipenv
    ```

    **Note**: If `pip` doesn't work, try `pip3`.

2. Define the python version:

    In the directory of the repository:

    ```bash
    pipenv --python /path/to/python
    ```

    **Note 1**: To get the `/path/to/python`, use `which python` or `which python3`
    **Note 2**: The minimum Python version to run this project is 3.8

3. Install the dependencies:

    In the directory of the repository:

    ```bash
    pipenv install
    ```

## Activating and exiting the virtual environment

To activate the virtual environment, use:

```bash
pipenv shell
```

To exit the virtual environment, use:

```bash
exit
```
