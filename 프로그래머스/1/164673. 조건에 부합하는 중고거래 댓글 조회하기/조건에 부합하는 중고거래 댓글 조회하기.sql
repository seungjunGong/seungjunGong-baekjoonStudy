SELECT B.TITLE, B.BOARD_ID, R.REPLY_ID, R.WRITER_ID,
    R.CONTENTS, DATE_FORMAT(R.CREATED_DATE, "%Y-%m-%d") AS CREATED_DATE
FROM USED_GOODS_BOARD AS B, USED_GOODS_REPLY AS R
WHERE B.BOARD_ID=R.BOARD_ID
AND DATE_FORMAT(B.CREATED_DATE, "%Y-%m")="2022-10"
ORDER BY R.CREATED_DATE, B.TITLE;