USE dad8hw_db;

SELECT 
    b.title,
    b.genre,
    b.publish_year,
    a.author_name,
    a.country
FROM books b
JOIN authors a
    ON b.author_id = a.author_id
WHERE a.country = 'United Kingdom';