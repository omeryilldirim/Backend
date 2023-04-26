--This is a single comment line

/*
Multiline 
comment
*/

-- SELECT 1 as one   ** TEK BLOK İŞLEMLER İÇİ N NOKTALI VİRGÜL ZORUNLU DEĞİLDİR.

-- SELECT 1 as One; /* this is a comment */ 

-- SELECT 2 AS TWO -- NOT case sensitive

--PİYASA STANDARTLARI
--* SQL temel komutları büyük harfle diğer koumtlar küçük harfle yazılır.  SELECT * FROM Album WHERE AlbumID=1
--* sring verilerde tek veya çift tırnak kullanılabilir ama standart olan tek tırnaktır.hatta bazı veritabanları çift tırnak desteklemez.  SELECT 'string' as text
--* Her bir temel komut yeni bir satıra yazılır.
/*
SELECT * 
FROM Album 
WHERE AlbumID=1
*/

--- --- --- SQL --- --- ---

-- SELECT  --> seç getir
-- FROM --> nerden

--SELECT * FROM Album;  -- tüm sütunlar
--SELECT AlbumId, Title FROM Album; -- istenilen sütunları getirir. Tavsiye edilen yöntem ayrı ayrı yazmaktır, yıldız kullanmak değil.

-- ** AS --> Tablo veya sütunları adlandırmak için kullanılır.

--SELECT 'data' as başlık
-- select 1+2  as result; -- mathematical expression

--SELECT AlbumId AS no, Title AS baslik FROM Album;
--SELECT AlbumId+3 AS no, Title AS baslik FROM Album;
-- SELECT Album.AlbumId, Album.Title FROM Album;
-- SELECT a.AlbumId, a.Title FROM Album AS a; -- Tablo isimlendirme
-- SELECT a.AlbumId AS Numara, a.Title AS Baslik FROM Album AS a;
-- SELECT a.AlbumId Numara, a.Title Baslik FROM Album a; -- AS kullanmadan da isimlendirme yapabiliriz.

-- * DISTINCT - Tekrar edilen kayıtarın tekrar edilmesini engeller (tek kayıt olarak getirir)
-- SELECT DISTINCT City FROM Customer;
-- SELECT DISTINCT City, Country FROM Customer; -- Bütün sutunlardaki ortak olanları 1 kere getirir.

-- * WHERE - Filtreleme
-- SELECT * FROM Customer WHERE Country = 'USA' -- Eşit olanları getir.
-- SELECT * FROM Customer WHERE Country != 'USA' -- Eşit olMAanları getir.
-- SELECT * FROM Customer WHERE Country <> 'USA' -- Eşit olMAanları getir.
-- SELECT * FROM Customer WHERE CustomerId > 20 -- Büyük olanları getir.
-- SELECT * FROM Customer WHERE CustomerId >= 20 -- BüyükEşit olanları getir.
-- SELECT * FROM Customer WHERE CustomerId < 20 -- Küçük olanları getir.
-- SELECT * FROM Customer WHERE CustomerId <= 20 -- KüçükEşit olanları getir.
-- SELECT * FROM Customer WHERE CustomerId BETWEEN 10 AND 20 -- 10 ile 20 arasında olanları getir. (her ikiside dahil)

-- * WHERE - AND OR NOT
-- * SELECT * FROM table WHERE True OR NOT True
-- SELECT * FROM Customer WHERE NOT Country = 'USA'
-- SELECT * FROM Customer WHERE Country = 'USA' AND Company  NOT NULL
-- SELECT * FROM Customer  WHERE Country = 'USA' OR Country = 'Brazil' OR Country='Denmark';
-- SELECT * FROM Customer  WHERE (Country = 'USA' OR Country = 'Brazil' OR Country='Denmark') AND CustomerId > 25;
-- SELECT * FROM Customer  WHERE (Country = 'USA' OR Country = 'Brazil' OR Country='Denmark') AND (CustomerId BETWEEN 25 AND 27)

-- * WHERE - IN - NOT IIN
-- SELECT * FROM Customer  WHERE Country = 'USA' OR Country = 'Brazil' OR Country='Denmark';
-- SELECT * FROM Customer  WHERE Country IN ('USA', 'Brazil', 'Denmark');
-- SELECT * FROM Customer  WHERE Country NOT IN ('USA', 'Brazil', 'Denmark');
-- SELECT * FROM Customer  WHERE CustomerID IN (2,3,4,10,11);

-- * WHERE - LIKE ( _ = SingleChar, % = JokerChar)
-- SELECT * FROM Customer WHERE Country LIKE 'USA' -- USA olanlar.
-- SELECT * FROM Customer WHERE Address LIKE '627 Broadway' -- 627 Broadway olanlar.
-- SELECT * FROM Customer WHERE Address LIKE '1498%'  -- 1498 ile başlayan kayıtlar.
-- SELECT * FROM Customer WHERE Address LIKE '%langer'  -- langer ile biten kayıtlar.
-- SELECT * FROM Customer WHERE Address LIKE '%rue%'  -- içinde "rue" geçen kayıtlar 

-- LIKE en yavaş filtreleme yöntemidir. LIKE metodunda da % ile arama yapmak * ile arama yapmaktan daha yavaştır.

--SELECT * FROM Customer WHERE Phone LIKE '_55 %' ;  -- 2. ve 3. karakteri 55 olan kayıtlar
-- SELECT * FROM Customer WHERE Phone LIKE '+__ 030%' ;

-- * ORDER BY ( ASC / DESC ) 

--SELECT * FROM Customer ORDER BY Country; --default is ASC
--SELECT * FROM Customer ORDER BY Country DESC;
--SELECT * FROM Customer ORDER BY Country, City, LastName;  -- Sırasıyla ülke, şehir ve soyisim sıralar
 
--SELECT * FROM Customer WHERE Country In ('USA', 'Brazil') AND CustomerId > 12 AND Company NOT NULL ORDER BY Company
/* -- Piyasada standartı:
SELECT * 
FROM Customer 
WHERE Country IN ('USA', 'Brazil') 
	AND CustomerId > 12
	AND Company NOT NULL 
ORDER BY Company ASC 
*/

--* LIMIT

-- SELECT * FROM Customer LIMIT 10;  -- default başlangıç 0
-- SELECT * FROM Customer LIMIT 0, 10;  -- LIMIT başlangıç kaydı, kayıt adedi
-- SELECT * FROM Customer LIMIT 5, 15;  -- ilk 5 kaydı atlar
-- SELECT * FROM Customer ORDER BY LastName ASC, FirstName DESC LIMIT 0, 5; -- Sıralamaya göre ilk 5 kayıt.
-- SELECT * FROM Customer ORDER BY LastName ASC, FirstName DESC LIMIT 5, 5; -- Sıralamaya göre ikinci 5 kayıt

--* SUBQUERY (SELECT IN SELECT)

-- SELECT * FROM Album WHERE ArtistId = (SELECT ArtistId FROM Artist WHERE Name = 'Led Zeppeli')
-- SELECT AlbumId, Title, (SELECT Name FROM Artist WHERE ArtistId = 22) AS Artist FROM Album;
/*
-- SubSELECT sorgusunu tablo gibi kullanmak:
SELECT FirstName, LastName
FROM (
	SELECT * FROM Customer WHERE Country = 'USA' AND CustomerId > 22
) WHERE FirstName LIKE '%a%'
*/

-- -- -- -- -- -- -- -- -- JOINS -- -- -- -- -- -- -- -- --

-- Birden fazla tablodaki kayıtları tek bir tabloda getirmek için kullanıyor.

-- * INNER JOIN
-- ALternatif Yazım: JOIN -- default JOIN yöntemi INNER JOIN'dir.

/*
SELECT  *
FROM Artist AS art
JOIN Album AS alb on alb.ArtistId=art.ArtistId
ORDER BY ArtistId ASC, AlbumId ASC
*/

/*
SELECT c.FirstName, c.LastName, c.Country,i.InvoiceId, i.InvoiceDate, i.Total
FROM Customer AS c
INNER JOIN Invoice AS i ON i.CustomerId = c.CustomerId
ORDER BY c.CustomerId
*/

/*
SELECT t.Name AS Song, a.Title Album, m.Name File, g.Name Category
FROM Track t
INNER JOIN Album a ON a.AlbumId = t.AlbumId
INNER JOIN MediaType m ON t.MediaTypeId = m.MediaTypeId
INNER JOIN Genre g ON g.GenreId = t.GenreId
*/

-- * LEFT JOIN -- Karşı tablodaki BÜTÜN kayıtlar ve LEFT JOIN'deki KESİŞEN kayıtları getir.
/*
SELECT *
FROM Artist AS art
LEFT JOIN Album AS alb ON alb.ArtistId=art.ArtistId
ORDER BY ArtistId ASC, AlbumId ASC
*/

-- * RIGHT JOIN -- Karşı tablodaki KESİŞEN kayıtlar ve RIGHT tablodaki BÜTÜN kayıtlar.
/*
SELECT *
FROM Artist AS art
RIGHT JOIN Album AS alb ON alb.ArtistId=art.ArtistId
ORDER BY ArtistId ASC, AlbumId ASC
*/

-- * FULL  OUTER JOIN -- Her iki tablonun BÜTÜN kayıtlarını göster, Eşleşenleri yanyana göster.
/*
SELECT *
FROM Artist AS art
FULL OUTER JOIN Album AS alb ON alb.ArtistId=art.ArtistId
ORDER BY ArtistId ASC, AlbumId ASC
*/

-- * CROSS JOIN -- Her iki tablonun BÜTÜN kayıtlarını göster, İlişki gözetme.
/*
SELECT *
FROM Artist AS art, Album AS alb
ORDER BY ArtistId ASC, AlbumId ASC
*/

-- * JOIN ÖRNEKLER
/*
-- Hangi sanatçı hangi albümleri çıkarmıştır. Bir albüme sahip olmayan sanatçıları gösterme. Sadece albüme sahip olan sanatçıları göster.
SELECT t1.ArtistId, t1.Name AS sanatci, t2.Title AS album
FROM Artist AS t1
INNER JOIN Album AS t2 ON t1.ArtistId=t2.ArtistId
-- WHERE t1.Name = 'Led Zeppeli'
ORDER BY t1.ArtistId
*/
/*
-- Bütün sanatçıları göster. Hangi sanatçı hangi albüme sahip onu da göster. Ama albüm sahibi olmayan kayıtlara NULL yaz.
SELECT t1.ArtistId, t1.Name AS sanatci, t2.Title AS album
FROM Artist AS t1
LEFT JOIN Album AS t2 ON t2.ArtistId=t1.ArtistId
ORDER BY t1.ArtistId
*/

-- -- -- -- -- -- -- --  FUNCTIONS -- -- -- -- -- -- -- -- -- -- -- -- 

--* COUNT -- Kayıt Sayısı
-- SELECT COUNT(*) AS kayitSayisi FROM Customer -- * kullanmak efektif değil. 
-- SELECT COUNT(CustomerId) AS kayitSayisi FROM Customer; -- Herhangi bir sutun ismi kullanmalıyız (PRIMARY)

-- * SUM -- Toplam
-- SELECT SUM(Total) AS toplam FROM Invoice; -- Toplam fatura tutarı
-- SELECT SUM(Total) AS toplam, BillingCountry FROM Invoice WHERE BillingCountry='USA'; -- Amerikaya kesilen fatura toplamı.

-- * AVG - Ortalama alır.
-- SELECT AVG(Total) AS ortalama FROM Invoice;

-- * ROUND -- Yuvarlama
-- SELECT ROUND(AVG(Total)) AS ortalama FROM Invoice;
-- SELECT ROUND(AVG(Total), 2) AS ortalama FROM Invoice;

-- * MIN -- En küçük değer.
-- SELECT MIN(Total) AS ortalama FROM Invoice;

-- * MAX -- En büyük değer.
-- SELECT MAX(Total) AS ortalama FROM Invoice;

-- * LENGTH -- Karakter Sayısı -- Satır satır.
-- SELECT LENGTH(BillingAddress) AS ortalama FROM Invoice;

-- * GROUP BY -- İşlemleri gruplayarak yap.
-- SELECT BillingCountry, SUM(Total) AS toplam FROM Invoice GROUP BY BillingCountry; -- Ülkeye göre toplam tutarları ver.
-- SELECT BillingCountry, COUNT(InvoiceId) AS faturaSayisi FROM Invoice GROUP BY BillingCountry;  -- hangi ülkeye kaç adet fatura göster.
-- SELECT BillingCountry, AVG(Total) AS ortalama FROM Invoice GROUP BY BillingCountry;  -- Ülkeye göre ortalama fatura tutarı.
-- SELECT BillingCountry, ROUND(AVG(Total), 2) AS ortalama FROM Invoice GROUP BY BillingCountry;  -- Ülkeye göre ortalama fatura tutarı. -- yuvarlanmış
-- SELECT BillingCountry, MIN(Total) AS minimum FROM Invoice GROUP BY BillingCountry;  -- Ülkeye göre minimum fatura tutarı.
-- SELECT BillingCountry, MAX(Total) AS maximum FROM Invoice GROUP BY BillingCountry;  -- Ülkeye göre maximum fatura tutarı.