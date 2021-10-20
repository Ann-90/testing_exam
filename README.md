# TESTING EXAM PROJECT
TESTING EXAM

This is the exam task. You should check bunch of tests with pytest lib:
 
* Clone the project. For example:

`git clone git@github.com:Ann-90/testing_exam.git`

* Enter the root directory of the project

`cd testing_exam`

* In the root directory create the environment

`python3 -m venv {env_name}`

`env_name/bin/activate`

`pip3 install -r requirements.txt`

* Run the test project

`pytest -v`

* If you need specific test-set choose `test_main_page.py` or `test_product_page.py` files. For example:

`pytest -v test_product_page.py`
* If you need specific test chose for example:

`pytest -v test_product_page.py::test_message_disappeared_after_adding_product_to_basket`

* Don't forget to drink your tea. It will be the long way 
 
