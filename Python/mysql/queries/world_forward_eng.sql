-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mysql_countries
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mysql_countries
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mysql_countries` DEFAULT CHARACTER SET utf8 ;
USE `mysql_countries` ;

-- -----------------------------------------------------
-- Table `mysql_countries`.`countries`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mysql_countries`.`countries` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `code` CHAR(3) NULL,
  `name` CHAR(52) NULL,
  `continent` ENUM('north_america', 'south_america', 'europe', 'asia', 'australia', 'antartica') NULL,
  `region` CHAR(26) NULL,
  `surface_area` FLOAT(10,2) NULL,
  `indep_year` SMALLINT(6) NULL,
  `population` INT(11) NULL,
  `life_expectancy` FLOAT(3,1) NULL,
  `gnp` FLOAT(10,2) NULL,
  `local_name` CHAR(45) NULL,
  `government_form` CHAR(45) NULL,
  `head_of_state` CHAR(60) NULL,
  `capital` INT(11) NULL,
  `code2` CHAR(2) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mysql_countries`.`languages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mysql_countries`.`languages` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `country_code` CHAR(3) NULL,
  `language` CHAR(30) NULL,
  `is_offical` ENUM('T', 'F') NULL,
  `percentage` FLOAT(4,1) NULL,
  `countries_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_languages_countries_idx` (`countries_id` ASC) VISIBLE,
  CONSTRAINT `fk_languages_countries`
    FOREIGN KEY (`countries_id`)
    REFERENCES `mysql_countries`.`countries` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mysql_countries`.`cities`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mysql_countries`.`cities` (
  `id` INT(11) NOT NULL,
  `name` CHAR(35) NULL,
  `country_code` CHAR(3) NULL,
  `district` CHAR(20) NULL,
  `population` INT(11) NULL,
  `countries_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_cities_countries1_idx` (`countries_id` ASC) VISIBLE,
  CONSTRAINT `fk_cities_countries1`
    FOREIGN KEY (`countries_id`)
    REFERENCES `mysql_countries`.`countries` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
