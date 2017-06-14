CREATE VIEW error_count AS 
	SELECT time, count(status) AS errors
	FROM log 
	WHERE status LIKE '%404%' 
	GROUP BY time
	ORDER BY time DESC;