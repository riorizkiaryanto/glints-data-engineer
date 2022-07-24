--
-- PostgreSQL database dump
--

-- Dumped from database version 12.11
-- Dumped by pg_dump version 14.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: sales_record; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sales_record (
    id integer NOT NULL,
    date_record date NOT NULL,
    sales numeric(50,0)
);


ALTER TABLE public.sales_record OWNER TO postgres;

--
-- Name: sales_record_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.sales_record_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sales_record_id_seq OWNER TO postgres;

--
-- Name: sales_record_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.sales_record_id_seq OWNED BY public.sales_record.id;


--
-- Name: sales_record id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sales_record ALTER COLUMN id SET DEFAULT nextval('public.sales_record_id_seq'::regclass);


--
-- Data for Name: sales_record; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sales_record (id, date_record, sales) FROM stdin;
1	2022-07-14	100
2	2022-07-15	50
3	2022-07-16	45
4	2022-07-17	80
5	2022-07-18	200
6	2022-07-19	30
7	2022-07-20	100
8	2022-07-21	100
9	2022-07-22	90
10	2022-07-23	300
11	2022-07-24	40
\.


--
-- Name: sales_record_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sales_record_id_seq', 11, true);


--
-- Name: sales_record sales_record_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sales_record
    ADD CONSTRAINT sales_record_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

