USE northwind;
SELECT * FROM order_details;

-- 01. Для каждого product_id выведите inventory_id а также предыдущий и последующей inventory_id по убыванию quantity.

SELECT product_id, quantity, inventory_id,
	LAG(inventory_id) OVER (PARTITION BY product_id ORDER BY quantity DESC) AS lag_inv_id,
    LEAD(inventory_id) OVER (PARTITION BY product_id ORDER BY quantity DESC) AS lead_inv_id
FROM order_details;

/* 02. Выведите максимальный и минимальный unit_price для каждого order_id с помощью функции FIRST_VALUE().
	   Выведите order_id и полученные значения. */
SELECT order_id, unit_price,
		FIRST_VALUE(unit_price) OVER(PARTITION BY order_id ORDER BY unit_price ASC) AS min_price,
        FIRST_VALUE(unit_price) OVER(PARTITION BY order_id ORDER BY unit_price DESC) AS max_price
FROM order_details;
/* 03. Выведите order_id и столбец с разницей между unit_price для каждого заказа
 и минимальным unit_price в рамках одного заказа.
! Задачу решить двумя способами - с помощью FIRST_VALUE() и MIN().*/

-- FIRST_VALUE
SELECT order_id, unit_price
, unit_price - FIRST_VALUE(unit_price)
 OVER
 (PARTITION BY order_id 
 ORDER BY unit_price) AS diff_price, FIRST_VALUE(unit_price)
 OVER
 (PARTITION BY order_id 
 ORDER BY unit_price) AS min_price
FROM order_details;

-- MIN

SELECT order_id, unit_price
, unit_price - min(unit_price)
 OVER
 (PARTITION BY order_id) AS diff_price
 , min(unit_price)
 OVER
 (PARTITION BY order_id) AS min_price
FROM order_details;

-- 04. Присвойте ранг каждой строке, используя RANK() по убыванию quantity.

SELECT quantity, RANK() OVER (ORDER BY quantity DESC) AS rank_quant
FROM order_details;

-- 05. Из предыдущего запроса выберите только строки с рангом до 10 включительно.

	WITH ranked_quant AS (SELECT quantity, RANK() OVER (ORDER BY quantity DESC) AS rank_quant
FROM order_details)
	SELECT quantity, rank_quant
FROM ranked_quant
WHERE rank_quant <= 10;
