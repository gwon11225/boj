-- 코드를 입력하세요
SELECT BOARD_ID, WRITER_ID, TITLE, PRICE, IF(`STATUS` = 'DONE', '거래완료', IF(`STATUS` = 'SALE', '판매중', '예약중')) AS 'STATUS' FROM USED_GOODS_BOARD WHERE CREATED_DATE = "2022-10-05" ORDER BY BOARD_ID DESC;