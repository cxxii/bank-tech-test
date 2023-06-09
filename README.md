# Bank Tech Test

A basic ATM style application that allows the user to make deposits and withdrawls, and prints a formatted statement of transactions.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.10 or later

### Installing

To install the bank tech test, follow these steps:

1. Make sure you have the prerequisites listed above, if not, install/get them

2. Clone the repository: For this step, you need Git installed.

   ```bash
   git clone https://github.com/cxxii/bank-tech-test.git
   ```

3. Navigate to the directory where the repository was downloaded

    ```bash
    cd bank-tech-test
    ```

## Usage

1. Navigate to directory of bank_tech.py

2. Open Python interactive shell

    ```bash
    python3
    ```

3. Import module

    ```python
    >>> import bank_tech
    ```

4. Create an instance of the Bank class by calling its constructor

    ```python
    >>> bank = bank_tech.Bank()
    ```

5. Call the methods of the Bank instance as needed

    ```python
    >>> bank.deposit(22425.27, "31/10/20")
    >>> bank.deposit(365, "21/11/20")
    >>> bank.withdraw(3389.55, "24/12/22")
    >>> bank.statement()
    ```

    ![screenshot](https://github.com/cxxii/bank-tech-test/blob/main/screenshot.png)

## Running the tests & coverage

To run all tests, run the following command:

```bash
pytest bank_tech_tests.py
```

To view the coverage report, run the following command:

```bash
coverage run bank_tech_tests.py 
coverage report bank_tech_tests.py
```

## Version

v1.0.1

## Authors

* **Callum Clark**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
