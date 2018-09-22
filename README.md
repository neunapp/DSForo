# DSForo
Foro DeporStart
CREATE INDEX entrada_title_idx ON entradas_entry USING GIN(title gin_trgm_ops);
