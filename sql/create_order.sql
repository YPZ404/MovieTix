CREATE TABLE `Order` (
  `id` int NOT NULL AUTO_INCREMENT,
  `order_id` int NOT NULL,
  `customer_id` int NOT NULL,
  `room_id` int NOT NULL,
  `seat_id` int NOT NULL,
  `release_id` int NOT NULL,
  `movie_id` int NOT NULL,
  `movie_name` varchar(40) NOT NULL,
  `price` float NOT NULL,
  `is_canceled` int NOT NULL default 0,
  `release_time` timestamp NOT NULL,
  `create_time` timestamp NOT NULL,
  `update_time` timestamp NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `order_id_UNIQUE` (`order_id`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8