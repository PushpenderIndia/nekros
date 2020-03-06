
CREATE TABLE `nekros_keys` (
  `software_key` char(32) NOT NULL,
  `decrypt_key` char(32) NOT NULL,
  `date` datetime NOT NULL,
  `payment` boolean NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


