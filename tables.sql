create table images (
    imgid integer NOT NULL GENERATED ALWAYS AS IDENTITY primary key,
    imgdata bytea
);
