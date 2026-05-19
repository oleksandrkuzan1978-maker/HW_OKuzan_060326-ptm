USE northwind;
SELECT * FROM purchase_order_details;

-- 01 Для каждого заказа purchase_order_id выведите минимальный, максимальный и средний unit_cost.

SELECT purchase_order_id
, min(unit_cost) OVER (PARTITION BY purchase_order_id) AS min_cost
, max(unit_cost) OVER (PARTITION BY purchase_order_id) AS max_cost
, avg(unit_cost) OVER (PARTITION BY purchase_order_id) AS avg_cost
 FROM purchase_order_details;   

-- 02 ставьте только уникальные строки из предыдущего запроса.

SELECT DISTINCT purchase_order_id
, min(unit_cost) OVER (PARTITION BY purchase_order_id) AS min_cost
, max(unit_cost) OVER (PARTITION BY purchase_order_id) AS max_cost
, avg(unit_cost) OVER (PARTITION BY purchase_order_id) AS avg_cost
 FROM purchase_order_details;    

SELECT purchase_order_id
, min(unit_cost) AS min_cost
, max(unit_cost) AS max_cost
, avg(unit_cost) AS avg_cost
 FROM purchase_order_details
 GROUP BY purchase_order_id
 ;    
 
/* 03 Посчитайте стоимость продукта в заказе как quantity * unit_cost.
Выведите суммарную стоимость продуктов с помощью оконной функции
для каждого purchase_order_id.
Сделайте то же самое с помощью GROUP BY. */
-- OVER (с повторами номеров заказа)

SELECT purchase_order_id, quantity, unit_cost
, quantity * unit_cost 
  AS total_cost 
, sum(quantity * unit_cost) OVER (PARTITION BY purchase_order_id
) AS sum_cost
FROM 
  purchase_order_details;  

    
-- OVER (без повторов номеров заказа)

SELECT DISTINCT purchase_order_id 
, sum(quantity * unit_cost) OVER (PARTITION BY purchase_order_id) AS sum_cost
 FROM purchase_order_details;  
 
-- GROUP BY

SELECT 
    purchase_order_id,
    ROUND(SUM(quantity * unit_cost), 2) AS sum_cost
FROM
    purchase_order_details
GROUP BY purchase_order_id;  

/* 04 Посчитайте количество заказов по дате получения и posted_to_inventory.
Если оно превышает 1 то выведите '>1' в противном случае '=1'.*/

-- ВАРИАНТ №1
SELECT DISTINCT date_received, posted_to_inventory,
COUNT(*) OVER (PARTITION BY date_received, posted_to_inventory) AS Num_Orders,
 CASE 
 WHEN (COUNT(*) OVER (PARTITION BY date_received, posted_to_inventory)
 ) > 1 
 THEN ">1"
 ELSE "=1" END AS Comparison
FROM purchase_order_details;

-- ВАРИАНТ №2
SELECT
    date_received, posted_to_inventory,
    COUNT(*) AS Num_Orders,
    CASE
        WHEN COUNT(*) > 1 THEN '>1'
        ELSE '=1'
    END AS Comparison
FROM purchase_order_details
GROUP BY date_received, posted_to_inventory;

-- 05 Выведите posted_to_inventory, date_received и вычисленный столбец.

SELECT date_received, posted_to_inventory,
COUNT(*) OVER (PARTITION BY date_received, posted_to_inventory) AS Num_Orders,
 CASE 
 WHEN (COUNT(*) OVER (PARTITION BY date_received, posted_to_inventory)
 ) > 1 
 THEN ">1"
 ELSE "=1" END AS Comparison
FROM purchase_order_details;