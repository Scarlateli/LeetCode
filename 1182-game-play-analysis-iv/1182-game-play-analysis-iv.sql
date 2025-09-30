-- Solução para Oracle: Calcular a fração de jogadores que voltaram no dia seguinte

SELECT 
    ROUND(
        SUM(CASE WHEN a2.event_date IS NOT NULL THEN 1 ELSE 0 END) * 1.0 / COUNT(*), 
        2
    ) AS fraction
FROM (
    SELECT 
        player_id,
        MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
) a1
LEFT JOIN Activity a2
    ON a1.player_id = a2.player_id
    AND a2.event_date = a1.first_login + 1;


-- Explicação:
-- 
-- 1. Subconsulta a1: pega o primeiro login de cada jogador
--
-- 2. LEFT JOIN: busca se o jogador voltou no dia seguinte (first_login + 1)
--
-- 3. SUM(CASE...): conta quantos jogadores voltaram (quando a2.event_date não é NULL)
--
-- 4. COUNT(*): conta total de jogadores
--
-- 5. * 1.0: força divisão decimal
--
-- 6. ROUND(..., 2): arredonda para 2 casas decimais