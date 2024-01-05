-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema esquema_belt_reviewer
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema esquema_belt_reviewer
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_belt_reviewer` DEFAULT CHARACTER SET utf8 ;
USE `esquema_belt_reviewer` ;

-- -----------------------------------------------------
-- Table `esquema_belt_reviewer`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_belt_reviewer`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_belt_reviewer`.`grades`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_belt_reviewer`.`grades` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `student` VARCHAR(45) NULL,
  `stack` VARCHAR(45) NULL,
  `date` DATE NULL,
  `grade` FLOAT NULL,
  `belt` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_grades_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_grades_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `esquema_belt_reviewer`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
