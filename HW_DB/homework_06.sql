USE northwind;

/* 01 Выведите одним запросом с использованием UNION столбцы id, employee_id из таблицы orders
и соответствующие им столбцы из таблицы purchase_orders.
В таблице purchase_orders  created_by соответствует employee_id.*/

SELECT * FROM orders;
SELECT * FROM purchase_orders;

SELECT 
    id, employee_id
FROM
    orders 
UNION SELECT 
    id, created_by
FROM
    purchase_orders;


/* 02 Из предыдущего запроса удалите записи там где employee_id не имеет значения.
Добавьте дополнительный столбец со сведениями из какой таблицы была взята запись. */

SELECT * FROM orders;
SELECT * FROM purchase_orders;

SELECT 
    id, employee_id, 'orders' AS from_table
FROM
    orders
WHERE
    employee_id IS NOT NULL 
UNION SELECT 
    id, created_by, 'purchase' AS from_table
FROM
    purchase_orders;


/* 03 Выведите все столбцы таблицы order_details,
 а также дополнительный столбец payment_method из таблицы purchase_orders.
 Оставьте только заказы для которых известен payment_method.

 (Таблицы order_details и purchase_orders связаны по purchase_order_id)
 */

SELECT * FROM order_details;
SELECT * FROM purchase_orders;

SELECT 
    p.payment_method, od.*
FROM
    order_details AS od
        INNER JOIN
    purchase_orders AS p 
    ON od.purchase_order_id = p.id
WHERE
    p.payment_method IS NOT NULL;


-- 04 Выведите заказы orders и фамилии клиентов customers 
-- для тех заказов по которым были инвойсы таблица invoices.
SELECT * FROM orders;
SELECT * FROM customers;
SELECT * FROM invoices;

SELECT 
    o.id, cust.last_name
FROM
    orders AS o
        INNER JOIN
    customers AS cust ON o.customer_id = cust.id
        INNER JOIN
    invoices AS inv ON o.id = inv.order_id; 


-- 05 Подсчитайте количество инвойсов для каждого клиента из предыдущего запроса.

SELECT 
    o.id, cust.last_name, COUNT(inv.id) AS inv_count
FROM
    orders AS o
        INNER JOIN
    customers AS cust ON o.customer_id = cust.id
        INNER JOIN
    invoices AS inv ON o.id = inv.order_id
GROUP BY cust.id , cust.last_name; 
