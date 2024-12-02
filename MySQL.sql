-- Referenced from SQL50 in leetcode


-- if no id, find same 
SELECT Distinct author_id as id from Views 
where author_id=viewer_id
order by id

-- count character
SELECT Distinct author_id as id from Views 
where author_id=viewer_id
order by id

--Left Join (From table as main identifier and rows count) 
SELECT
EmployeeUNI.unique_id, Employees.name
FROM EmployeeUNI
LEFT JOIN Employees on Employees.id = EmployeeUNI.id

-- | id | name     |
-- | -- | -------- |
-- | 1  | Alice    |
-- | 7  | Bob      |
-- | 11 | Meir     |
-- | 90 | Winston  |
-- | 3  | Jonathan |

-- | id | unique_id |
-- | -- | --------- |
-- | 3  | 1         |
-- | 11 | 2         |
-- | 90 | 3         |

-- Result:
-- | unique_id | name     |
-- | --------- | -------- |
-- | 1         | Jonathan |
-- | 2         | Meir     |
-- | 3         | Winston  |

-- Join 
Select 
     p.product_name, s.year, s.price
From
    Sales s
JOIn Product p on s.product_id = p.product_id

-- Not In 
SELECT customer_id, COUNT(v.visit_id) as count_no_trans 
FROM Visits v
LEFT JOIN Transactions t ON v.visit_id = t.visit_id
WHERE transaction_id IS NULL
GROUP BY customer_id

-- Input: 
-- Visits
-- +----------+-------------+
-- | visit_id | customer_id |
-- +----------+-------------+
-- | 1        | 23          |
-- | 2        | 9           |
-- | 4        | 30          |
-- | 5        | 54          |
-- | 6        | 96          |
-- | 7        | 54          |
-- | 8        | 54          |
-- +----------+-------------+
-- Transactions
-- +----------------+----------+--------+
-- | transaction_id | visit_id | amount |
-- +----------------+----------+--------+
-- | 2              | 5        | 310    |
-- | 3              | 5        | 300    |
-- | 9              | 5        | 200    |
-- | 12             | 1        | 910    |
-- | 13             | 2        | 970    |
-- +----------------+----------+--------+
-- Output: 
-- +-------------+----------------+
-- | customer_id | count_no_trans |
-- +-------------+----------------+
-- | 54          | 2              |
-- | 30          | 1              |
-- | 96          | 1              |
-- +-------------+----------------+
-- Explanation: 
-- Customer with id = 23 visited the mall once and made one transaction during the visit with id = 12.
-- Customer with id = 9 visited the mall once and made one transaction during the visit with id = 13.
-- Customer with id = 30 visited the mall once and did not make any transactions.
-- Customer with id = 54 visited the mall three times. During 2 visits they did not make any transactions, and during one visit they made 3 transactions.
-- Customer with id = 96 visited the mall once and did not make any transactions.
