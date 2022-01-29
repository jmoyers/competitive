/**
---
title: Second Highest Salary
difficulty: easy
number: 176
tags:
- sql
- max
- subqueries
links:
- https://leetcode.com/problems/second-highest-salary/
- https://www.geeksforgeeks.org/sql-query-to-find-second-largest-salary/
---
' SQL Schema
' 
' Write a SQL query to get the second highest salary from the Employee table.
' 
' +----+--------+
' | Id | Salary |
' +----+--------+
' | 1  | 100    |
' | 2  | 200    |
' | 3  | 300    |
' +----+--------+
' 
' For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.
' 
' +---------------------+
' | SecondHighestSalary |
' +---------------------+
' | 200                 |
' +---------------------+
**/
select max(salary) as SecondHighestSalary from Employee where salary < (select max(salary) from Employee)

-- this uses a subquery to generate the first max, then finds the next highest
-- salary. if asked for the nth highest salary, i'd probably come up with a
-- way to rank them. DENSE_RANK() looks reasonable