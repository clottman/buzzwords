# How innovative is the Raikes School of Computer Science and Management? Let's find out!

The analysis was initially ran in January 2014. See the file [analysisOutputOld](analysisResults/analysisOutput_Old.txt) for its results.
The text used for this analysis included all the anchor, paragraph, H1, and H5 tags on the website. This covered the majority of text.

Later in 2014, the Raikes School website underwent rebranding. After this rebranding, in August 2014, I  ran the analysis again using the text from the same HTML elements as before. See [here](analysisResults/analysisOutput_RebrandingOldTags.txt).

However, the updated website used all header elements 1-5 regularly, and also placed more content in span and blockquote elements. These elements were included in [this](analysisResults/analysisOutput_RebrandingMoreTags) analysis.


### Usage:

To crawl:
In the project folder in a console window with python installed:
```
scrapy crawl **spider name** -o **output file name** -t **output file type**
```
To run the analysis:
```
python analysis.py
```
