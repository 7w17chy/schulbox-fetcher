# German students: Please read on!
# Why the fvck are all variable names and `print()` outputs in German?
Schulbox is a German-only service (maybe it's even limited to Rheinland-Pfalz), as far as I know. If not, please correct me and I'll translate it.

# Make this shovelware work
Go to schulbox.bildung-rp.de, log in, and rightclick on 'Download all files'. You have two options:

Option 1: Copy the link and paste it directly in the script

```python
zip_datei = urllib.request.urlretrieve(open('LINK.txt').read().replace('\n', ''), 'zipdatei.zip')
```
Replace `(open('LINK.txt')...) ,` with the link.

Option 2:
Paste the link in a file called `LINK.txt` in the same directory as the script.

## Tool written in Python to notify the user about new exercises/news from their teachers.
Here in Rheinland-Pfalz, Germany, we've got a service called 'Schulbox'. It's basically a cloud (based on Nextcloud, I think), which allows
teachers to upload school materials like exercises as files, so that students can easily access it.
It is/was (depending on when you read it xD) heavily used during the corona crisis. Since it's really annoying to go to that website and search
through all folders to check whether new materials were uploaded or not. This script does take some work from you, but not all: for now, it only tells you that there are new materials; by comparing the size of the downloaded zip file.

# But hold up, I'll add more functionality ASAP! Probably tomorrow. You could of course just extend it yourself (and submit a pullrequest, if you so please).

# Why is it written in Python?
Well, for simplicity's sake and because many students in Germany learn/know Python.
