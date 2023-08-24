-- K - Пользователи и заказы

select DISTINCT u.id, name 
FROM users as u
JOIN orders as o
ON u.id = o.user_id
ORDER BY name, id;