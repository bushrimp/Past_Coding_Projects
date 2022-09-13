-- * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
-- Name: 	BI_IS370_FP_DDL_DML
-- Type: 	SQL
-- Author: 	Bushra Ibrahim
-- Date: 	2022-4-20
-- Purpose:	The purpose of this SQL script is to build the International 
-- 			Song App Database, based on the BI_IS370_FP_UML_Drawing, and 
--          fill it up with data (min 10 entries per table).
-- 
-- Changes: 5/3/22 - by: Bushra Ibrahim
--          I made DOB a "date" data type instead of "datetime."
--          I made DOB nullable because some obscure artists' birthdays were not available.
--          I made the duration a "time" data type instead of a numeric so minutes and seconds are obvious.
--          I made tbe ID data types int instead of numeric so that auto_increment will work.
--          	*note: auto_increment can only be mentioned for the primary key of each table
--              *also, this means removing id#s from inserts, and adding table names
-- * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

DROP DATABASE IF EXISTS `International_Song_App`;
CREATE DATABASE `International_Song_App`;
USE International_Song_App;

CREATE TABLE Languages (
LANG_ID int NOT NULL AUTO_INCREMENT,
LANG_NAME varchar(50) NOT NULL,
PRIMARY KEY (LANG_ID)
)
ENGINE = INNODB;

INSERT INTO Languages (LANG_NAME) VALUES('Tamil');
INSERT INTO Languages (LANG_NAME)VALUES('Arabic (Egyptian)');
INSERT INTO Languages (LANG_NAME)VALUES('Japanese');
INSERT INTO Languages (LANG_NAME)VALUES('Korean');
INSERT INTO Languages (LANG_NAME)VALUES('English');
INSERT INTO Languages (LANG_NAME) VALUES('Spanish');
INSERT INTO Languages (LANG_NAME)VALUES('Hindi');
INSERT INTO Languages (LANG_NAME)VALUES('Thai');
INSERT INTO Languages (LANG_NAME)VALUES('Kinyarwanda');
INSERT INTO Languages (LANG_NAME)VALUES('French');


CREATE TABLE Genres (
GENRE_ID int NOT NULL AUTO_INCREMENT,
GENRE_NAME enum ('K-Pop','Carnatic','Hip Hop/Rap','Indian Pop','Spiritual','Rock',
				'J-Pop','Rhythmic Soul','Street','Classical','Trap/Pop','Latin Urbano') NOT NULL,
PRIMARY KEY (GENRE_ID)
)
ENGINE = INNODB;

INSERT INTO Genres (GENRE_NAME) VALUES('K-Pop');
INSERT INTO Genres (GENRE_NAME) VALUES('Carnatic');
INSERT INTO Genres (GENRE_NAME) VALUES('Hip Hop/Rap');
INSERT INTO Genres (GENRE_NAME) VALUES('Indian Pop');
INSERT INTO Genres (GENRE_NAME) VALUES('Spiritual');
INSERT INTO Genres (GENRE_NAME) VALUES('Rock');
INSERT INTO Genres (GENRE_NAME) VALUES('J-Pop');
INSERT INTO Genres (GENRE_NAME) VALUES('Rhythmic Soul');
INSERT INTO Genres (GENRE_NAME) VALUES('Street');
INSERT INTO Genres (GENRE_NAME) VALUES('Classical');
INSERT INTO Genres (GENRE_NAME) VALUES('Trap/Pop');
INSERT INTO Genres (GENRE_NAME) VALUES('Latin Urbano');


CREATE TABLE Countries (
COUN_ID int NOT NULL AUTO_INCREMENT,
COUN_NAME varchar(50) NOT NULL,
LANG_ID int NOT NULL,
PRIMARY KEY (COUN_ID),
FOREIGN KEY (LANG_ID) REFERENCES Languages(LANG_ID)
)
ENGINE = INNODB;

INSERT INTO Countries (COUN_NAME, LANG_ID) VALUES('India','7');
INSERT INTO Countries (COUN_NAME, LANG_ID) VALUES('Egypt','2');
INSERT INTO Countries (COUN_NAME, LANG_ID) VALUES('South Korea','4');
INSERT INTO Countries (COUN_NAME, LANG_ID) VALUES('Japan','3');
INSERT INTO Countries (COUN_NAME, LANG_ID) VALUES('Thailand','8');
INSERT INTO Countries (COUN_NAME, LANG_ID) VALUES('France','10');
INSERT INTO Countries (COUN_NAME, LANG_ID) VALUES('United States','5');
INSERT INTO Countries (COUN_NAME, LANG_ID) VALUES('Rwanda','9');
INSERT INTO Countries (COUN_NAME, LANG_ID) VALUES('Cuba','6');
INSERT INTO Countries (COUN_NAME, LANG_ID) VALUES('Colombia','6');


CREATE TABLE Artists (
ARTIST_ID int NOT NULL AUTO_INCREMENT,
ARTIST_NAME varchar(50) NOT NULL,
ARTIST_DOB date,
ARTIST_EB varchar(75),
COUN_ID int NOT NULL,
PRIMARY KEY (ARTIST_ID),
FOREIGN KEY (COUN_ID) REFERENCES COUNTRIES(COUN_ID)
)
ENGINE = INNODB;

INSERT INTO Artists (ARTIST_NAME, ARTIST_DOB, ARTIST_EB, COUN_ID) VALUES('A.R. Rahman','1967-01-06','South Indian (Tamil)','1');
INSERT INTO Artists (ARTIST_NAME, ARTIST_DOB, ARTIST_EB, COUN_ID) VALUES('J Balvin','1985-05-07','Colombian','10');
INSERT INTO Artists (ARTIST_NAME, ARTIST_DOB, ARTIST_EB, COUN_ID) VALUES('Bad Bunny','1994-03-10','Puerto Rican','7');
INSERT INTO Artists (ARTIST_NAME, ARTIST_DOB, ARTIST_EB, COUN_ID) VALUES('Sema Sole', NULL,'Rwandan','8');
INSERT INTO Artists (ARTIST_NAME, ARTIST_DOB, ARTIST_EB, COUN_ID) VALUES('Jungkook','1997-09-01','South Korean','3');
INSERT INTO Artists (ARTIST_NAME, ARTIST_DOB, ARTIST_EB, COUN_ID) VALUES('Cochise','1998-05-29','Jamaican','7');
INSERT INTO Artists (ARTIST_NAME, ARTIST_DOB, ARTIST_EB, COUN_ID) VALUES('BewhY','1993-06-15','South Korean','3');
INSERT INTO Artists (ARTIST_NAME, ARTIST_DOB, ARTIST_EB, COUN_ID) VALUES('Matthieu Chedid','1971-12-21','French','6');
INSERT INTO Artists (ARTIST_NAME, ARTIST_DOB, ARTIST_EB, COUN_ID) VALUES('Santhosh Narayanan','1983-05-15','South Indian (Tamil)','1');
INSERT INTO Artists (ARTIST_NAME, ARTIST_DOB, ARTIST_EB, COUN_ID) VALUES('Doja Cat','1995-10-21','South African & Jewish American','7');
INSERT INTO Artists (ARTIST_NAME, ARTIST_DOB, ARTIST_EB, COUN_ID) VALUES('Milli','2002-11-13','Thai','5');
INSERT INTO Artists (ARTIST_NAME, ARTIST_DOB, ARTIST_EB, COUN_ID) VALUES('Travis Scott','1991-04-30','African American','7');
INSERT INTO Artists (ARTIST_NAME, ARTIST_DOB, ARTIST_EB, COUN_ID) VALUES('Ahmed Saad','1981-08-20','Egyptian','2');

CREATE TABLE Albums (
ALBUM_ID int NOT NULL AUTO_INCREMENT,
ALBUM_NAME varchar(50) NOT NULL,
ARTIST_ID int NOT NULL,
PRIMARY KEY (ALBUM_ID),
FOREIGN KEY (ARTIST_ID) REFERENCES Artists(ARTIST_ID)
)
ENGINE = INNODB;

INSERT INTO Albums (ALBUM_NAME, ARTIST_ID) VALUES('Delhi-6','1');
INSERT INTO Albums (ALBUM_NAME, ARTIST_ID) VALUES('Planet Her','10');
INSERT INTO Albums (ALBUM_NAME, ARTIST_ID) VALUES('Benbow Crescent','6');
INSERT INTO Albums (ALBUM_NAME, ARTIST_ID) VALUES('Karnan','9');
INSERT INTO Albums (ALBUM_NAME, ARTIST_ID) VALUES('Madras','9');
INSERT INTO Albums (ALBUM_NAME, ARTIST_ID) VALUES('Jodhaa Akbar','1');
INSERT INTO Albums (ALBUM_NAME, ARTIST_ID) VALUES('Astroworld','12');
INSERT INTO Albums (ALBUM_NAME, ARTIST_ID) VALUES('Las que no iban a salir','3');
INSERT INTO Albums (ALBUM_NAME, ARTIST_ID) VALUES('The Movie Star','7');
INSERT INTO Albums (ALBUM_NAME, ARTIST_ID) VALUES('Bururu EP','4');

CREATE TABLE Songs (
SONG_ID int NOT NULL AUTO_INCREMENT,
SONG_NAME varchar(50) NOT NULL,
ARTIST_ID int NOT NULL,
ALBUM_ID int,
SONG_DUR time NOT NULL,
LANG_ID int NOT NULL,
GENRE_ID int NOT NULL,
SONG_PR tinyint,
PRIMARY KEY (SONG_ID),
FOREIGN KEY (ARTIST_ID) REFERENCES Artists(ARTIST_ID),
FOREIGN KEY (ALBUM_ID) REFERENCES Albums(ALBUM_ID),
FOREIGN KEY (LANG_ID) REFERENCES Languages(LANG_ID),
FOREIGN KEY (GENRE_ID) REFERENCES Genres(GENRE_ID)
)
ENGINE = INNODB;

INSERT INTO Songs (SONG_NAME, ARTIST_ID, ALBUM_ID, SONG_DUR, LANG_ID, GENRE_ID, SONG_PR) VALUES('Rehna Tu','1','1','00:6:51','7','8','4');
INSERT INTO Songs (SONG_NAME, ARTIST_ID, ALBUM_ID, SONG_DUR, LANG_ID, GENRE_ID, SONG_PR) VALUES('Dil Gira Daftan','1','1','00:5:40','7','11','5');
INSERT INTO Songs (SONG_NAME, ARTIST_ID, ALBUM_ID, SONG_DUR, LANG_ID, GENRE_ID, SONG_PR) VALUES('Need To Know','10','2','00:3:31','5','8','5');
INSERT INTO Songs (SONG_NAME, ARTIST_ID, ALBUM_ID, SONG_DUR, LANG_ID, GENRE_ID, SONG_PR) VALUES('El Melouk','13',NULL,'00:4:10','2','9','4');
INSERT INTO Songs (SONG_NAME, ARTIST_ID, ALBUM_ID, SONG_DUR, LANG_ID, GENRE_ID, SONG_PR) VALUES('Still With You','5', NULL,'00:3:59','4','1','5');
INSERT INTO Songs (SONG_NAME, ARTIST_ID, ALBUM_ID, SONG_DUR, LANG_ID, GENRE_ID, SONG_PR) VALUES('Tell Em','6', NULL,'00:3:00','5','3','5');
INSERT INTO Songs (SONG_NAME, ARTIST_ID, ALBUM_ID, SONG_DUR, LANG_ID, GENRE_ID, SONG_PR) VALUES('Uttradheenga','9','4','00:5:04','1','4','4');
INSERT INTO Songs (SONG_NAME, ARTIST_ID, ALBUM_ID, SONG_DUR, LANG_ID, GENRE_ID, SONG_PR) VALUES('Mirror Mirror','11', NULL,'00:4:14','8','3','3');
INSERT INTO Songs (SONG_NAME, ARTIST_ID, ALBUM_ID, SONG_DUR, LANG_ID, GENRE_ID, SONG_PR) VALUES('Side by Side','7', NULL,'00:2:50','4','3','4');
INSERT INTO Songs (SONG_NAME, ARTIST_ID, ALBUM_ID, SONG_DUR, LANG_ID, GENRE_ID, SONG_PR) VALUES('Sicko Mode','12','7','00:5:13','5','3','3');
INSERT INTO Songs (SONG_NAME, ARTIST_ID, ALBUM_ID, SONG_DUR, LANG_ID, GENRE_ID, SONG_PR) VALUES('Kama','4',NULL,'00:2:32','9','3','4');
INSERT INTO Songs (SONG_NAME, ARTIST_ID, ALBUM_ID, SONG_DUR, LANG_ID, GENRE_ID, SONG_PR) VALUES('Un Monstre a Paris','8',NULL,'00:2:36','10','8','5');
INSERT INTO Songs (SONG_NAME, ARTIST_ID, ALBUM_ID, SONG_DUR, LANG_ID, GENRE_ID, SONG_PR) VALUES('Hatchback','6', '3','00:2:32','5','3','4');
INSERT INTO Songs (SONG_NAME, ARTIST_ID, ALBUM_ID, SONG_DUR, LANG_ID, GENRE_ID, SONG_PR) VALUES('Cuidao Por Ahi','2', NULL,'00:3:20','6','12','4');
INSERT INTO Songs (SONG_NAME, ARTIST_ID, ALBUM_ID, SONG_DUR, LANG_ID, GENRE_ID, SONG_PR) VALUES('Mann Mohana','1','6','00:6:51','1','5','5');








