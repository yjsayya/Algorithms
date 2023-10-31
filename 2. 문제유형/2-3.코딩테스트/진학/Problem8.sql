SELECT
    MUTUAL_ID as ID
FROM
    (
        SELECT
            ID2 as MUTUAL_ID
        FROM
            FRIENDS
        WHERE ID1 in
        (
            SELECT ID2
            FROM FRIENDS
            WHERE ID1 = "naneekgunpowder1886"
                UNION ALL
            SELECT ID1
            FROM FRIENDS
            WHERE ID2 = "naneekgunpowder1886"
        ) AND ID2 <> "naneekgunpowder1886"

        UNION ALL

        SELECT
            ID1 as MUTUAL_ID
        FROM
            FRIENDS
        WHERE ID2 in (
            SELECT ID2
            FROM FRIENDS
            WHERE ID1 = "naneekgunpowder1886"
                UNION ALL
            SELECT ID1
            FROM FRIENDS
            WHERE ID2 = "naneekgunpowder1886"
        ) AND ID1 <> "naneekgunpowder1886"
    ) as T
GROUP BY
    ID
ORDER BY
    count(*) DESC, ID
LIMIT 1;





-- 1. 전체 테이블
-- select * from FRIENDS

-- select ID1 from FRIENDS where id2 = "langworthychance1887"
-- union all
-- select ID2 from FRIENDS where id1 = "langworthychance1887"

-- 2. nanee의 친구 구하기
-- SELECT ID2
-- FROM FRIENDS
-- WHERE ID1 = "naneekgunpowder1886"
--     UNION ALL
-- SELECT ID1
-- FROM FRIENDS
-- WHERE ID2 = "naneekgunpowder1886"

-- 3. Mutual_Friend(친구의 친구 찾기)
-- SELECT
--     ID2 as MUTUAL_ID
-- FROM
--     FRIENDS
-- WHERE ID1 in
--     (
--         SELECT ID2
--         FROM FRIENDS
--         WHERE ID1 = "naneekgunpowder1886"
--             UNION
--         SELECT ID1
--         FROM FRIENDS
--         WHERE ID2 = "naneekgunpowder1886"
--     ) AND ID2 <> "naneekgunpowder1886"

-- UNION ALL

-- SELECT
--     ID1 as MUTUAL_ID
-- FROM
--     FRIENDS
-- WHERE ID2 in
--     (
--         SELECT ID2
--         FROM FRIENDS
--         WHERE ID1 = "naneekgunpowder1886"
--             UNION
--         SELECT ID1
--         FROM FRIENDS
--         WHERE ID2 = "naneekgunpowder1886"
--     ) AND ID1 <> "naneekgunpowder1886"