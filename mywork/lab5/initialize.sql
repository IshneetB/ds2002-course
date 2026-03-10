USE dad8hw_db;

DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(100) NOT NULL,
    country VARCHAR(50),
    birth_year INT
);

CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    genre VARCHAR(50),
    publish_year INT,
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

INSERT INTO authors (author_id, author_name, country, birth_year) VALUES
(1, 'George Orwell', 'United Kingdom', 1903),
(2, 'Jane Austen', 'United Kingdom', 1775),
(3, 'Mark Twain', 'United States', 1835),
(4, 'Chinua Achebe', 'Nigeria', 1930),
(5, 'Haruki Murakami', 'Japan', 1949),
(6, 'Toni Morrison', 'United States', 1931),
(7, 'Gabriel Garcia Marquez', 'Colombia', 1927),
(8, 'J.K. Rowling', 'United Kingdom', 1965),
(9, 'Khaled Hosseini', 'Afghanistan', 1965),
(10, 'Margaret Atwood', 'Canada', 1939);

INSERT INTO books (book_id, title, genre, publish_year, author_id) VALUES
(101, '1984', 'Dystopian', 1949, 1),
(102, 'Animal Farm', 'Political Satire', 1945, 1),
(103, 'Pride and Prejudice', 'Romance', 1813, 2),
(104, 'Emma', 'Romance', 1815, 2),
(105, 'Adventures of Huckleberry Finn', 'Adventure', 1884, 3),
(106, 'Things Fall Apart', 'Historical Fiction', 1958, 4),
(107, 'Norwegian Wood', 'Fiction', 1987, 5),
(108, 'Beloved', 'Historical Fiction', 1987, 6),
(109, 'One Hundred Years of Solitude', 'Magical Realism', 1967, 7),
(110, 'Harry Potter and the Sorcerer''s Stone', 'Fantasy', 1997, 8);