-- This query shows every individual lead in your database
SELECT title, source, status, scraped_at
FROM leads
ORDER BY scraped_at DESC;