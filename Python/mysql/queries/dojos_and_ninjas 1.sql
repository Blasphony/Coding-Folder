INSERT INTO dojo (name)
VALUES ("Chicago"), ("Seattle"),("Online");

SET SQL_SAFE_UPDATES = 0;


SELECT * FROM ninjas;
INSERT INTO ninjas (first_name,last_name,age,dojo_id)
VALUES ("Adrien","Dion",39,1),("Anne","Jurack",34,1),("Ryan","Magley",30,1);

INSERT INTO ninjas (first_name,last_name,age,dojo_id)
VALUES ("Marisa","Goode",37,2),("Todd","Enders",36,2),("Sadie","Flick",29,2);

INSERT INTO ninjas (first_name,last_name,age,dojo_id)
VALUES ("Mr. Nibbles","Pancakes",54,3),("Benny Bob","McBob",65,3),("Mitch","Golden",26,3);

SELECT * FROM dojo
LEFT JOIN ninjas ON dojo.id = ninjas.dojo_id
WHERE dojo.id = 1;

SELECT * FROM dojo
LEFT JOIN ninjas ON dojo.id = ninjas.dojo_id
	WHERE dojo.id IN (SELECT id FROM dojo ORDER BY id DESC) LIMIT 2;

SELECT id FROM dojo ORDER BY id DESC LIMIT 2;

SELECT * FROM dojo
WHERE dojo.id = (SELECT dojo_id FROM ninjas ORDER BY dojo_id DESC LIMIT 1);