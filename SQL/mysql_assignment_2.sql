CREATE TABLE `Post` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`userId` INT NOT NULL,
	`content` TEXT,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_on` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Like` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`userId` INT NOT NULL,
	`postId` INT NOT NULL,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Comment` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`userId` INT NOT NULL,
	`postId` INT NOT NULL,
	`content` TEXT NOT NULL,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Image` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`postId` INT NOT NULL,
	`src` varchar(255) NOT NULL UNIQUE,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
);

CREATE TABLE `User` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(255) NOT NULL UNIQUE,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
);

ALTER TABLE `Post` ADD CONSTRAINT `Post_fk0` FOREIGN KEY (`userId`) REFERENCES `User`(`id`);

ALTER TABLE `Like` ADD CONSTRAINT `Like_fk0` FOREIGN KEY (`userId`) REFERENCES `User`(`id`);

ALTER TABLE `Like` ADD CONSTRAINT `Like_fk1` FOREIGN KEY (`postId`) REFERENCES `Post`(`id`);

ALTER TABLE `Comment` ADD CONSTRAINT `Comment_fk0` FOREIGN KEY (`userId`) REFERENCES `User`(`id`);

ALTER TABLE `Comment` ADD CONSTRAINT `Comment_fk1` FOREIGN KEY (`postId`) REFERENCES `Post`(`id`);

ALTER TABLE `Image` ADD CONSTRAINT `Image_fk0` FOREIGN KEY (`postId`) REFERENCES `Post`(`id`);


INSERT INTO `User`(`name`) 
VALUES ('Tyler'),('Madison'),('Colin'),('Sean');

SELECT * FROM `User`;

INSERT INTO `Post`(`userId`,`content`) 
VALUES 
(1,'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'),
(3,'et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut'),
(4,'consectetur animi nesciunt iure dolore\nenim quia ad\nveniam autem ut quam aut nobis\net est aut quod aut provident voluptas autem voluptas'),
(1,'quo et expedita modi cum officia vel magni\ndoloribus qui repudiandae\nvero nisi sit\nquos veniam quod sed accusamus veritatis error'),
(2,'eveniet quo quis\nlaborum totam consequatur non dolor\nut et est repudiandae\nest voluptatem vel debitis et magnam'),
(3,'eos qui et ipsum ipsam suscipit aut\nsed omnis non odio\nexpedita earum mollitia molestiae aut atque rem suscipit\nnam impedit esse');

SELECT * FROM `Post`;

INSERT INTO `Image`(`postId`,`src`) 
VALUES (4,'https://freerangestock.com/photos/113325/connected-smart-city.html'),
(4,'https://freerangestock.com/photos/88174/rooftopper-looking-down.html'),
(5,'https://freerangestock.com/photos/39309/money-and-financial-data--finance-concept.html'),
(2,'https://unsplash.com/photos/1vJXDrv_498');

SELECT * FROM `Image`;

INSERT INTO `Like`(`userId`,`postId`) 
VALUES (2,4),
(4,4),
(1,2),
(3,6);

 SELECT * FROM `Like`; 
 
INSERT INTO `Comment`(`userId`,`postId`,`content`) 
VALUES (1,4,'repudiandae repellat quia\nsequi est dolore explicabo nihil et\net sit et\net praesentium iste atque asperiores tenetur'),
(2,3,'expedita maiores dignissimos facilis\nipsum est rem est fugit velit sequi\neum odio dolores dolor totam\noccaecati ratione eius rem velit'),
(4,5,'ut voluptatem corrupti velit\nad voluptatem maiores\net nisi velit vero accusamus maiores\nvoluptates quia aliquid ullam eaque'),
(3,3,'harum non quasi et ratione\ntempore iure ex voluptates in ratione\nharum architecto fugit inventore cupiditate\nvoluptates magni quo et');

SELECT * FROM `Comment`;
