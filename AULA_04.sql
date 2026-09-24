/* SELECT * FROM cadastro_produtos;
SELECT Produto, Marca FROM cadastro_produtos


SELECT * FROM cadastro_produtos 
WHERE Marca = "Logitech";


SELECT * FROM cadastro_produtos 
WHERE `Preço Unitario` >20 
ORDER BY `Preço Unitario`; 


SELECT * FROM cadastro_produtos 
WHERE `Tipo do Produto` = "Mouse" 
AND (marca = "logitech" OR marca= "multilaser");
*/

SELECT* FROM cadastro_produtos 
WHERE marca = "Hashtag"
AND `Preço Unitario` >=20
BETWEEN 20 AND 50; 








