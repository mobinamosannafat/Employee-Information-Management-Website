# Employee Information Management Website

Implementation of Employee Information Management Website using django.

This website includes the following pages:

### Admin login page:
Admin logs in the main page of the website by entering the username and password.


### Information registration page: 
On this page there is a form that contains employee information that includes first name, last name, national code, personal code, phone, address, single or married, age and income, and the manager can Enter the employee information by entering the information and pressing the confirmation button.


### Information editing page:
In this page, which is similar to the information registration page, the same form is displayed and the manager can edit all the details of the employees except the personl code field.


### Delete information page:
This page is similar to the information registration page, except that the manager deletes an employee by entering the personal code of this employee and pushing the delete button.


### Reporting page:
On this page, the manager can make various reports on employee information. These reports should be based on last name, age, maritial status, as well as a combination of these.


## Statistical reporting page:
This page is for statistical reporting and the manager should be able to retrieve the following reports:
- Number of married employees
- Number of single employees
- Number of employees which their income is above 1,000,000
- Information of the employees with the most and least incomes
- Total staff salaries
- Deviation of personnel salary criteria (in order to analyze the degree of dispersion of staff salaries)


### REST APIs:
- GET / myget / ali / : List of all employees whose name is Ali will be returned.
- POST / myupdate / 123/5000000 / : Salary of an employee whose personal code is 123 changes to 5000000.
- DELETE / mydel / married / : All married employees will be removed.
- DELETE / mydel / single / : All single employees will be removed.
