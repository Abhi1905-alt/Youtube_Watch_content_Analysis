DROP TABLE IF EXISTS watch_history;
DROP TABLE IF EXISTS videos;

CREATE TABLE videos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    video_url TEXT NOT NULL,
    thumbnail_url TEXT NOT NULL,
    category TEXT NOT NULL
);

CREATE TABLE watch_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    video_id INTEGER,
    watched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (video_id) REFERENCES videos (id)
);

-- Seed Data (Sample Videos)
INSERT INTO videos (title, description, video_url, thumbnail_url, category) VALUES 
('Learn Python in 10 Minutes', 'A quick crash course on Python basics.', 'https://www.w3schools.com/html/mov_bbb.mp4', 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5', 'Education'),
('Building a Startup from Scratch', 'The psychological and practical roadmap to entrepreneurship.', 'https://www.w3schools.com/html/mov_bbb.mp4', 'https://images.unsplash.com/photo-1519389950473-47ba0277781c', 'Business'),
('Funny Cat Compilation 2026', 'Try not to laugh at these cute kittens!', 'https://www.w3schools.com/html/mov_bbb.mp4', 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba', 'Entertainment'),
('Advanced Database Indexing', 'Optimize your SQL queries like a pro.', 'https://www.w3schools.com/html/mov_bbb.mp4', 'https://images.unsplash.com/photo-1544383835-bda2bc66a55d', 'Education'),
('ASMR Gaming - Relaxing Gameplay', 'Chill vibes and white noise gameplay.', 'https://www.w3schools.com/html/mov_bbb.mp4', 'https://images.unsplash.com/photo-1538481199705-c710c4e965fc', 'Entertainment');