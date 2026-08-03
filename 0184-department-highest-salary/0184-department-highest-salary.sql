# Write your MySQL query statement below
with dense_ranked as (select salary,departmentid,name,rank() over (partition by departmentid order by salary desc) as rnk from employee)
select dept.name as Department,emp.name as Employee,emp.salary as Salary from dense_ranked as emp 
join department dept on emp.departmentid=dept.id 
where rnk=1