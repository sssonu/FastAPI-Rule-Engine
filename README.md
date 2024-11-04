#### Overview
A simple 3-tier rule engine application built with Flask that determines user eligibility based on attributes
using an Abstract Syntax Tree (AST) to represent conditional rules.

#### Snapshots
1) UI
![User Interface](https://github.com/user-attachments/assets/ddd2a943-78d0-4947-85a2-3e3d461ec0f1)

2) Rule Creation

   ![Rule Creation](https://github.com/user-attachments/assets/80bc258e-2a80-4776-a369-94591f90b18d)

3) Evaluate Rule

   ![Evaluate rule](https://github.com/user-attachments/assets/3fabd085-329a-4e54-b0f8-0a00644f0faa)

4) Combine rule


   ![Combined rule](https://github.com/user-attachments/assets/f8453ded-af5a-49ab-8188-3dbde4678a93)

   




#### Features
1) Create ,Evaluate and Combine eligibility rules.
2) Use of Abstract Syntax Tree (AST) for rule representation.
3) RESTful API for rule management.
4) Simple UI for interacting with the rule engine.

#### Technologies Used
1) Backend: Flask
2) Database :SQLite
3) Frontend : HTML/ CSS
4) Libraries : Flask- SQLAlchemy, Werkzeug

### Installation
##### Steps
1) Clone the repository in Visual Studio code : <code> https://github.com/sssonu/FastAPI-Rule-Engine.git </code>
2) Create virtual environment : <code> python -m venv venv </code>
3) Activate Virtual environment:<code>On Windows</code> <code> venv\Scripts\activate </code>
4) Install the dependencies : <code> pip install -r requirements.txt </code>
5) Set up Database : <code> pip install mysql-connector-python #No installation is needed as Python includes sqlite3 by default. </code>
6) Run the application : <code> python main.py </code>
7) You will see a link something like this <code> http://127.0.0.1:5000/ </code>.
