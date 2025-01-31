-- This is a valid SQL comment
CREATE TABLE IF NOT EXISTS business_ideas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    idea_name VARCHAR(255) NOT NULL,
    market_size INT,
    competition INT,
    budget INT,
    risk INT
);

INSERT INTO business_ideas (idea_name, market_size, competition, budget, risk) 
VALUES 
    ('E-commerce Platform', 1000, 200, 500, 50),
    ('Food Delivery App', 800, 150, 400, 60);
