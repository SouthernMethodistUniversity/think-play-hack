echo "starting Postgres"
pg_ctl -D /nfsscratch/tph_myth/reddit_db -l logfile start &&

echo "running the awesome command"
psql -h localhost -p 5432 --username=acambre -c "VACUUM FULL VERBOSE public.reddit;" reddit &&

echo "stopping postgres"
pg_ctl -D /nfsscratch/tph_myth/reddit_db stop
