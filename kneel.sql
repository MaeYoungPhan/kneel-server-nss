CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` NUMERIC(5,2) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Pieces`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `type` NVARCHAR(160) NOT NULL
);

CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL,
    `style_id` INTEGER NOT NULL,
    `piece_id` INTEGER NOT NULL,
    `timestamp` FLOAT NOT NULL,
    FOREIGN KEY(`metal_id`) REFERENCES `Metals`(`id`),
    FOREIGN KEY(`size_id`) REFERENCES `Sizes`(`id`),
    FOREIGN KEY(`style_id`) REFERENCES `Styles`(`id`),
    FOREIGN KEY(`piece_id`) REFERENCES `Pieces`(`id`)
);

INSERT INTO 'METALS' VALUES (null, "Sterling Silver", 12.42 );
INSERT INTO 'METALS' VALUES ( null, "14K Gold", 736.4 );
INSERT INTO 'METALS' VALUES ( null, "24K Gold", 1258.9 );
INSERT INTO 'METALS' VALUES ( null, "Platinum", 795.45 );
INSERT INTO 'METALS' VALUES ( null, "Palladium", 1241.0 );

INSERT INTO 'SIZES' VALUES (null, 0.5, 405);
INSERT INTO 'SIZES' VALUES (null, 0.75, 782);
INSERT INTO 'SIZES' VALUES (null, 1, 1470);
INSERT INTO 'SIZES' VALUES (null, 1.5, 1997);
INSERT INTO 'SIZES' VALUES ( null, 2,  3638);

INSERT INTO 'STYLES' VALUES (null, "Classic", 500 );
INSERT INTO 'STYLES' VALUES (null, "Modern", 710 );
INSERT INTO 'STYLES' VALUES (null, "Vintage", 965 );

INSERT INTO 'PIECES' VALUES (null, "Ring");
INSERT INTO 'PIECES' VALUES (null, "Earrings");
INSERT INTO 'PIECES' VALUES (null, "Necklace");

INSERT INTO 'ORDERS' Values (null, 3, 2, 3, 1, 1614659931693);
INSERT INTO 'ORDERS' VALUES (null, 2, 1, 3, 2, 1614659931643);
INSERT INTO 'ORDERS' VALUES (null, 3, 1, 1, 2, 1614659931743);
INSERT INTO 'ORDERS' VALUES (null, 2, 2, 3, 3, 1614659939643);
INSERT INTO 'ORDERS' VALUES (null, 1, 3, 2, 1, 1614659931683);

SELECT * FROM metals

SELECT
    o.id,
    o.metal_id,
    o.size_id,
    o.style_id,
    o.piece_id,
    o.timestamp,
    m.metal metal_metal,
    m.price metal_price,
    s.carets size_carets,
    s.price size_price,
    t.style style_style,
    t.price style_price,
    p.type piece_type
FROM Orders o
JOIN Metals m
    ON m.id = o.metal_id
JOIN Sizes s
    ON s.id = o.size_id
JOIN Styles t
    ON t.id = o.style_id
JOIN Pieces p
    ON p.id = o.piece_id
