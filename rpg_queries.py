import sqlite3
-- Total characters
SELECT COUNT(character_id)
FROM charactercreator_character;

-- Characters by subclass
SELECT "Class", COUNT("Class") FROM (

	SELECT character_id,
		(CASE
			WHEN character_id IN (SELECT mage_ptr_id FROM charactercreator_necromancer) THEN "Necromancer"
			WHEN character_id IN (SELECT character_ptr_id FROM charactercreator_fighter) THEN "Fighter"
			WHEN character_id IN (SELECT character_ptr_id FROM charactercreator_thief) THEN "Thief"
			WHEN character_id IN (SELECT character_ptr_id FROM charactercreator_cleric) THEN "Cleric"
			WHEN character_id IN (SELECT character_ptr_id FROM charactercreator_mage) THEN "Mage"
		END) AS "Class"
	FROM charactercreator_character)
GROUP BY "Class";

-- Total items
SELECT COUNT(item_id)
FROM armory_item;

-- How many items are weapons? How many aren't?
SELECT "Type", COUNT("Type") FROM (

	SELECT (CASE
				WHEN item_id IN (SELECT item_ptr_id FROM armory_weapon) THEN "Is Weapon"
				ELSE "Is Not Weapon"
			END) AS "Type"
	FROM armory_item)
GROUP BY "Type"

-- Average items per character
SELECT AVG("Num of Items") FROM (

	SELECT character_id, COUNT(item_id) AS "Num of Items"
	FROM charactercreator_character_inventory
	GROUP BY character_id)

  -- Average weapons per character
SELECT AVG("Num of Weapons") FROM (

	SELECT character_id, COUNT(item_id) AS "Num of Weapons"
	FROM charactercreator_character_inventory
		JOIN armory_weapon
		WHERE item_id = item_ptr_id
	GROUP BY character_id)
