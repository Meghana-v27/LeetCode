# Write your MySQL query statement below
select dept.name as Department,emp.name as Employee,emp.salary as Salary from employee emp 
join department dept 
on emp.departmentid=dept.id 
where (emp.departmentid,emp.salary) in
(select departmentid,max(salary)
from employee
group by departmentid)