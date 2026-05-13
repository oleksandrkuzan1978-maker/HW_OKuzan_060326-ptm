USE northwind;

SELECT * FROM products;
SELECT * FROM order_details;
SELECT * FROM orders;

/* 01 Вывести названия продуктов (таблица products),
включая количество заказанных единиц quantity для каждого продукта таблица order_details.
Решить задачу с помощью CTE и подзапроса. */
/* Решение исходит из следующего понимания задания: Вывести наименования всех продуктов,
 а ТАКЖЕ показать общее количество заказанных единиц каждого из продуктов.*/
-- 1) CTE

WITH order_prod AS (
    SELECT 
		product_id,
        SUM(quantity) AS total_quantity
    FROM order_details
    GROUP BY product_id
)
SELECT 
    p.product_name,
    op.total_quantity 
FROM products as p
LEFT JOIN order_prod as op 
    ON p.id = op.product_id;



-- 2)  Подзапрос

SELECT 
    p.product_name,
    (SELECT SUM(od.quantity)
        FROM order_details as od
        WHERE od.product_id = p.id
        GROUP BY product_id
    ) AS total_quantity
FROM products as p;


/* 02 Найти все заказы таблица orders,
сделанные после даты самого первого заказа клиента Lee таблица customers. */

-- Через CTE
WITH f AS (SELECT min(o.order_date) AS first_order_Lee 
FROM customers AS cust
JOIN orders AS o
ON cust.id = o.customer_id
WHERE cust.last_name = "Lee") 

SELECT id, order_date FROM orders
WHERE order_date > (SELECT first_order_Lee FROM f);

-- Через SubQuery
SELECT 
    id, order_date
FROM
    orders
WHERE
    order_date > (SELECT 
            MIN(o.order_date) AS first_order
        FROM
            customers AS cust
                JOIN
            orders AS o ON cust.id = o.customer_id
        WHERE
            cust.last_name = 'Lee');





-- 03 Найти все продукты таблицы products c максимальным target_level.
SELECT 
    id, product_name, target_level
FROM
    products
WHERE
    target_level = (SELECT 
            MAX(target_level)
        FROM
            products);
