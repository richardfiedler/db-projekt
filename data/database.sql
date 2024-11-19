BEGIN;


CREATE TABLE IF NOT EXISTS public.geraete
(
    geraeteid integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    soll_laufen boolean NOT NULL DEFAULT false,
    CONSTRAINT geraete_pkey PRIMARY KEY (geraeteid)
);

CREATE TABLE IF NOT EXISTS public.laufzeitregeln
(
    geraeteid integer NOT NULL,
    startzeit timestamp without time zone NOT NULL,
    endzeit timestamp without time zone NOT NULL,
    CONSTRAINT laufzeitregeln_pkey PRIMARY KEY (geraeteid, startzeit, endzeit)
);

CREATE TABLE IF NOT EXISTS public.preise
(
    stromanbieterid integer NOT NULL,
    preishoehe double precision NOT NULL,
    gueltig_ab timestamp without time zone NOT NULL,
    CONSTRAINT preise_pkey PRIMARY KEY (stromanbieterid, gueltig_ab)
);

CREATE TABLE IF NOT EXISTS public.stromanbieter
(
    stromanbieterid integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT stromanbieter_pkey PRIMARY KEY (stromanbieterid)
);

ALTER TABLE IF EXISTS public.laufzeitregeln
    ADD CONSTRAINT geraeteid FOREIGN KEY (geraeteid)
    REFERENCES public.geraete (geraeteid) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;
CREATE INDEX IF NOT EXISTS fki_geraeteid
    ON public.laufzeitregeln(geraeteid);


ALTER TABLE IF EXISTS public.preise
    ADD CONSTRAINT preise_stromanbieterid_fkey FOREIGN KEY (stromanbieterid)
    REFERENCES public.stromanbieter (stromanbieterid) MATCH SIMPLE
    ON UPDATE CASCADE
    ON DELETE CASCADE
    NOT VALID;
CREATE INDEX IF NOT EXISTS fki_s
    ON public.preise(stromanbieterid);

END;
