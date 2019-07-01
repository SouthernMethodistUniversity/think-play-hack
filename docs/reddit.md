# Accessing reddit data
## Where it is
The reddit data is in a PostgreSQL database on m2. The whole dataset is over 1 TB, and the database lets you get portions of the data.
## Advisory
The reddit data is not filtered. You may see offensive information, even in subreddits that seem safe. Use discretion in what you use and share.
## SSH tunnel
Before you can use this database, you must turn on an SSH tunnel to m2.
### SSH tunnel first time setup (Windows only)
You need to do this once, only for Windows:
1. Open PuTTY. ([Download](https://www.chiark.greenend.org.uk/~sgtatham/putty/) and install if you don't already have it.)
2. On the left side, select **Connection** > **SSH** > **Tunnels**.
3. On the right side, fill in these fields:
   1. **Source port**: ``5432``
   2. **Destination**: ``login02.m2.smu.edu:5432``
4. Click **Add**.
5. On the left side, click on **Session** (the first selection).
6. For **Host Name (or IP address)**, enter ``login02.m2.smu.edu``.
7. For **Saved Sessions**, type ``login02.m2.smu.edu SSH tunnel``.
8. Click **Save**.

### Activating the SSH tunnel
#### Apple or Linux
1. Open a new terminal window.
2. Type this into your terminal and press enter, replacing **username** with your m2 username: `ssh -C -Y -L 5432:localhost:5432 username@login02.m2.smu.edu`
#### Windows
1. Open PuTTY.
2. Under **Saved Sessions**, double-click on **login02.m2.smu.edu SSH tunnel**.
3. If prompted, accept the certificate for login02.m2.smu.edu.
4. When prompted, enter your m2 username and password.

### When to close the SSH tunnel

Keep the PuTTY or terminal window open the whole time you need to connect to the PostgreSQL database. Once you've downloaded all the data you need, it's fine to close the connection.
## Connecting to PostgreSQL in R

You need the RPostgreSQL package installed first. If it's not installed, run `install.packages("RPostgreSQL")` in R. You only need to run this once.

Load the library and driver:
```R
library(RPostgreSQL)
drv <- dbDriver("PostgreSQL")
```

Create a connection to the database:
```R
con <- dbConnect(drv, dbname = "reddit",
                 host = "localhost",
                 port = 5432,
                 user = "tph_read",
                 password = "think-play-hack")
```

Now you'll execute your query. More info on how to build a proper query is below. (This code will not work without constructing a query!) Change the object name to something that describes the data.
```R
reddit_data <- dbGetQuery(con, "replace this with a proper SQL query")
```
When you are done getting data from the database, disconnect using this command:
```R
dbDisconnect(con)
```
## Creating SQL queries
The SQL queries you'll use start with this:
```SQL
SELECT id, ups, downs, parent_id, body, subreddit_id, subreddit, link_id, created_utc, created_utc_timestamp, author
FROM reddit_new
WHERE ...
```
What you need to build is the `WHERE` clause. This filters things down so that you don't overwhelm yourself with 1.6 billion rows of data!

### Filtering by subreddit
Determine which subreddits you want to edit. The dataset has almost 240,000 subreddits. The full list of subreddits is available here. Get the list: [CSV](https://drive.google.com/open?id=102CuIB5B9WYJdh5lNxWNXIoojBa3LyLN) (4.9 MB) [Google Sheet](https://docs.google.com/spreadsheets/d/1QiVw0hvYDbTY1enAmgG1PfJnQqWG6utwveVlvJL_cl4/edit?usp=sharing) (may be slow).

Once you know your subreddits, build a `WHERE` clause to filter by them. First, create a comma-separated list of subreddits you want to get, like this:
```SQL
subreddit IN ("BoyScoutsofAmerica","cubscouts","EagleScout","EagleScouts","Eagle_Scouts","EagleScoutsOnReddit")
```
Important notes:
* Keep capitalization, punctuation, all other details the same. Differences will prevent that subreddit from appearing.
* Sometimes, there will be multiple subreddits for one topic.

Now replace the ellipsis (...) in the sample SQL query above (starts with `SELECT`) with the clause you just created. Viola, you have a SQL query! Take that query and substitute it in the R code where I wrote `replace this with a proper SQL query`.

### Other filtering
It is possible to filter by other criteria, such as date and more. These criteria can be in addition to or instead of filtering by subreddit. Aren Cambre can help you create the proper SQL query for this.

## Exporting the data
If you would like to use something other than R to analyze the data you downloaded, you can export it. All the below commands come from Tidyverse libraries, so let's load the Tidyverse first:
```R
install.packages(tidyverse) # only run this line if you have not done this since installing R
library(tidyverse)
```

Assuming you used the same `reddit_data` object name as above, you can use this command to export your data to a CSV:
```R
write_csv(reddit_data, "reddit_data.csv")
```

Want to write to a TSV instead?
```R
write_tsv(reddit_data, "reddit_data.csv")
```
