SELECT author_id AS id
FROM Views v1
WHERE EXISTS (
    SELECT 1 FROM Views v2 
    WHERE v2.author_id = v1.author_id 
    AND v2.author_id = v2.viewer_id
)
GROUP BY author_id
ORDER BY id ASC;